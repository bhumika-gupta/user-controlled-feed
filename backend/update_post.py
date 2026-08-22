from sqlalchemy import select

from database import SessionLocal
from models import Post


def update_post():
    db = SessionLocal()

    try:
        post = db.scalar(
            select(Post).where(Post.id == 4)
        )

        if post is None:
            print("Post not found.")
            return

        post.content = "actually curious how this debate is gonna go"

        db.commit()
        print("Post updated successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    update_post()