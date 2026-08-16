// displays many posts
// knows: which posts it received, maybe empty-feed state
// doesn't decide ranking

import PostCard from './PostCard'

function PostList() {
    <section id="posts">
        <h1>Posts</h1>
        <div>
            <PostCard
                creator="randomcreator1"
                topic="technology"
                content="ai this ai that"
                timestamp="10:00 August 11 2026"
            />
            <PostCard
                creator="randomcreator2"
                topic="music"
                content="ep release coming to u this friday"
                timestamp="14:00 August 12 2026"
            />
            <PostCard
                creator="randomcreator3"
                topic="photography"
                content="sunset"
                timestamp="20:00 August 13 2026"
            />
        </div>
    </section>
}

export default PostList