// handles the user's feed preferences
// initially: latest, following
// eventually: user directed. topics, ranking preferences

function FeedControls() {
    return (
        <div>
            <p>Feed: </p>
            <button>
                [Latest]
            </button>
            <button>
                [Following]
            </button>
        </div>
    )

}

export default FeedControls