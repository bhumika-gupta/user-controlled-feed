// coordinates the page
// get feed data -> supply it to the list -> display controls -> respond when controls change

import PostList from "../sections/PostList";
import FeedControls from "../sections/FeedControls";
import type { Post } from "../types/Post";

const postData: Post[] = [
    {
        id: 1,
        creator: 'randomcreator1', 
        topic: "technology", 
        content: "ai this ai that", 
        timestamp: "10:00 August 11 2026"
    },
    {
        id: 2,
        creator: 'randomcreator1', 
        topic: "technology", 
        content: "ai this ai that", 
        timestamp: "10:00 August 11 2026"
    },
    {
        id: 3,
        creator: "randomcreator3", 
        topic: "photography", 
        content: "sunset", 
        timestamp: "20:00 August 13 2026"
    }
];

function FeedPage() {
    return (
        <main>
            <FeedControls />
            <PostList posts={postData} />
        </main>
    );
}

export default FeedPage;
