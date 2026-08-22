// displays many posts
// knows: which posts it received, maybe empty-feed state
// doesn't decide ranking

import PostCard from './PostCard'
import type { Post } from "../types/Post";

interface PostListProps {
    posts: Post[]
}

function PostList({ posts }: PostListProps) {
    if (posts.length === 0) {
        return <p className="feed-message">No posts to show yet.</p>
    }

    return(
        <section className="post-list" aria-label="Feed posts">
            {posts.map((post) => (
                <PostCard 
                    key={post.id} 
                    creator={post.creator} 
                    topic={post.topic} 
                    content={post.content} 
                    timestamp={post.timestamp}
                />
            ))}
        </section>
    );
}

export default PostList;