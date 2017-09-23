from flask import Flask, json
from flask import jsonify

#import requests

app = Flask(__name__)

@app.route("/")
def hello():
	return "Welcome to our app!"
@app.route('/patients/<int:id>')
def summary(id):
	pp = None
	for p in h1.patients:
		if(p.idNumber==str(id)):
			pp = p
	s = jsonify(
		idNumber = pp.idNumber,
		picture = pp.picture,
		name = pp.name,
		status = pp.status
		)
	return s
	#return json.dumps(pp.toJSON())
@app.route('/patients')
def patients():
	sj = json.dumps([e.toJSON() for e in h1.patients])
	response = app.response_class(
		response = sj,
		status = 200,
		mimetype = 'application/json'
		)
	return response
@app.route('/events')
def events():
	sj = json.dumps([e.toJSON() for e in h1.events])
	return sj

#@app.route('/postevent',methods=["POST"])
#def postevent():
#    if resquest.method == "POST":


class Room(object):
	roomNumber = 0
	floor = None
	patients = []
	def __init__(self, number, fl):
		super(Room, self).__init__()
		self.RoomNumber = number
		self.floor = fl
	def add_patient(self,p):
		self.patients.append(p)
	def remove_patient(id):
		for p in patients:
			if(p.idNumber==id):
				patients.remove(p)

class Hospital(object):
	rooms = []
	doctors = []
	nurses = []
	patients = []
	events = []
	def __init__(self,idNumber):
		super (Hospital, self).__init__()
		self.idNumber = idNumber
	def add_room(self, room):
		self.rooms.append(room)
	def add_nurse(self,nurse):
		self.nurses.append(nurse)
	def add_doctor(self,doc):
		self.doctors.append(doc);
	def add_patient(self,p):
		self.patients.append(p)
	def add_event(self,e):
		self.events.append(e)

class Patient(object):
	needs = []
	def __init__(self, idNumber, age, picture, name, status):
		super (Patient,self).__init__()
		self.idNumber = idNumber
		self.picture = picture
		self.name = name
		self.status = status
		self.age = age
	def addEvent(self, e):
		self.events.append(e)
	def toJSON(self):
		return {'idNumber': self.idNumber,'age':self.age,'picture': self.picture,'name': self.name, 'status': self.status}

class Employee(object):
	#events = []
	def __init__(self,idNumber):
		super (Employee,self).__init__()
		self.idNumber = idNumber
	#def add_event(self, e):
	#	self.events.append(e)

class Doctor(Employee):
	patients = []
	def __init__(self, idNumber):
		super(Doctor, self).__init__(idNumber)
	def add_patient(self, p):
		self.patients.append(p)

class Nurse(Employee):
	patients = []
	def __init__(self, idNumber):
		super(Nurse,self).__init__(idNumber)
	def add_patient(self,p):
		self.patients.append(p)

class Event(object):
	def __init__(self, eventId, title, room, time, message, nurseId, patientId):
		super(Event,self).__init__()
		self.eventId = eventId
		self.title = title
		self.room = room
		self.time = time
		self.message = message
		self.nurseId = nurseId
		self.patientId = patientId
	def toJSON(self):
		return {'eventId': self.eventId,'title': self.title,'room': self.room,'time': self.time, 'message': self.message, 'nurseId': self.nurseId, 'patientId': self.patientId}

h1 = Hospital("1");
n1 = Nurse("1")
n2 = Nurse("2")
d1 = Doctor("1")
d2 = Doctor("2")
p1 = Patient("1","30","https://cdn.fstoppers.com/styles/full/s3/lead/2016/04/portrait_rules_correct.jpg","Ann","1")
p2 = Patient("2","48","https://1.bp.blogspot.com/-9QM7ciGXRkQ/V1hsB-wNLBI/AAAAAAAAMoA/eYbSHs00PTAjrI4QAmvYAIGCUe1AuRAnwCLcB/s1600/bryan_cranston_0095.jpg","Ben","2")
e1 = Event("1","Medicine","102","08:30:00","Give five","1","1")
e2 = Event("2","Drug","101","09:30:00","One","2","2")
h1.add_event(e1)
h1.add_event(e2)
h1.add_nurse(n1)
h1.add_nurse(n2)
h1.add_patient(p1)
h1.add_patient(p2)
n1.add_patient(p1)
n2.add_patient(p2)