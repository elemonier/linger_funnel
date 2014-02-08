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
	
	#attributes w/ relationships
	user_inmessages = db.relationship('InMessage', backref='user', lazy='dynamic')
	user_outmessages = db.relationship('OutMessage', backref='user', lazy='dynamic')
	user_contacts = db.relationship('Contact', backref='user', lazy='dynamic')

	#attributes
	user_id = db.Column(db.Integer, primary_key = True, unique = True) 				#sequentially generated user id
	user_name = db.Column(db.String(64), index = True)								#user's physical name
	user_phone = db.Column(db.String(64), index = True, unique = True)				#user's phone number
	user_email = db.Column(db.String(64), index = True, unique = True)				#user's email

	user_encrypted_password = db.Column(db.String(64), index = True, unique = True)
	user_salt = db.Column(db.String(64), index = True, unique = True)
	
	user_created_at = db.Column(db.DateTime, index = True)							#date/time user registered
	user_updated_at = db.Column(db.DateTime, index = True)							#date/time last updated contacts
	

	def __init__(self, name, email, phone, password):
		''' User constructor '''
		
		self.user_name = name
		self.user_phone = phone	
		self.user_email = email

		self.user_encrypted_password = password #no encryption
		self.user_salt = password 				#no encryption

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
# def is_authenticated(self):
 #        return True
 #    def is_active(self):
 #        return True
 #    def is_anonymous(self):
 #        return False
 #    def get_id(self):
 #        return unicode(self.user_id)


class Contact(db.Model):
	''' Contact class '''
	__tablename__ = 'contacts'
	
	#attributes w/ relationship
	contact_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))	#user relationship

	#attributes
	contact_id = db.Column(db.Integer, primary_key = True)	#sequentially generated user id by db
	#contact_phone_id = db.Column(db.Integer, unique = True)	#android phone's uniquely generated id assoc. w/ contact
	contact_name = db.Column(db.String(64))					
	contact_phone1 = db.Column(db.String(64), unique = True)				
	contact_email1 = db.Column(db.String(64), unique = True)				


	def __init__(self, name, phone_id, phone1, email1): #implement kwargs for phone1, 2, or default to None?
		''' Contact constructor '''
		#selc.contact_phone_id = phone_id
		self.contact_name = name
		self.contact_phone1 = phone1
		self.contact_email1 = email1

	def __repr__(self):
		''' Print objects of Contact class'''
		return "<Contact name= '%s', user_id= '%s' "% (self.contact_name, self.contact_user)

#contact name....AAHAHAYSGWVWk
class InMessage(db.Model):
	''' InMessage Class '''

	__tablename__ = 'in_messages'
	
	#attributes w/ relationship
	inmessage_user = db.Column(db.Integer, db.ForeignKey('users.user_id')) 	#user id assoc. w/ message
	#inmessage_contact_id = db.Column(db.Integer, db.ForeignKey('contact.contact_phone_id')) #contact phone_id assoc. w/ message
	
	#attribute
	inmessage_id = db.Column(db.Integer, primary_key = True)	#sequentially generated user id by db
	inmessage_contact_phone = db.Column(db.String(64))				#same as a contact phone_number
	inmessage_when_received = db.Column(db.DateTime) 			#I'm getting a long.
	inmessage_content = db.Column(db.String(400)) 				#make dynamic??
	inmessage_thread_id = db.Column(db.Integer)					#number associated w/ convo btwn user, contact

	def __init__(self, content, contact_phone, thead, when_received): #contact, user ide?
		''' InMessage Constructor '''
		self.outmessage_contact_phone = contact_phone
		self.inmessage_when_received = when_received #may need to parse into datetime object
		self.inmessage_content = content
		self.inmessage_thread_id = thread

	def __repr__(self):
		''' print objects of InMessage class '''
		return "<Message: from='%s', content= '%s'>" % 'contact name?', inmessage_content

class OutMessage(db.Model):
	''' OutMessage Class '''
	
	__tablename__ = 'out_messages'
	
	#attributes w/ relationship
	outmessage_user = db.Column(db.Integer, db.ForeignKey('users.user_id')) #relationship w/ usr
	#outmessage_contact_phone_id = db.Column(db.Integer, db.ForeignKey('contact.contact_phone_id'))
	
	#attribute
	outmessage_id = db.Column(db.Integer, primary_key = True)
	outmessage_contact_phone = db.Column(db.String(64))	
	outmessage_when_sent = db.Column(db.DateTime) #fucked up. should be sent
	outmessage_content = db.Column(db.String(400))
	outmessage_thread_id = db.Column(db.Integer)

	def __init__(self, contact_phone, content, thread, when_sent): #contact, user ide?
		''' OutMessage Constructor '''
		self.outmessage_contact_phone = contact_phone
		self.outmessage_when_sent = when_sent
		self.outmessage_content = content
		self.outmessage_thread_id = thread


	def __repr__(self):
		''' print objects of OutMessage class '''
		return "<OutMessage: from='%s', content= '%s'>" % 'contact name?', outmessage_content
