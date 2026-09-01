
# test 1 - GET returns seeded preference
def test_get_feed_preference(client):
    response = client.get("/feed-preference")

    assert response.status_code == 200
    assert response.json()["default_feed_mode"] == "latest"

# test 2 - PATCH changes preference
def test_patch_feed_preference(client):
    response = client.patch(
        "/feed-preference",
        json={"default_feed_mode":"following"},
        )

    assert response.status_code == 200
    assert response.json()["default_feed_mode"] == "following"

# test 3 - saved preference persists across another API request
def test_persisted_feed_preference(client):
    update_response = client.patch(
        "/feed-preference",
        json={"default_feed_mode":"following"},
        )

    assert update_response.status_code == 200

    get_response = client.get("/feed-preference")

    assert get_response.status_code == 200
    assert get_response.json()["default_feed_mode"] == "following"


# test 4 - unsupported preference is rejected by FastAPI/Pydantic
def test_invalid_feed_preference_is_rejected(client):
    response = client.patch(
        "/feed-preference",
        json={"default_feed_mode": "banana"},
    )

    assert response.status_code == 422

