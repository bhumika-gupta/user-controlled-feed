from datetime import datetime
from typing import Literal

from pydantic import BaseModel


FeedMode = Literal["latest", "following"]

# request body sent when the user changes their feed mode preference
class FeedPreferenceUpdate(BaseModel):
    default_feed_mode: FeedMode

# one post returned by the API
class PostResponse(BaseModel):
    id: int
    creator: str
    topic: str
    content: str
    timestamp: datetime

# response returned by GET /feed
class FeedResponse(BaseModel):
    feed: list[PostResponse]

# response returned by GET/PATCH /feed-preference
class FeedPreferenceResponse(BaseModel):
    default_feed_mode: FeedMode