"""This module contains endpoints for the deepseek.exe app."""
import os
import random
from flask import Blueprint, render_template, current_app, jsonify

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])
def main():
    """Endpoint to get main page."""
    return render_template('index.html')
