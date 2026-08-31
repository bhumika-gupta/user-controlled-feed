from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Post, User, Follow, FeedPreference
from schemas import FeedMode, FeedPreferenceUpdate

import models
from database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
def get_health():
    return {"status": "healthy"}

@app.get("/feed")
def get_feed(db: Session = Depends(get_db), mode: FeedMode = "latest"):
    
    if mode == "following":
        demo_user = db.scalar(
            select(User).where(User.username == "demo_user")
        )
        if demo_user is None:
            raise HTTPException(status_code=404, detail="demo_user not found")

        followed_users_ids_by_demo_user = select(Follow.followed_id).where(
            Follow.follower_id==demo_user.id
        )

        statement_followed_posts = (
            select(Post)
            .where(Post.creator_id.in_(followed_users_ids_by_demo_user))
            .order_by(Post.created_at.desc())
        )

        posts = db.scalars(statement_followed_posts).all()
    else:
        statement_all_posts = select(Post).order_by(
            Post.created_at.desc()
        )
        
        posts = db.scalars(statement_all_posts).all()

    feed_list = [
        {
        "id": post.id,
        "creator": post.creator.username,
        "topic": post.topic,
        "content": post.content,
        "timestamp": post.created_at.isoformat()
        }
        for post in posts
    ]
    
    return {
        "feed": feed_list
    }

# tell frontend the current saved feed mode
@app.get("/feed-preference") 
def get_feed_preference(db: Session = Depends(get_db)):
    demo_user = db.scalar(
        select(User).where(User.username == "demo_user")
    )

    if demo_user is None:
        raise HTTPException(status_code=404, detail="demo_user not found")

    feed_preference_demo_user = db.scalar(
        select(FeedPreference).where(
            FeedPreference.user_id == demo_user.id
        )
    )

    if feed_preference_demo_user is None:
        raise HTTPException(status_code=404, detail=f"Feed preference for {demo_user.username} not found")

    return {
        "default_feed_mode": feed_preference_demo_user.default_feed_mode
    }

# change the saved feed mode
@app.patch("/feed-preference")
def update_feed_preference(
    preference_update: FeedPreferenceUpdate,
    db: Session = Depends(get_db)
):
    demo_user = db.scalar(
        select(User).where(User.username == "demo_user")
    )

    if demo_user is None:
            raise HTTPException(status_code=404, detail="demo_user not found")

    feed_preference_demo_user = db.scalar(
        select(FeedPreference).where(
            FeedPreference.user_id == demo_user.id
        )
    )

    if feed_preference_demo_user is None:
        raise HTTPException(status_code=404, detail=f"Feed preference for {demo_user.username} not found")

    feed_preference_demo_user.default_feed_mode = (
        preference_update.default_feed_mode
    )

    db.commit()
    db.refresh(feed_preference_demo_user)

    return {
        "default_feed_mode": feed_preference_demo_user.default_feed_mode
    }
