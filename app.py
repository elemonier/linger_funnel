from flask import Flask, jsonify, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)

# disable this for launch (~~ 'watch')
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@server/db'
db = SQLAlchemy(app)

@app.route("/")
def login():
	return render_template("login.html")

# @app.route("/search/<search_query>")
# def search(search_query):
# 	return search_query

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return render_template("dashboard.html", username=username)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404



if __name__ == "__main__":
	app.run(host="0.0.0.0")