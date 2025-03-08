"""This module contains endpoints for the deepseek calls."""
from flask import Blueprint, request, jsonify, current_app
from openai import OpenAI

deepseek_bp = Blueprint('deepseek_bp', __name__)

def get_openai_client():
    """Retrieves OpenAI client using the API key from Flask config."""
    api_key = current_app.config.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Missing OpenAI API Key")
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    return client

def generate_response(system_prompt, user_prompt):
    """Helper function to generate AI responses using DeepSeek Chat API."""
    try:
        client = get_openai_client()
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content, None
    except Exception as error:  # noqa: W0718 (Still catching general exceptions)
        current_app.logger.error("Unexpected AI Model Error: %s", str(error))
        return None, "An unexpected error occurred."

@deepseek_bp.route('/recipe', methods=['POST'])
def provide_recipe():
    """Provides an AI-generated recipe based on user-provided ingredients."""

    # Extract ingredients from the request JSON
    data = request.get_json()
    ingredients = data.get("ingredients", "")

    if not ingredients:
        return jsonify({"success": False, "error": "No ingredients provided"}), 400

    system_prompt = (
        "You are a professional chef and recipe creator. Your task is to generate 2"
        "simple, brief recipes based on the given ingredients. "
    )

    user_prompt = f"Quickly create 2 brief recipes with these ingredients: {ingredients}."

    # Generate AI response
    recipe, error = generate_response(system_prompt, user_prompt)

    if error:
        return jsonify({"success": False, "error": error}), 500

    return jsonify({"success": True, "recipe": recipe})
