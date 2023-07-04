from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home_default():
    return render_template("index.html")

@app.route("/index.html")
def my_home():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/works.html")
def works_page():
    return render_template("works.html")

@app.route("/contact.html")
def contact_page():
    return render_template("contact.html")