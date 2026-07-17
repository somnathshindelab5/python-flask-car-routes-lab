from flask import Flask

# Initialize the Flask application for the car routes lab.
app = Flask(__name__)

# Available car models for the catalog lookup route.
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def home():
    """Return the landing page message for the Flatiron Cars app."""
    return 'Welcome to Flatiron Cars'


@app.route('/<model>')
def model_info(model):
    """Return whether a requested model exists in the catalog."""
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'

    return f'No models called {model} exists in our catalog'


__all__ = ['app', 'existing_models', 'home', 'model_info']
