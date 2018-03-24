# Flask file

from flask import Flask, render_template 
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello world"


@app.route("/data")
def data():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0")
