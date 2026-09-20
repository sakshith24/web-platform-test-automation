from utils.api_client import APIClient
import json

BASE_API_URL = "https://jsonplaceholder.typicode.com"
api_client = APIClient(BASE_API_URL)

print("--- Testing APIClient ---")

# --- GET Request ---
print("\n1. Testing GET /posts/1")
get_response = api_client.get('/posts/1')
print(f"Status Code: {get_response.status_code}")
if get_response.status_code == 200:
    print(f"Response JSON: {json.dumps(get_response.json(), indent=2)}")
    assert 'id' in get_response.json()
    assert 'title' in get_response.json()
    print("GET test passed: Status 200 and expected fields found.")
else:
    print("GET test FAILED.")

# --- POST Request ---
print("\n2. Testing POST /posts")
post_payload = {
    "title": "Test Post",
    "body": "Created by automation test",
    "userId": 1
}
post_response = api_client.post('/posts', json=post_payload)
print(f"Status Code: {post_response.status_code}")
if post_response.status_code == 201:
    response_json = post_response.json()
    print(f"Response JSON: {json.dumps(response_json, indent=2)}")
    assert 'id' in response_json
    assert response_json.get('title') == "Test Post"
    print("POST test passed: Status 201 and expected fields found.")
else:
    print("POST test FAILED.")

# --- PUT Request ---
print("\n3. Testing PUT /posts/1")
put_payload = {
    "id": 1,
    "title": "Updated Test Post",
    "body": "This post was updated by automation",
    "userId": 1
}
put_response = api_client.put('/posts/1', json=put_payload)
print(f"Status Code: {put_response.status_code}")
if put_response.status_code == 200:
    response_json = put_response.json()
    print(f"Response JSON: {json.dumps(response_json, indent=2)}")
    assert response_json.get('title') == "Updated Test Post"
    print("PUT test passed: Status 200 and title updated.")
else:
    print("PUT test FAILED.")

# --- DELETE Request ---
print("\n4. Testing DELETE /posts/1")
delete_response = api_client.delete('/posts/1')
print(f"Status Code: {delete_response.status_code}")
if delete_response.status_code == 200:
    print("DELETE test passed: Status 200.")
else:
    print("DELETE test FAILED.")

print("\n--- APIClient manual test complete ---")
