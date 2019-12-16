"""
Minimal Flask App
"""

from flask import flask

# Make the application
app = Flask(__name__)

# Make the route
@app.route("/")

# Now define a function
def hello:
    return "Hello World!"
