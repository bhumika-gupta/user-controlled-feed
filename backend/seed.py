# create fake users -> create fake posts belonging to those users -> commit them to postgresql

from database import SessionLocal
from models import User, Post, Follow

def seed_database():
    db = SessionLocal()

    try:
        # create users
        creator1 = User(username="randomcreator1")
        creator2 = User(username="randomcreator2")
        creator3 = User(username="randomcreator3")

        # add users
        db.add_all([
            creator1,
            creator2,
            creator3
        ])

        # create posts associated with same users
        post1 = Post(
            creator=creator1,
            topic="technology",
            content="new phone update is actually kinda nice"
        )

        post2 = Post(
            creator=creator2,
            topic="music",
            content="ep release coming to u this friday"
        )

        post3 = Post(
            creator=creator3,
            topic="photography",
            content="sunset"
        )

        post4 = Post(
            creator=creator1,
            topic="politics",
            content="vote for her she actually cares about the wellbeing of society"
        )

        post5 = Post(
            creator=creator1,
            topic="photography",
            content="look at this beautiful solar eclipse!"
        )

        post6 = Post(
            creator=creator3,
            topic="fashion",
            content="huge warehouse sale this weekend"
        )

        # add posts
        db.add_all([
            post1,
            post2,
            post3,
            post4,
            post5,
            post6
        ])

        db.commit()
        print("Database seeded successfully.")

    finally:
        db.close()

if __name__ == "__main__":
    seed_database()