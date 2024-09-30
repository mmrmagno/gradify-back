import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine, get_db
from app.models import Base
from app.keycloak import get_token

# Setup the database
@pytest.fixture(scope="module")
def test_client():
    Base.metadata.create_all(bind=engine)
    client = TestClient(app)
    yield client
    Base.metadata.drop_all(bind=engine)

# Mock Keycloak authentication
@pytest.fixture
def access_token():
    # Replace these with valid test credentials for Keycloak
    username = "testuser"
    password = "password"
    
    token_response = get_token(username, password)  # Make sure this is a valid function to get tokens
    return token_response['access_token']

def test_create_user(test_client, access_token):
    response = test_client.post(
        "/users/",
        json={"name": "John Doe", "email": "john@example.com", "role": "student"},
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "john@example.com"

def test_get_user(test_client, access_token):
    # Create a user first
    create_response = test_client.post(
        "/users/",
        json={"name": "Jane Doe", "email": "jane@example.com", "role": "student"},
        headers={"Authorization": f"Bearer {access_token}"}
    )
    user_id = create_response.json()["id"]

    # Get the user
    response = test_client.get(f"/users/{user_id}", headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200
    assert response.json()["email"] == "jane@example.com"
