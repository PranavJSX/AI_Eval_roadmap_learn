import pytest

@pytest.mark.smoke
def test_get_all_posts(api_client):
    response  = api_client.get("/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

@pytest.mark.smoke
def test_create_post(api_client, sample_post_payload):
    response = api_client.post("/posts", payload=sample_post_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == sample_post_payload["title"]
    assert "id" in data

@pytest.mark.parametrize("post_id", [1,5,15])
def test_get_single_post(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

def test_delete_request(api_client, sample_post_payload):
    response = api_client.delete(f"/posts/{sample_post_payload['id']}")
    assert response.status_code == 200
    