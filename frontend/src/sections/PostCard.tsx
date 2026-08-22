// display one post
// knows things like: creator, content, topic, timestamp

// import React from 'react'

type PostCardProps = {
    creator: string
    topic: string
    content: string
    timestamp: string
}

function PostCard({creator, topic, content, timestamp}: PostCardProps) {
    const formattedTimestamp = new Intl.DateTimeFormat("en-CA", {
        month: "short",
        day: "numeric",
        hour: "numeric",
        minute: "2-digit",
    }).format(new Date(timestamp));

    return (
        <article className="post-card">
            <div className="post-header">
                <div className="post-avatar">
                    {creator.charAt(0).toUpperCase()}
                </div>

                <div className="post-meta">
                    <strong className="post-creator">{creator}</strong>
                    <span className="post-time">{formattedTimestamp}</span>
                </div>

                <span className="post-topic">{topic}</span>
            </div>

            <p className="post-content">{content}</p>
        </article>
    )
}

export default PostCard