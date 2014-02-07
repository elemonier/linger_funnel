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
	''' User Class '''
	__tablename__ = 'users'
	#relationships
	user_inmessages = db.relationship('InMessage', backref='user', lazy='dynamic')
	user_outmessages = db.relationship('OutMessage', backref='user', lazy='dynamic')
	user_contacts = db.relationship('Contact', backref='user', lazy='dynamic')

	user_id = db.Column(db.Integer, primary_key = True, unique = True)
	user_name = db.Column(db.String(64), index = True)
	user_phone = db.Column(db.String(64), index = True, unique = True)
	user_encrypted_password = db.Column(db.String(64), index = True, unique = True)
	user_salt = db.Column(db.String(64), index = True, unique = True)
	user_email = db.Column(db.String(64), index = True, unique = True)
	user_created_at = db.Column(db.DateTime, index = True)
	user_updated_at = db.Column(db.DateTime, index = True)
	

	def __init__(self, name, email, phone, password):
		''' User constructor '''
		self.user_name = name
		self.user_email = email
		self.user_phone = phone
		self.user_encrypted_password = password #encrypted? how
		self.user_salt = password

		self.user_created_at = dt.datetime.now()
		self.user_updated_at = dt.datetime.now()

	def __repr__(self):
		''' Print objects of User class	'''
		return "<User(id = '%s', name='%s', phone='%s', email='%s', created='%s')>" % (
			str(self.user_id), 
			self.user_name, 
			self.user_phone, 
			self.user_email, 
			str(self.user_created_at)
			)


class Contact(db.Model):
	''' Contact class '''
	__tablename__ = 'contacts'
	contact_user = db.Column(db.Integer, db.ForeignKey('users.user_id'))	#user relationship

	contact_id = db.Column(db.Integer, primary_key = True)
	contact_name = db.Column(db.String(64))
	contact_phone1 = db.Column(db.String(64))
	contact_phone2 = db.Column(db.String(64))
	contact_email1 = db.Column(db.String(64))
	contact_email2 = db.Column(db.String(64))

	def __init__(self, name, phone1, phone2, email1, email2): #implement kwargs for phone1, 2, or default to None?
		''' Contact constructor '''
		self.contact_name = name
		self.phone1 = phone1
		self.phone2 = phone2
		self.email1 = email1
		self.email2 = email2

	def __repr__(self):
		''' Print objects of Contact class'''
		return "<Contact name= '%s', user_id= '%s' "% (self.contact_name, self.contact_user)

class InMessage(db.Model):
	''' InMessage Class '''
	__tablename__ = 'in_messages'
	inmessage_user = db.Column(db.Integer, db.ForeignKey('users.user_id')) #relationship w/ usr
	#inmessage_contact = db.Column(db.Integer, db.ForeignKey('user.user_id')) #relationship w/ usr
	inmessage_contact = db.Column(db.String(64))
	
	inmessage_id = db.Column(db.Integer, primary_key = True)
	inmessage_content = db.Column(db.String(400)) #make dynamic??
	inmessage_when_received = db.Column(db.DateTime)

	def __init__(self, content, received): #contact, user ide?
		''' InMessage Constructor '''
		self.inmessage_content = content
		self.inmessage_when_received = received

	def __repr__(self):
		''' print objects of InMessage class '''
		return "<Message: from='%s', content= '%s'>" % 'contact name?', inmessage_content

class OutMessage(db.Model):
	''' OutMessage Class '''
	__tablename__ = 'out_messages'
	outmessage_user = db.Column(db.Integer, db.ForeignKey('users.user_id')) #relationship w/ usr
	#inmessage_contact = db.Column(db.Integer, db.ForeignKey('user.user_id')) #relationship w/ usr
	outmessage_contact = db.Column(db.String(64))
	
	outmessage_id = db.Column(db.Integer, primary_key = True)
	outmessage_content = db.Column(db.String(400)) #make dynamic??
	outmessage_when_received = db.Column(db.DateTime)

	def __init__(self, content, received): #contact, user ide?
		''' OutMessage Constructor '''
		self.outmessage_content = content
		self.outmessage_when_received = received

	def __repr__(self):
		''' print objects of OutMessage class '''
		return "<OutMessage: from='%s', content= '%s'>" % 'contact name?', outmessage_content
