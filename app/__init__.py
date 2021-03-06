# Call Flask framework
from flask import Flask

# Initialize the application
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# Load the configuration file
app.config.from_object('config')