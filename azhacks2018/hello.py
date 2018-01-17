from flask import Flask, render_template, flash, redirect, url_for, logging, request
from flask_mysqldb import MySQL 
from wtforms import Form, IntegerField, StringField, TextField, RadioField, validators, TextAreaField

app = Flask(__name__)

# Config mySQL
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "myflaskapp"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def hello():
	return render_template("home.html")

class CallRecord(Form):
	ptn = IntegerField("Phone Number", [validators.Length(min = 3, max = 20)])
	provideName = RadioField("Did they provide their name?", choices = [("0", "Yes"), ("1", "No"), ("2", "N/A")])
	onlyCall = RadioField("Is this the only call regarding the incident?", choices = [("0", "Yes"), ("1", "No"), ("2", "N/A")])
	additionalInfo = RadioField("Is the caller able to give you additional details(phone number, current location, accurate street names, etc...)", choices = [("0", "Yes"), ("1", "No"), ("2", "N/A")])
	voicemask = RadioField("Is the caller's voice masked/computerized in any way? (i.e. not a relay service)", choices = [("0", "Yes"), ("1", "No"), ("2", "N/A")])
	otherData = TextAreaField("Other information")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/callForm", methods = ["GET", "POST"])
def callForm():
	form = CallRecord(request.form)
	if request.method == "POST":

		ptn = form.ptn.data
		provideName = form.provideName.data 
		onlyCall = form.onlyCall.data
		additionalInfo = form.additionalInfo.data
		voicemask = form.voicemask.data 
		otherData = form.otherData.data

		cur = mysql.connection.cursor()
		cur.execute()
		return render_template("callForm.html", form = form)


	return render_template("callForm.html", form = form)


if __name__ == "__main__":
	app.run(debug = True)

