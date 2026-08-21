from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
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

