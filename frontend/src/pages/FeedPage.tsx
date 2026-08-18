// coordinates the page
// get feed data -> supply it to the list -> display controls -> respond when controls change

import PostList from "../sections/PostList";
import FeedControls from "../sections/FeedControls";
import type { Post } from "../types/Post";
import { useState, useEffect } from 'react';

function FeedPage() {
    const [posts, setPosts] = useState<Post[]>([]);

    useEffect(() => {
        // fetch feed from FastAPI
        fetch("http://127.0.0.1:8000/feed")
        // convert response to JSON
            .then((data) => data.json())
        // take data.feed
            .then((data) => {
                // call setPosts(data.feed)
                setPosts(data.feed);
            })
    }, []);

    return (
        <main>
            <FeedControls />
            <PostList posts={posts} />
        </main>
    );
}

export default FeedPage;
