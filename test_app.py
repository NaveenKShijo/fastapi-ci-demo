from fastapi.testclient import TestClient  # FastAPI built its TestClient directly on top of the httpx library
from fast_app import app

client = TestClient(app)

# Each function -> 1 pass

def test_home():
    response = client.get("/home/")
    assert response.status_code == 400
    assert response.json() == {"response": "Welcome here at home"}

def test_home2():
    response = client.get("/home/")
    assert response.status_code == 200
    assert response.json() == {"response": "Welcome here at home"}



