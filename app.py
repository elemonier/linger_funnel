from flask import Flask, jsonify, render_template, request, session, redirect, flash, config
import requests
from configuration import API_USER, API_KEY

app = Flask(__name__)
app.debug = True

@app.route("/index", methods=["GET", "POST"])
def signup():
	if request.method == "POST":
		url = "https://api.sendgrid.com/api/mail.send.json"
		msg = {}

		msg['api_user'] = API_USER
		msg['api_key'] = API_KEY
		msg['to'] = "lingerio@googlegroups.com" 
		msg['subject'] = "LINGER CONTACT"	
		msg['text'] = "name: " + request.form['name'] + \
					"\nphone: " + request.form['phone'] + \
					"\nemail: " + request.form['email'] + \
					"\ncomments: " + request.form['comments']

		msg['from'] = "lingerio@googlegroups.com"
		print 'msg: ', msg
		response = requests.post(url, msg)	#error template

		print 'SIGNUP EMAIL SENT'
		return redirect("/")
	else:
		return redirect("/")




@app.route("/")
def home():
	return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def mail():
	if request.method == "GET":
		print 'GET SIGNUP'
	if request.method == "POST":

		url = "https://api.sendgrid.com/api/mail.send.json"
		msg = {}

		msg['api_user'] = API_USER
		msg['api_key'] = API_KEY
		msg['to'] = "lingerio@googlegroups.com" 
		msg['subject'] = "LINGER CONTACT"	
		msg['text'] = "name: " + request.form['name'] + \
					"\nphone: " + request.form['phone'] + \
					"\nemail: " + request.form['email'] + \
					"\ncomments: " + request.form['comments']

		msg['from'] = "lingerio@googlegroups.com"
		response = requests.post(url, msg)	#error template
		return redirect("/")
	else:
		return redirect("/")


@app.route("/signup-submit", methods=["GET", "POST"])
def signup_submit():
	#request_form...
	if request.method == "POST":
		print 'signupsubmit-post'
		# add method to get elements from post and push to db.
		# js alert? homepage?
		#check equal passwords
		if request.form['signup-pass1'] == request.form['signup-pass1']:
			new_user = models.User(
					request.form['signup-name'], 
					request.form['signup-email'], 
					request.form['signup-phone'],
					request.form['signup-pass1'])
			print new_user
			models.db.session.add(new_user)
			models.db.session.commit()
			return render_template("login.html", alert_title="Success: ", error="you've registered your account!")
		else:
			#TO DO: print 'password incorrect?'
			return render_template("signup.html")
	else: # request.method == "GET"
		print 'signupsubmit-post'
		return render_template("signup.html")


@app.errorhandler(404)
def page_not_found(error):
	return render_template("404.html"), 404


if __name__ == "__main__":
	app.run(host="0.0.0.0")


