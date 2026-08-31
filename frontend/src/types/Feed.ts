export type FeedMode = "latest" | "following";

export interface FeedPreference {
    default_feed_mode: FeedMode;
}