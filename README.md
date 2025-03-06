# GenRecipe

## Project Objective
GenRecipe is an AI-powered recipe generator that helps users discover delicious recipes based on the ingredients they have available. The application integrates with a Large Language Model (LLM) to generate recipe suggestions dynamically. Additionally, this project includes a second AI-powered app of your choice, providing an opportunity to explore creative AI applications.

## Features
- **AI-Powered Recipe Generation**: Users input available ingredients, and the app suggests relevant recipes.
- **LLM Integration**: Connects to DeepSeek to generate recipes dynamically.
- **Responsive UI**: A professional and mobile-friendly design using Bootstrap.
- **CI/CD Pipeline**: Automates linting, testing, and deployment to Heroku.

## Getting Started
- Python 3.x
- Flask
- Heroku account
- API key from an LLM provider

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/treytuscai/GenRecipe.git
   cd GenRecipe
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```sh
   export OPENAI_API_KEY='your_api_key_here'
   ```
4. Run the Flask app:
   ```sh
   flask run
   ```

## Contribution
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit changes and push to GitHub.
4. Open a Pull Request for review.

## License
This project is licensed under the MIT License.

