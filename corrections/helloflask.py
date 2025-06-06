from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/formation/<name>")
def hello_world_all(name):
    return f"<p>Hello, A tous dans la formation {escape(name)} !</p>"