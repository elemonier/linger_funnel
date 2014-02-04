from flask import Flask, jsonify, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# disable this for launch (~~ 'watch')
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@server/db'
db = SQLAlchemy(app)

@app.route("/")
def login():
	return render_template("login.html")

@app.route("/name")
def name():
	return "William G. Falk-Wallace"

@app.route("/search/<search_query>")
def search(search_query):
	return search_query

if __name__ == "__main__":
	app.run(host="0.0.0.0")