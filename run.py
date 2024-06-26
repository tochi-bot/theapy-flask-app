import os  # Import the os module for interacting with the operating system
import json  # Import the json module for handling JSON data
from flask import Flask, render_template, request, flash  # Import Flask class and render_template, request functions from the flask module
if os.path.exists("env.py"):
    import env

app = Flask(__name__)  # Create an instance of the Flask class for our web application
app.secret_key=os.environ.get("SECRET_KEY")

# Define the route for the root URL ("/")
@app.route("/")
def index():
    # Render and return the 'index.html' template when the root URL is accessed
    return render_template("index.html")

# Define the route for the "/about" URL
@app.route("/about")
def about():
    data = []
    # Open and read the company.json file, storing its content in the data variable
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    # Render and return the 'about.html' template with page title and company data when the "/about" URL is accessed
    return render_template("about.html", page_title="About", company=data)

# Define the route for the "/contact" URL, accepting both GET and POST methods
@app.route("/contact", methods=["GET", "POST"])
def contact():
    # If the request method is POST, print the form data to the console
    if request.method == "POST":
      flash("Thank You {}, we have received your message".format(request.form.get("name")))
    # Render and return the 'contact.html' template with page title when the "/contact" URL is accessed
    return render_template("contact.html", page_title="Contact")

# Define the route for the "/careers" URL
@app.route("/careers")
def careers():
    # Example job data
    jobs = [
        {"id": 1, "title": "Software Engineer", "description": "Develop and maintain software applications."},
        {"id": 2, "title": "Data Scientist", "description": "Analyze and interpret complex data to help companies make decisions."},
    ]
    # Render and return the 'careers.html' template with page title and job listings when the "/careers" URL is accessed
    return render_template("careers.html", page_title="Careers", jobs=jobs)


# Define the route for job details
@app.route("/job/<int:job_id>")
def job_details(job_id):
    jobs = [
        {"id": 1, "title": "Software Engineer", "description": "Develop and maintain software applications.", "requirements": "Experience with Python and Flask."},
        {"id": 2, "title": "Data Scientist", "description": "Analyze and interpret complex data to help companies make decisions.", "requirements": "Experience with data analysis and machine learning."},
    ]
    job = next((job for job in jobs if job["id"] == job_id), None)
    if job is None:
        flash("Job not found.")
        return redirect(url_for("careers"))
    return render_template("job_details.html", job=job)

# Define the route for submitting job applications
@app.route("/apply", methods=["POST"])
def apply():
    name = request.form.get("name")
    email = request.form.get("email")
    resume = request.files.get("resume")

    # Here you would save the resume file and store the application details in the database
    flash(f"Thank you, {name}. Your application has been submitted.")
    return redirect(url_for("careers"))

# Check if the script is executed directly (i.e., not imported as a module)
if __name__ == "__main__":
    # Run the Flask application with the host and port specified in the environment variables,
    # or default to '0.0.0.0' for host and '5000' for port if not specified
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True  # Enable debug mode for detailed error pages and auto-reloading
    )
