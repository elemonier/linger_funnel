from flask import Flask, jsonify, render_template, request, session
from flask.ext.sqlalchemy import SQLAlchemy
import requests, os, json, datetime
import models
from sqlalchemy import create_engine
from flask.ext.login import LoginManager

app = Flask(__name__)
app.debug = True

#app.config['SQLALCHEMY_ECHO'] = True
app.config.from_object('config.flask_config')
db = SQLAlchemy(app)

#login manager
login_manager = LoginManager()
login_manager.init_app(app)


#reload user object from the user ID stored in session
@login_manager.user_loader 
def load_user(userid):
    return models.User.get(int(userid))

@app.route("/")
def home():
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


# route("/app/register", post)
# request.JSONPARSINGLIBHERE
# build contact/message info json into object, see if it's in db. add if not

# route("/app/update")
# here too as above

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		#find user by phone in db, confirm hash matches
		currrent_user = models.User.query.filter_by(user_phone = request.form['username'])
		#confirm hash matches

		#in tbwa server/blue/admin.py
		session

	if form.validate_on_submit():
		#login + validate user
		if not sha256_crypt.verify(password, db_admin['password']):
			flash("Incorrect password")
			return render_template("signup.html")
		return redirect(request.args.get("next") or url_for("index"))
	return render_template("login.html", form=form)
	#successful login -> /user/<uder_id>
#req.form[username]
#post new row (if unique) to db

@app.route("/app/contacts/<user_phone_number>")
def update_contacts(user_phone_number):
	''' updates contacts for user associated w/ user_phone 
		1. deletes existing contacts assoc. w/ user_phone (unique)
		2. adds all contacts from post to db
		3. adds all contacts from post to current user's contact list
		3. updates current user's user_updated_at (datetime obj.) to now 
	'''

	contact_list = request.get_json(force = True) #list of contacts posted; Assumption: list of dictionaries.
	current_user = models.User.query.filter_by(user_phone = user_phone_number).first()
	
	#delete all contacts associated w/ user_id
	models.Contacts.query.filter_by(contact_user = username_entry.user_id).delete()
	#sets user_updated_at (ie updated time) to now
	current_user.user_updated_at = datetime.datetime.now()

	#add all new contacts to db + associate w/ user + commit
	for contact in contact_list:
		new_contact = models.Contact(
			contact['name'], #get out -'s'
			contact['phone'],
			contact['email']
			)
		db.session.add(new_contact)
		current_user.user_contacts.append(new_contact)

	db.session.commit()
	return render_template("login.html") #DUMMY RETURN

#sender_name = my phone number
#form of the timestamp.  
#
@app.route("/app/inmessages/<user_phone_number>")
def update_inmessages(user_phone_number):
	''' updates contacts for user associated w/ user_phone 
		1. Grabs last time user updated
		2. adds all messages from *now* to last time user updated

	'''

	message_list = request.get_json(force = True) #list of contacts posted; Assumption: list of dictionaries.
	current_user = models.User.query.filter_by(user_phone = user_phone_number).first()
	last_updated = current_user.user_updated_at
	time_delta = datetime.datetime.now() + datetime.timedelta(days=5)

	#add all new messages to db + associate w/ user + commit
	for message in message_list:
		#contact_phone, content, thread, when_sent
		#if datetime - message['when_sent'] < 5 days, add new_message
		if time_delta > message['when_sent']:
		#contact_phone, content, thread, when_sent
		#if datetime - message['when_receive'] < 5 days, add new_message
			new_message = models.InMessage(
				message['phone'],
				message['content'],
				message['thread_id'],
				message['when_receive']
				)
			db.session.add(new_message)
			current_user.user_inmessages.append(new_message)

	db.session.commit()
	#return render_template("login.html") #DUMMY RETURN; get return to app browser

@app.route("/app/outmessages/<user_phone_number>")
def update_outmessages(user_phone_number):
	''' updates contacts for user associated w/ user_phone 
		1. Grabs last time user updated
		2. adds all messages from *now* to last time user updated

	'''

	message_list = request.get_json(force = True) #list of contacts posted; Assumption: list of dictionaries.
	current_user = models.User.query.filter_by(user_phone = user_phone_number).first()
	last_updated = current_user.user_updated_at

	time_delta = datetime.datetime.now() + datetime.timedelta(days=5)

	#add all new messages to db + associate w/ user + commit
	for message in message_list:
		#contact_phone, content, thread, when_sent
		#if datetime - message['when_sent'] < 5 days, add new_message
		if time_delta > message['when_sent']:
			new_message = models.OutMessage(
				message['phone'],
				message['content'],
				message['thread_id'],
				message['when_sent']
				)
			print new_message
			db.session.add(new_message)
			current_user.user_outmessages.append(new_message)
	db.session.commit()
	#mreturn render_template("login.html") #DUMMY RETURN


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
			db.session.add(new_user)
			db.session.commit()
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

# @app.route("/login", methods=["GET", "POST"])
# def login():
# 	if request.method == "POST":
# 		print 'signupsubmit-post'
# 		# add method to get elements from post and push to db.
# 		# js alert? homepage?
# 		#check equal passwords
# 		if request.form['signup-pass1'] == request.form['signup-pass1']:
# 			new_user = models.User(
# 					request.form['signup-name'], 
# 					request.form['signup-email'], 
# 					request.form['signup-phone'],
# 					request.form['signup-pass1'])
# 			print new_user
# 			db.session.add(new_user)
# 			db.session.commit()
# 			return render_template("signupsuccess.html", signup_email=request.form["register_email"])
# 		else:
# 			#TO DO: print 'password incorrect?'
# 			return render_template("signup.html")
# 	else: # request.method == "GET"
# 		print 'signupsubmit-post'
# 		return render_template("signup.html")

#goal: add username entry from blah.
@app.route('/user/<user_phone>')
def show_user_profile(user_phone):
	''' Show user profile of username, contacts, messages '''
	#query db for user info
	user_instance = models.User.query.filter_by(user_phone=user_phone).first()
	#if user doesn't exist, route to signup page
	if user_instance is None:
		return render_template("login.html", user_phone=user_phone, error="Phone number entered was invalid")

	#only displaying if user exists...
	#print 'user_instance', user_instance.user_id
	contact_list = user_instance.user_contacts.all() 
	inmessages_list = user_instance.user_inmessages.all()
	outmessages_list = user_instance.user_outmessages.all()

	# print 'USERNAME INSTANCE: ', user_instance
	# print 'CONTACT: ', contact_dict
	# print 'MESSAGES: ', inmessages_dict, outmessages_dict
	
	#render template w/ contacts, messages in dictionary form
	return render_template("dashboard.html", 
		username= user_phone, 
		contacts = contact_list, 
		inmessages = inmessages_list,
		outmessages = outmessages_list)

#twilio tests
#@app.route("/user/<username_entry>/contact/compose_message") #compose message


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
	app.run(host="0.0.0.0")


