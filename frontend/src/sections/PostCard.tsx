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
    return (
        <div>
        <p>{creator}</p>
        <p>{topic}</p>
        <p>{content}</p>
        <p>{timestamp}</p>
        </div>
    )
}

export default PostCard