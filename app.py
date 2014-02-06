from flask import Flask, jsonify, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import requests
import os
import models

app = Flask(__name__)
app.debug = True

#DATABASE
#app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_ECHO'] = True
#gets models from models.py


#SESSIONS
#Session = sessionmaker(bind=engine)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@server/db'
#config has db uri,e tc. 

db = SQLAlchemy(app)
db.create_all()

@app.route("/")
def login():
	return render_template("login.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
	if request.method == "POST":
		print 'email', 
		return render_template("contact.html", signup_email=request.form["register_email"])
	else: # request.method == "GET"
		print 'not email'
		return render_template("contact.html")

@app.route('/user/<username_entry>')
def show_user_profile(username_entry):
	''' Show user profile of username, contacts, messages '''
    #query db for user, get contacts, messages
    #TEST LINE SESSION: user_instance = session.query(User).filter_by(user_name = username).first() 
	#user_instance = session.query(User).filter_by(user_name = username).first() 
	user_instance = models.User.query.filter_by(user_name= username_entry)
	print 'user_instance', user_instance
	contact_dict = user_instance.contacts.all()
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