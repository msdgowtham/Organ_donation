from flask import Flask, request, render_template, url_for, session, redirect, g
import os
from datetime import timedelta

app = Flask(__name__)

@app.route("/index")
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/awareness')
def awareness():
    return render_template("awareness.html")

@app.route('/aboutonelife')
def aboutonelife():
    return render_template("aboutonelife.html")

@app.route('/event')
def event():
    return render_template("event.html")

@app.route('/event-details')
def event_details():
    return render_template("event-details.html")

@app.route('/about-us')
def about_us():
    return render_template("about-us.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/elements')
def elements():
    return render_template("elements.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.permanent_session_lifetime = timedelta(minutes=10)
    app.run(debug=True)