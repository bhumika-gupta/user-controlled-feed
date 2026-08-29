from sqlalchemy import select

from database import SessionLocal
from models import Follow, User


def seed_demo_user():
    db = SessionLocal()

    try:
        # look up the existing users by username
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

        # check whether the demo user already exists
        existing_demo_user = db.scalar(
            select(User).where(User.username == "demo_user")
        )

        if existing_demo_user is not None:
            print("Demo user already exists")
            return

        # create the demo user
        demo_user = User(username="demo_user")

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
             demo_user,
             follow_relationship_demo_1,
             follow_relationship_demo_3
        ])

        db.commit()
        print("Demo user and follow relationships seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_demo_user()