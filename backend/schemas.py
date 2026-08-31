from typing import Literal

from pydantic import BaseModel


FeedMode = Literal["latest", "following"]


class FeedPreferenceUpdate(BaseModel):
    default_feed_mode: FeedMode