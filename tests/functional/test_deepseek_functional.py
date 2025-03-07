"""This module contains functional tests for the deepseek ai."""
from unittest import mock
from flask import json

def test_provide_recipe_success(client, app):
    """Test the /recipe endpoint for successful response."""
    with app.app_context():
        with mock.patch('website.deepseek.generate_response') as mock_generate_response:
            mock_generate_response.return_value = ("Here is a recipe", None)

            # Send POST request to /recipe
            response = client.post('/recipe', json={"ingredients": "cheese, chicken, eggs, milk"})

            assert response.status_code == 200
            response_json = json.loads(response.data)
            assert response_json["success"] is True
            assert "recipe" in response_json
            assert response_json["recipe"] == "Here is a recipe"

def test_provide_recipe_error(client, app):
    """Test the /recipe endpoint when there is an error generating it."""
    with app.app_context():
        with mock.patch('website.deepseek.generate_response') as mock_generate_response:
            mock_generate_response.return_value = (None, "An unexpected error occurred.")

            # Send POST request to /recipe with missing ingredients
            response = client.post('/recipe', json={})  # Empty body to simulate missing ingredients

            assert response.status_code == 400  # Expecting 400 for missing ingredients
            response_json = json.loads(response.data)
            assert response_json["success"] is False
            assert response_json["error"] == "No ingredients provided"

            response = client.post('/recipe', json={"ingredients": "cheese, chicken, eggs"})
            assert response.status_code == 500  # Expecting 500 due to generation error
            response_json = json.loads(response.data)
            assert response_json["success"] is False
            assert response_json["error"] == "An unexpected error occurred."
