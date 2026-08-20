// coordinates the page
// get feed data -> supply it to the list -> display controls -> respond when controls change

import PostList from "../sections/PostList";
import FeedControls from "../sections/FeedControls";
import type { Post } from "../types/Post";
import { useState, useEffect } from 'react';

function FeedPage() {
    const [posts, setPosts] = useState<Post[]>([]); // posts = the feed data currently available to the UI
    const [loading, setLoading] = useState(false); // loading is a flag to show whether we're currently waiting for a response from the server/backend
    const [error, setError] = useState<string | null>(null); // error message if the fetch fails or returns an error

    useEffect(() => {
        // useEffect itself shouldn't be async, so define async function inside it:
        async function fetchFeed() {
            // about to start an external request
            setLoading(true); // start loading message
            setError(null); // clear any previous errors

            try {
                // start the HTTP request to fastAPI
                // "await" pauses THIS async function until the response arrives
                const response = await fetch("http://127.0.0.1:8000/feed");
                
                // fetch() doesn't automatically throw for 404/500 responses, so explicitly treat unsuccessful HTTP responses as errors:
                if (!response.ok) {
                    throw new Error("Failed to fetch feed");
                }

                // convert the JSON response body into a JavaScript object
                const data = await response.json();

                // store the returned posts in React state. this causes React to render FeedPage again
                setPosts(data.feed);
            } catch (err) {
                setError("Something went wrong. Please try again.");
            } finally { // runs whether the request succeeded or failed
                setLoading(false);
            }
        }

        // actually start the async work after FeedPage renders
        fetchFeed();
        
        // [] = empty dependency array: run this effect when FeedPage first mounts (when React creates it and puts it into the UI for the first time)
    }, []);

    return (
        <main>
            <FeedControls />

            {/* while the backend request is still running */}
            {loading && <p>Loading...</p>}

            {/* if the request failed*/}
            {error && <p style={{ color: 'red' }}>{error}</p>}

            {/* only show the feed once we're not loading and there's no error */}
            {!loading && !error && <PostList posts={posts} />}
        </main>
    );
}

export default FeedPage;
