from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
	"""Verifies the health endpoint reture 200 OK and healthy status"""
	response = client.get("/health")
	assert response.status_code == 200
	assert response.json() == {"status": "healthy"}

def test_read_root():
	"""Verifies the root endpoint is accessible."""
	response = client.get("/")
	assert response.status_code == 200

def test_api_is_running():
	"""A simple assertion to ensure the test suite is active"""
	assert True
