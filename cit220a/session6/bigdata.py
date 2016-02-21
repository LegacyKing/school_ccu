__author__ = 'Andrew'
_project_ = 'Session6'
# Date: 2016-02-16

class Person:
	perCount = 0

	def __init__(self):
		self._first_name = None
		self._last_name = None
		self._date_of_birth = None
		self._ssn = None
		self._address = None
		self._tithe = None
		self._spiritual_gifts = None
		self._member = None
		self._ministries = None
		self._phone_number = None
		self._start_date = None
		self._end_date = None
		self._left_reason = None
		Person.perCount += 1

	def __repr__(self):
		return self._first_name + ' ' + self._last_name

	@property
	def first_name(self):
		return self._first_name

	@first_name.setter
	def first_name(self, first_name):
		self._first_name = first_name

	@property
	def last_name(self):
		return self._last_name

	@last_name.setter
	def last_name(self, last_name):
		self._lastName = last_name

	@property
	def date_of_birth(self):
		return self._date_of_birth

	@date_of_birth.setter
	def date_of_birth(self, date_of_birth):
		self._date_of_birth = date_of_birth

	@property
	def ssn(self):
		return self._ssn

	@ssn.setter
	def ssn(self, ssn):
		self._ssn = ssn

	@property
	def address(self):
		return self._address

	@address.setter
	def address(self, address):
		self._address = address

	@property
	def tithe(self):
		return self._tithe

	@tithe.setter
	def tithe(self, tithe):
		self._tithe = tithe

	@property
	def spiritual_gifts(self):
		return self._spiritual_gifts

	@spiritual_gifts.setter
	def spiritual_gifts(self, spiritual_gifts):
		self._spiritual_gifts = spiritual_gifts

	@property
	def member(self):
		return self._member

	@member.setter
	def member(self, member):
		self._member = member

	@property
	def ministries(self):
		return self._ministries

	@ministries.setter
	def ministries(self, ministries):
		self._ministries = ministries

	@property
	def phone_number(self):
		return self._phone_number

	@phone_number.setter
	def phone_number(self, phone_number):
		self._phone_number = phone_number

	@property
	def start_date(self):
		return self._start_date

	@start_date.setter
	def start_date(self, start_date):
		self._start_date = start_date

	@property
	def end_date(self):
		return self._end_date

	@end_date.setter
	def end_date(self, end_date):
		self._end_date = end_date

	@property
	def left_reason(self):
		return self._left_reason

	@left_reason.setter
	def left_reason(self, left_reason):
		self._left_reason = left_reason


bob = Person()

bob.first_name = "Bob"

print(bob)
print(bob.first_name)

"""
Classes:
	Person
	Ministries
	Inventory
	Payroll

"""