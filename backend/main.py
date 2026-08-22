from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Post

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
def get_feed(db: Session = Depends(get_db)):
    statement = select(Post).order_by(Post.created_at.desc())
    posts = db.scalars(statement).all()

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

