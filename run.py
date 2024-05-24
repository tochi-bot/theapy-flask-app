import os  # Import the os module for interacting with the operating system
from flask import Flask, render_template  # Import Flask class and render_template function from the flask module

app = Flask(__name__)  # Create an instance of the Flask class for our web application

# Define the route for the root URL ("/")
@app.route("/")
def index():
    # Render and return the 'index.html' template when the root URL is accessed
    return render_template("index.html")

# Define the route for the "/about" URL
@app.route("/about")
def about():
    # Render and return the 'about.html' template when the "/about" URL is accessed
    return render_template("about.html")

# Define the route for the "/contact" URL
@app.route("/contact")
def contact():
    # Render and return the 'contact.html' template when the "/contact" URL is accessed
    return render_template("contact.html")

# Define the route for the "/careers" URL
@app.route("/careers")
def careers():
    # Render and return the 'careers.html' template when the "/careers" URL is accessed
    return render_template("careers.html")

# Check if the script is executed directly (i.e., not imported as a module)
if __name__ == "__main__":
    # Run the Flask application with the host and port specified in the environment variables,
    # or default to '0.0.0.0' for host and '5000' for port if not specified
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True  # Enable debug mode for detailed error pages and auto-reloading
    )
