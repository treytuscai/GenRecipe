"""This module contains fixtures for testing."""
import pytest
from website import create_app

@pytest.fixture
def app():
    """Fixture to set up a Flask app for testing."""
    app = create_app()
    app.config["OPENAI_API_KEY"] = "test_api_key"
    return app

@pytest.fixture
def client(app):
    """Fixture to provide a test client."""
    return app.test_client()
