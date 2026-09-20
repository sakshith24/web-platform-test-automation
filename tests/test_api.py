import pytest
from utils.api_client import APIClient

BASE_API_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def api_client():
    """
    Pytest fixture that provides an instance of APIClient.
    The 'module' scope means it will be created once per test module.
    """
    return APIClient(BASE_API_URL)

def test_get_post(api_client):
    """
    Test to verify fetching a single post using GET.
    """
    print("\nRunning test_get_post...")
    response = api_client.get('/posts/1')

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers["Content-Type"].startswith("application/json"), \
        f"Expected JSON content type, but got {response.headers['Content-Type']}"

    data = response.json()
    assert isinstance(data, dict), "Response is not a dictionary"
    assert "userId" in data, "Field 'userId' not found in response"
    assert "id" in data, "Field 'id' not found in response"
    assert "title" in data, "Field 'title' not found in response"
    assert "body" in data, "Field 'body' not found in response"
    print("test_get_post PASSED.")


def test_create_post(api_client):
    """
    Test to verify creating a new post using POST.
    """
    print("\nRunning test_create_post...")
    payload = {
        "title": "Test Post",
        "body": "Created by pytest automation",
        "userId": 1
    }
    response = api_client.post('/posts', json=payload)

    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    assert response.headers["Content-Type"].startswith("application/json"), \
        f"Expected JSON content type, but got {response.headers['Content-Type']}"

    data = response.json()
    assert isinstance(data, dict), "Response is not a dictionary"
    assert "id" in data, "Field 'id' not found in response"
    assert data.get("title") == payload["title"], "Returned title does not match payload title"
    assert data.get("body") == payload["body"], "Returned body does not match payload body"
    assert data.get("userId") == payload["userId"], "Returned userId does not match payload userId"
    print("test_create_post PASSED.")


def test_update_post(api_client):
    """
    Test to verify updating an existing post using PUT.
    """
    print("\nRunning test_update_post...")
    payload = {
        "id": 1, # JSONPlaceholder often echoes the ID back
        "title": "Updated Test Post",
        "body": "Updated using pytest",
        "userId": 1
    }
    response = api_client.put('/posts/1', json=payload)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers["Content-Type"].startswith("application/json"), \
        f"Expected JSON content type, but got {response.headers['Content-Type']}"

    data = response.json()
    assert isinstance(data, dict), "Response is not a dictionary"
    assert data.get("id") == payload["id"], "Returned ID does not match payload ID"
    assert data.get("title") == payload["title"], "Returned title does not match updated title"
    assert data.get("body") == payload["body"], "Returned body does not match updated body"
    assert data.get("userId") == payload["userId"], "Returned userId does not match updated userId"
    print("test_update_post PASSED.")


def test_delete_post(api_client):
    """
    Test to verify deleting a post using DELETE.
    """
    print("\nRunning test_delete_post...")
    response = api_client.delete('/posts/1')

    # JSONPlaceholder returns 200 OK for a successful DELETE
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    # JSONPlaceholder returns an empty dictionary for delete, so no further content assertion needed.
    assert response.json() == {}, "Expected empty JSON response for DELETE"
    print("test_delete_post PASSED.")


def test_get_invalid_post(api_client):
    """
    Negative test to verify handling of a non-existent post ID.
    """
    print("\nRunning test_get_invalid_post...")
    response = api_client.get('/posts/999999')

    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
    assert response.json() == {}, "Expected empty JSON response for 404"
    print("test_get_invalid_post PASSED.")
