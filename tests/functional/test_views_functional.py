"""This module contains functional tests for the views."""

def test_main_route(client):
    """Test the main route and check that a hiding spot is selected."""
    response = client.get('/')
    assert response.status_code == 200

