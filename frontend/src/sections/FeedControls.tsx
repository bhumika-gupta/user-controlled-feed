// handles the user's feed preferences
// initially: latest, following
// eventually: user directed. topics, ranking preferences

function FeedControls() {
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
                    className="feed-option feed-option-active"
                >
                    Latest
                </button>
                <button
                    type="button"
                    className="feed-option"
                >
                    Following
                </button>
            </div>
        </section>
    );
}

export default FeedControls