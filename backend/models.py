from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    # one user can have many posts
    # back_populates links this to Post.creator below
    posts: Mapped[list["Post"]] = relationship(
        back_populates="creator"
    )

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)

    # foreign key connects each post to an existing user
    # index=True makes filtering posts by creator faster; tells SQLalchemy to create a database index on that column (index=extra data structure postgresql maintains so that it can find rows matching that col faster)
    creator_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    topic: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    # postgresql automatically fills in the current time when a new post is inserted without created_at
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # lets python access the User object for this post as post.creator
    creator: Mapped["User"] = relationship(
        back_populates="posts"
    )

class Follow(Base):
    __tablename__ = "follows"

    # prevents the same follow relationship from being stored more than once
    # the pair (follower_id, followed_id) must be unique
    __table_args__ = (
        UniqueConstraint(
            "follower_id",
            "followed_id",
            name="uq_follower_followed"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    # the user who is doing the following
    # points to that user's row in the users table
    follower_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    # the user who is being followed
    # also points to a row in the users table
    followed_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    # lets Python access the User object represented by follower_id
    # foreign_keys is needed because Follow has two foreign keys pointing to users.id
    follower: Mapped["User"] = relationship(
        foreign_keys=[follower_id]
    )

    # lets Python access the User object represented by followed_id
    followed: Mapped["User"] = relationship(
        foreign_keys=[followed_id]
    )

class FeedPreference(Base):
    __tablename__ = "feed_preferences"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True, # each user should only have one current preference record
        nullable=False,
        index=True
    )

    default_feed_mode: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        server_default="latest"
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(), # SQLAlchemy will update the timestamp when it issues an update
        nullable=False
    )
