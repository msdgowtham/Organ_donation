from flask import Flask, request, render_template, url_for, session, redirect, g
import os
from datetime import timedelta

app = Flask(__name__)

@app.route("/index")
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ministries')
def ministries():
    return render_template("ministries.html")

@app.route('/sermons')
def sermons():
    return render_template("sermons.html")

@app.route('/event')
def event():
    return render_template("event.html")

@app.route('/event-details')
def event_details():
    return render_template("event-details.html")

@app.route('/about-us')
def about_us():
    return render_template("about-us.html")

@app.route('/donation')
def donation():
    return render_template("donation.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/blog-single')
def blog_single():
    return render_template("blog-single.html")

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.permanent_session_lifetime = timedelta(minutes=10)
    app.run(debug=True)