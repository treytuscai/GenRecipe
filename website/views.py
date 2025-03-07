"""This module contains endpoints for the genrecipe app."""
from flask import Blueprint, render_template

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])
def main():
    """Endpoint to get main page."""
    return render_template('index.html')
