from flask import Flask, jsonify, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import requests
import os
import models
from sqlalchemy import create_engine

app = Flask(__name__)
app.debug = True

#DATABASE
#app.config.from_object('config')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#app.config['SQLALCHEMY_ECHO'] = True
#gets models from models.py

# an Engine, which the Session will use for connection
# resources
my_engine = create_engine('sqlite:////tmp/test.db')

db = SQLAlchemy(app)
db.create_all()

@app.route("/")
def login():
	return render_template("login.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
	if request.method == "POST":
		print 'signup-post'
		return render_template("signup.html", signup_email=request.form["register_email"])
	else: # request.method == "GET"
		print 'signup-get'
		return render_template("signup.html")

@app.route("/signup-submit", methods=["GET", "POST"])
def signupsubmit():
	#request_form...
	if request.method == "POST":
		print 'signupsubmit-post'
		# add method to get elements from post and push to db.
		# js alert? homepage?

		#check password identity. 
		#create user
		# name, email, phone, password)
		#check equal passwords
		if request.form['signup-pass1'] == request.form['signup-pass1']:
			new_session = session_creator()
			new_session._model_changes = {}
			new_user = models.User(
					request.form['signup-name'], 
					request.form['signup-email'], 
					request.form['signup-phone'],
					request.form['signup-pass1'])
			print new_user
			new_session.add(new_user)
			new_session.commit()
			return render_template("signupsuccess.html", signup_email=request.form["register_email"])
		else:
			#TO DO: print 'password incorrect?'
			return render_template("signup.html")
	else: # request.method == "GET"
		print 'signupsubmit-post'
		return render_template("signup.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")


#goal: add username entry from blah.
@app.route('/user/<username_entry>')
def show_user_profile(username_entry):
	''' Show user profile of username, contacts, messages '''
	#query db for user info
	print 'username_entry', username_entry
	user_instance = models.User.query.filter_by(user_name=username_entry).first()
	print 'user_instance', user_instance.user_id
	contact_dict = user_instance.user_contacts.all()
	messages_dict = user_instance.messages.all()
	#render template w/ contacts, messages in dictionary form
	return render_template("dashboard.html", 
		username=username_entry, 
		contacts = contact_dict, 
		messages = messages_dict)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
	app.run(host="0.0.0.0")