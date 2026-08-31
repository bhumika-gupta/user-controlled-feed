// coordinates the page
// get feed data -> supply it to the list -> display controls -> respond when controls change

import PostList from "../sections/PostList";
import FeedControls from "../sections/FeedControls";
import type { Post } from "../types/Post";
import type { FeedMode } from "../types/Feed"
import { useState, useEffect } from 'react';
import "./FeedPage.css";

function FeedPage() {
    const [posts, setPosts] = useState<Post[]>([]); // posts = the feed data currently available to the UI
    const [loading, setLoading] = useState(false); // loading is a flag to show whether we're currently waiting for a response from the server/backend
    const [error, setError] = useState<string | null>(null); // error message if the fetch fails or returns an error
    const [feedMode, setFeedMode] = useState<FeedMode | null>(null);

    useEffect(() => {
        async function fetchFeedPreference() {
            try {
                const response = await fetch(
                    "http://127.0.0.1:8000/feed-preference"
                );

                if (!response.ok) {
                    throw new Error("Failed to fetch feed preference");
                }

                const data = await response.json();

                setFeedMode(data.default_feed_mode);
            } catch (err) {
                setError("Something went wrong. Please try again.");
            }
        }

        fetchFeedPreference();
    }, []); // [] = get the user's saved preference once when the page mounts

    useEffect(() => {
        if (feedMode === null) {
            return;
        }

        // useEffect itself shouldn't be async, so define async function inside it:
        async function fetchFeed() {
            // about to start an external request
            setLoading(true); // start loading message
            setError(null); // clear any previous errors

            try {
                // start the HTTP request to fastAPI
                // "await" pauses THIS async function until the response arrives
                const response = await fetch(`http://127.0.0.1:8000/feed?mode=${feedMode}`);
                
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

    }, [feedMode]); // [feedMode] = effect should react whenever feedMode changes

    return (
        <main className="feed-page">
            <div className="feed-shell">

                <header className="feed-header">
                    <div>
                        <p className="feed-eyebrow">USER-CONTROLLED FEED</p>
                        <h1 className="feed-title">Your Feed</h1>
                        <p className="feed-subtitle">
                            A social feed designed to give users explicit control
                            over how content is ranked and delivered.
                        </p>
                    </div>
                </header>

                {feedMode === null && !error && (
                    <p className="feed-message">Loading preferences...</p>
                )}

                {feedMode !== null && (
                    <FeedControls 
                        feedMode={feedMode}
                        onFeedModeChange={setFeedMode}
                    />
                )}
                

                {/* while the backend request is still running */}
                {loading && (
                    <p className="feed-message">Loading feed...</p>
                )}

                {/* if the request failed*/}
                {error && (
                    <p className="feed-message feed-error">{error}</p>
                )}

                {/* only show the feed once we're not loading and there's no error */}
                {!loading && !error && feedMode !== null && (
                    <PostList posts={posts} />
                )}
            </div>
        </main>
    );
}

export default FeedPage;
