'''
Created by: Emily Lemonier
Purpose: Outline ORM for User, Contact, InMessage, OutMessage Objects

Too add: relationships
'''

from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import datetime as dt

class User(db.Model):
	#index? necessaryd
	user_id = db.Column(db.Integer, primary_key = True)
	user_name = db.Column(db.String(64), index = True)
	user_phone = db.Column(db.String(64), index = True, unique = True)
	user_encrypted_password = db.Column(db.String(64), index = True, unique = True)
	user_salt = db.Column(db.String(64), index = True, unique = True)
	user_email = db.Column(db.String(64), index = True, unique = True)
	user_created_at = db.Column(db.DateTime, index = True)
	user_updated_at = db.Column(db.DateTime, index = True)
	user_contacts = relationship('Contact')
	
	def __repr__(self):
		''' Print objects of User class	'''
		return "<User(name='%s', phone='%s', email='%s')>" % (
			self.user_name, self.user_phone, self.user_email)

	def __init__(self, name, email, phone, password):
		#self.user_id = 
	    self.user_name = name
	    self.user_email = email
	    self.phone = phone
	    self.encrypted_password = password #encrypted? how
	    #self.contacts = []
	    self.user_created_at = dt.datetime
	    self.user_updated_at = dt.datetime

class Contact(db.Model):

	contact_id = db.Column(db.Integer, primary_key = True)
	#root user?
	contact_user = db.Column(Integer, ForeignKey('user.user_id')) #chose user_id. guarenteed unique
	contact_name = db.Column(db.String(64))
	contact_phone1 = db.Column(db.Integer)
	contact_phone2 = db.Column(db.Integer)
	contact_email1 = db.Column(db.String(64))
	contact_email2 = db.Column(db.String(64))
	#user_id = db.Column(Integer, ForeignKey('user.user_id'))

	def __repr__(self):
		''' Print objects of Contact class'''
		return '<Contact %r' % (self.contact_name)
	def __init__(self, name, phone1): #implement kwargs
		#self.contact_user = 
		self.contact_name = name
		self.phone1 = phone1

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


