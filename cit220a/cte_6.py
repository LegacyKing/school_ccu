'This is a program which contains errors that need to be corrected so that the program will execute.'

__author__ = 'Andrew'
_project_ = 'Session6CTE'

'Enter your comments about what the errors were and how you corrected them'

from pprint import pprint

class Person:
	perCount = 0

	def __init__(self, name, datejoined, address, phonenum, email):
		self.name = name
		self.datejoined = datejoined
		self.address = address
		self.phonenum = phonenum
		self.email = email
		Person.perCount += 1

# All the Print commands are missing parenthesis ()
	def displayPerson(self):
		print("Name: ", self.name, ", Date Joined: ", self.datejoined)
		print("Address: ", self.address)
		print("Phone Number: ", self.phonenum, ", Email: ", self.email)

	def displayCount():
		print("Total number of people %d" % Person.perCount)

per1 = Person("Smith, John", 20020101, "111 First St. Dallas, TX 78989", "555-555-1111", "js@aol.com")
per2 = Person("Jones, Jim", 20021021, "222 Second St. Tulsa, OK 65454", "555-544-1234", "jj@gmail.com")

per1.displayPerson()
per2.displayPerson()

# This makes no sense, only useful in a loop. Make a loop?

print("Total People %d" % Person.perCount)

x = Person.displayCount()

print(x)
