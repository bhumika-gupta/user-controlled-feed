
# test 1 - Latest mode returns all posts
def test_latest_feed_returns_all_posts(client):
    response = client.get("/feed?mode=latest")

    assert response.status_code == 200

    posts = response.json()["feed"]

    assert len(posts) == 3

# test 2 - Latest mode orders posts newest first
def test_latest_feed_is_newest_first(client):
    response = client.get("/feed?mode=latest")

    assert response.status_code == 200

    posts = response.json()["feed"]

    creators = [post["creator"] for post in posts]

    assert creators == [
        "randomcreator1",
        "randomcreator3",
        "randomcreator2",
    ]

# test 3 - Following only shows creators followed by demo_user
def test_following_feed_excludes_unfollowed_creator(client):
    response = client.get("/feed?mode=following")

    assert response.status_code == 200

    posts = response.json()["feed"]

    creators = [post["creator"] for post in posts]

    assert "randomcreator1" in creators
    assert "randomcreator3" in creators
    assert "randomcreator2" not in creators

# test 4 - unsupported feed modes are rejected
def test_invalid_feed_mode_is_rejected(client):
    response = client.get("/feed?mode=banana")

    assert response.status_code == 422
