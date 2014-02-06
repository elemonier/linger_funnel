'''
Created by: Emily Lemonier
Purpose: Outline ORM for User, Contact, InMessage, OutMessage Objects

Too add: relationships
'''

from app import db

class User(db.Model):
	#index? necessary
	user_id = db.Column(db.Integer, primary_key = True)
	user_name = db.Column(db.String(64), index = True)
	user_phone = db.Column(db.String(64), index = True, unique = True)
	user_encrypted_password = db.Column(db.String(64), index = True, unique = True)
	user_salt = db.Column(db.String(64), index = True, unique = True)
	user_email = db.Column(db.String(64), index = True, unique = True)
	user_created_at = db.Column(db.DateTime, index = True)
	user_updated_at = db.Column(db.DateTime, index = True)
	
	def __repr__(self):
		''' Print objects of User class	'''
		return '<User %r>' % (self.user_name)

class Contact(db.Model):

	contact_id = db.Column(db.Integer, primary_key = True)
	contact_user = db.Column(db.String(64))
	contact_name = db.Column(db.String(64))
	contact_phone1 = db.Column(db.Integer)
	contact_phone2 = db.Column(db.Integer)
	contact_email1 = db.Column(db.String(64))
	contact_email2 = db.Column(db.String(64))

	def __repr__(self):
		''' Print objects of Contact class'''
		return '<Contact %r' % (self.contact_name)

class InMessage(db.Model):
	inmessage_id = db.Column(db.Integer, primary_key = True)
	inmessage_user = db.Column(db.String(64))
	inmessage_contact = db.Column(db.String(64))
	inmessage_content = db.Column(db.String(120))
	inmessage_when_received = db.Column(db.DateTime)

	def __repr__(self):
		''' print objects of InMessage class '''
		return '<Message %r>' % inmessage_content

class OutMessage(db.Model):
	outmessage_id = db.Column(db.Integer, primary_key = True)
	outmessage_user = db.Column(db.String(64))
	outmessage_contact = db.Column(db.String(64))
	outmessage_content = db.Column(db.String(120))
	outmessage_when_received = db.Column(db.DateTime)

	def __repr__(self):
		''' print objects of OutMessage class '''
		return '<Message %r>' % outmessage_content


