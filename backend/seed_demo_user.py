from sqlalchemy import select

from database import SessionLocal
from models import Follow, User, FeedPreference


def seed_demo_user():
    db = SessionLocal()

    try:
        # look up the existing creators
        randomcreator1 = db.scalar(
            select(User).where(User.username == "randomcreator1")
        )

        randomcreator2 = db.scalar(
            select(User).where(User.username == "randomcreator2")
        )

        randomcreator3 = db.scalar(
            select(User).where(User.username == "randomcreator3")
        )

        if (
            randomcreator1 is None 
            or randomcreator2 is None 
            or randomcreator3 is None
        ):
            print("One or more creators were not found.")
            return

        # look for existing demo user
        demo_user = db.scalar(
            select(User).where(User.username == "demo_user")
        )

        # create demo user only if it already doesn't exist
        if demo_user is None:
            demo_user = User(username="demo_user")
            db.add(demo_user)

            # flush sends the INSERT to PostgreSQL so demo_user gets an id without commiting the whole transaction yet
            db.flush()

            # demo_user follows creator1
            follow_relationship_demo_1 = Follow(
                follower=demo_user,
                followed=randomcreator1
            )

            # demo_user follows creator3
            follow_relationship_demo_3 = Follow(
                follower=demo_user,
                followed=randomcreator3
            )

            # no Follow row is created for randomcreator2, meaning demo_user doesn't follow creator2

            db.add_all([
                follow_relationship_demo_1,
                follow_relationship_demo_3
            ])

            print("Demo user and follow relationships created.")
        else:
            print("Demo user already exists")

        # check whether this user already has a feed preference
        existing_preference = db.scalar(
            select(FeedPreference).where(
                FeedPreference.user_id == demo_user.id
            )
        )

        # create preference only if missing
        if existing_preference is None:
            feed_preference = FeedPreference(
                user_id = demo_user.id,
                default_feed_mode="latest"
            )

            db.add(feed_preference)
            print("Feed preference created.")

        db.commit()
        print("Demo user seed completed successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_demo_user()