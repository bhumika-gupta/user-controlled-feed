// handles the user's feed preferences
// initially: latest, following
// eventually: user directed. topics, ranking preferences

import type { FeedMode } from "../types/Feed"

interface FeedControlsProps {
    feedMode: FeedMode;
    onFeedModeChange: (mode: FeedMode) => void;
}


function FeedControls({feedMode, onFeedModeChange}: FeedControlsProps) {
    return (
        <section className="feed-controls">
            <div>
                <p className="control-label">Feed ranking</p>
                <p className="control-description">
                    Choose how posts are ordered.
                </p>
            </div>

            <div className="feed-options">
                <button
                    type="button"
                    className={
                        feedMode === "latest" 
                            ? "feed-option feed-option-active"
                            : "feed-option"
                    } 
                    onClick={() => onFeedModeChange("latest")}
                >
                    Latest
                </button>
                <button
                    type="button"
                    className={
                        feedMode === "following"
                            ? "feed-option feed-option-active"
                            : "feed-option"
                    }
                    onClick={() => onFeedModeChange("following")}
                >
                    Following
                </button>
            </div>
        </section>
    );
}

export default FeedControls