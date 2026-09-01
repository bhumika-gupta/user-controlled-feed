from datetime import datetime, timezone

import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base, get_db
from main import app
from models import User, Post, Follow, FeedPreference

TEST_DATABASE_URL = "sqlite://" # in-memory SQLite database

# create a separate in-memory database engine used only by tests
test_engine = create_engine(
    TEST_DATABASE_URL, 
    connect_args={"check_same_thread": False}, # bypasses SQLite's same-thread restriction
    poolclass=StaticPool, # tells SQLite to reuse the same underlying SQLite connection (for pytest setup, FastAPI request, SQLAlchemy session)
    )

# create database sessions connected to the test DB instead of PostgreSQL
TestingSessionLocal = sessionmaker(
    autoflush=False, 
    bind=test_engine
)

# fixture: test_database
# create tables
@pytest.fixture
def test_database():
    # start every test with a completely clean database
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)

    # seed known data
    test_db = TestingSessionLocal()

    try:
        # create test users
        creator1 = User(username="randomcreator1")
        creator2 = User(username="randomcreator2")
        creator3 = User(username="randomcreator3")
        demo_user = User(username="demo_user")

        # add test users
        test_db.add_all([
            creator1,
            creator2,
            creator3,
            demo_user,
        ])

        # give the User objects database IDs before creating related rows
        test_db.flush()

        # create follow relationships
        # demo_user follows creator1 and creator3,
        # but NOT creator2.
        follow1 = Follow(
            follower=demo_user,
            followed=creator1,
        )

        follow3 = Follow(
            follower=demo_user,
            followed=creator3,
        )

        # create default preference
        preference = FeedPreference(
            user_id=demo_user.id,
            default_feed_mode="latest",
        )

        # create posts associated with same users
        post1 = Post(
            creator=creator2,
            topic="technology",
            content="why do my headphones keep dying???",
            created_at=datetime(
                2026, 8, 1, 12, 0,
                tzinfo=timezone.utc,
            ),
        )

        post2 = Post(
            creator=creator3,
            topic="music",
            content="definitely a no skip album",
            created_at=datetime(
                2026, 8, 2, 12, 0,
                tzinfo=timezone.utc,
            ),
        )

        post3 = Post(
            creator=creator1,
            topic="photography",
            content="cool new graffiti",
            created_at=datetime(
                2026, 8, 3, 12, 0,
                tzinfo=timezone.utc,
            ),
        )

        test_db.add_all([
            follow1,
            follow3,
            preference,
            post1,
            post2,
            post3,
        ])

        test_db.commit()
        print("Test seed completed successfully.")

    finally:
        test_db.close()

    # the test itself runs here
    try:
        yield
    finally:
        # drop tables (after the test finishes, remove everything)
        Base.metadata.drop_all(bind=test_engine)



# fixture: client
# override get_db
@pytest.fixture
def client(test_database):
    
    def override_get_db():
        db = TestingSessionLocal()

        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    # create TestClient
    with TestClient(app) as test_client:
        # yield client
        yield test_client

    # remove override (make sure the real app dependency is restored afterward)
    app.dependency_overrides.clear()
