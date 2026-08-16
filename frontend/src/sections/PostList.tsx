// displays many posts
// knows: which posts it received, maybe empty-feed state
// doesn't decide ranking

import PostCard from './PostCard'
import type { Post } from "../types/Post";

interface PostListProps {
    posts: Post[]
}

function PostList({ posts }: PostListProps) {
    return(
        <section id="posts">
            <h1>Posts</h1>
            <div>
                {posts.map((post) => (
                    <PostCard 
                        key={post.id} 
                        creator={post.creator} 
                        topic={post.topic} 
                        content={post.content} 
                        timestamp={post.timestamp}
                    />
                ))}
            </div>
        </section>
    );
}

export default PostList;