"""
Unit tests for Flask Application
"""

import pytest
import json
import sys
import os

# CRITICAL: Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the app
from app.app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHomeEndpoint:
    """Tests for the home endpoint"""
    
    def test_home_returns_200(self, client):
        """Test that home endpoint returns 200 OK"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_home_returns_json(self, client):
        """Test that home endpoint returns JSON"""
        response = client.get('/')
        assert response.content_type == 'application/json'
    
    def test_home_contains_message(self, client):
        """Test that home endpoint contains welcome message"""
        response = client.get('/')
        data = json.loads(response.data)
        assert 'message' in data
        assert 'Hello from GitHub Actions' in data['message']


class TestHealthEndpoint:
    """Tests for the health check endpoint"""
    
    def test_health_returns_200(self, client):
        """Test that health endpoint returns 200 OK"""
        response = client.get('/health')
        assert response.status_code == 200
    
    def test_health_status_healthy(self, client):
        """Test that health endpoint reports healthy status"""
        response = client.get('/health')
        data = json.loads(response.data)
        assert data['status'] == 'healthy'


class TestReadyEndpoint:
    """Tests for the readiness probe endpoint"""
    
    def test_ready_returns_200(self, client):
        """Test that ready endpoint returns 200 OK"""
        response = client.get('/ready')
        assert response.status_code == 200
    
    def test_ready_status_ready(self, client):
        """Test that ready endpoint reports ready status"""
        response = client.get('/ready')
        data = json.loads(response.data)
        assert data['status'] == 'ready'


class TestInfoEndpoint:
    """Tests for the info endpoint"""
    
    def test_info_returns_200(self, client):
        """Test that info endpoint returns 200 OK"""
        response = client.get('/api/info')
        assert response.status_code == 200
    
    def test_info_contains_features(self, client):
        """Test that info endpoint contains features list"""
        response = client.get('/api/info')
        data = json.loads(response.data)
        assert 'features' in data
        assert isinstance(data['features'], list)


class TestEchoEndpoint:
    """Tests for the echo endpoint"""
    
    def test_echo_returns_200(self, client):
        """Test that echo endpoint returns 200 OK"""
        test_data = {"message": "Hello"}
        response = client.post(
            '/api/echo',
            data=json.dumps(test_data),
            content_type='application/json'
        )
        assert response.status_code == 200
    
    def test_echo_returns_posted_data(self, client):
        """Test that echo endpoint returns the posted data"""
        test_data = {"message": "Test message"}
        response = client.post(
            '/api/echo',
            data=json.dumps(test_data),
            content_type='application/json'
        )
        data = json.loads(response.data)
        assert 'received' in data
        assert data['received'] == test_data


class TestErrorHandling:
    """Tests for error handling"""
    
    def test_404_not_found(self, client):
        """Test that non-existent endpoints return 404"""
        response = client.get('/nonexistent')
        assert response.status_code == 404
    
    def test_404_returns_json(self, client):
        """Test that 404 error returns JSON"""
        response = client.get('/nonexistent')
        assert response.content_type == 'application/json'
