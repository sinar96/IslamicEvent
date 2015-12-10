from db import database

class Event(database.Model):
	__tablename__ = 'event'

	id = database.Column(database.Integer, primary_key=True)
	name = database.Column(database.String())
	theme = database.Column(database.String())
	date = database.Column(database.String())
	area = database.Column(database.String())
	location = database.Column(database.String())
	facility = database.Column(database.String())
	htm = database.Column(database.Double())
	how_to_join = database.Column(database.String())
	contact_person = database.Column(database.Integer())
	speaker = database.Column(database.String())

	def __repr__(self):
		return '<Event {}>'.format(self.name)

class Speaker(database.Model):
	__tablename__ = 'speaker'

	id = database.Column(database.Integer, primary_key=True)
	name= database.Column(database.String())
	gender = database.Column(database.String())
	profession = database.Column(database.String())

	def __repr__(self):
		return '<Speaker {}>'.format(self.name)