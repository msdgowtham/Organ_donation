from flask import Flask, request, render_template, url_for, session, redirect, g
import os
from datetime import timedelta

app = Flask(__name__)

@app.route('/')
def index():
    print("nothing")
    return "Hello World"


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.permanent_session_lifetime = timedelta(minutes=10)
    app.run(debug=True)