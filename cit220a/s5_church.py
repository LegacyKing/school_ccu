__author__ = 'Andrew'
_project_ = 'Session4'

# Date: 2016-02-05

# This is the Big Data project. My project encompassed data a church would likely keep track of.
# I set up namedtuples of key with labels=value. I then set them up in a list to iterate across the array and print each entry in a concise manner
# This meets the basic requirements of two data array types. LIST and TUPLE
# With the printing, we are using the list to fill in the blanks in an organized human readable format. A raw format could be achieved just as easily.

# With some input from Dwain, I did play with the Enumerator function for the first group.



from enum import Enum
from collections import namedtuple


# Assignment Session 5:
# Grab messages of value to display

# Add, attendance Count
# Line Chart - Attendance by Service

# Comparison -
# Member Joined - by Year
# Member Left - by Year

# Ministry volunteers vs. paid staff
# Need a count

# Church attendance - experimenting
churchAttendance = [1000, 2000, 1500, 1750, 2200]

churchAttendanceCount = len(churchAttendance)

i = 0

while i < churchAttendanceCount:
	print("Month: ",i+1 , churchAttendance[i])
	i = i + 1

def churchAttendance():
	churchAttendance = [1000, 2000, 1500, 1750, 2200]
	return churchAttendance


# Using namedtuple as the primary data storage method
# Labels should be self explanatory. This lists the available labels in "Person"
Person = namedtuple("Person", ['firstName',
                                'lastName',
                                'dateOfBirth',
                                'ssn',
                                'address',
                                'tithe',
                                'spiritualGifts',
                                'member',
                                'ministries',
                                'phoneNumber',
                                'startDate',
                                'endDate',
                                'leftReason'])
	# Playing with the Enum feature
class Ministry(Enum):
			Youth = 1,
			Safety = 2,
			Mens = 3

SpiritualGift = namedtuple('SpiritualGift', ['name'])   # We can set up namedtuples for each known spiritual gift, if desired.

sg_discernment = SpiritualGift('discernment')


# People - ideally a database outside the file, but not a requirement for this assignment
drew = Person(firstName='Andrew',
		              lastName='Maitland',
		              dateOfBirth='1/3/2000',
		              ssn='111 11 1112',
		              address='112 main street',
		              tithe='yes',
		              spiritualGifts=sg_discernment,
		              member='yes',
		              ministries=[Ministry.Youth, Ministry.Safety],
		              phoneNumber='111 222 4444',
		              startDate='2016-01-02',
		              endDate='2016-02-03',
		              leftReason='Moving')

john = Person(firstName='John',
		              lastName='Doe',
		              dateOfBirth='1/3/2000',
		              ssn='111 11 1112',
		              address='112 main street',
		              tithe='yes',
		              spiritualGifts=sg_discernment,
		              member='yes',
		              ministries=[Ministry.Youth, Ministry.Mens],
		              phoneNumber='111 222 4444',
		              startDate='2016-01-02',
		              endDate='2016-02-03',
		              leftReason='Visiting from out of state')
# Export - using the tuple named labels, we can alter how we display on output.
# Using manual entry list.



def peoplelist():
	people = [drew, john]
	return people



# Give each section it's own Header
if (1 > 2):
			print("Church Directory: ")
			for person in people:   # Loop through the available entries
				print('First Name: ' + person.firstName)
				print('Last Name: ' + person.lastName)
				print('Ministries: ')
				for ministry in person.ministries:
					print('\t' + str(ministry))
				print('Spiritual Gifts:')
				for gift in person.spiritualGifts:
					print('\t' + gift)
				print('Dob: ' + person.dateOfBirth)
				print('SSN: ' + person.ssn)
				print('Address: ' + person.address)
				print('Tithes?: ' + person.tithe)
				print('Member: ' + person.member)
				print('Phone: ' + person.phoneNumber)
				print('Joined: ' + person.startDate)
				print('Left: ' + person.endDate)
				print('Reason for leaving: ' + person.leftReason)
				print("")
# We repeat the pattern for the other categories.
# Since the pattern is repeated, I will not include further notes beyond this point.
'''
ministryTitle
ministryPaid
ministrySalary
ministryDuties
ministryDaysAvailable
ministryReportsTo
ministrySupervises
ministryPhoneNumber
'''
ChurchMinistry = namedtuple("ChurchMinistry", ['ministryTitle',
                                    'ministryPaid',
                                    'ministrySalary',
                                    'ministryDuties',
                                    'ministryDaysAvailable',
                                    'ministryReportsTo',
                                    'ministrySupervises',
                                    'ministryPhoneNumber'])

Pastor = ChurchMinistry(ministryTitle='Pastor',
                    ministryPaid='Yes',
                    ministrySalary='Rate Schedule 5',
                    ministryDuties='Conduct Worship Services',
                    ministryDaysAvailable='All Week',
                    ministryReportsTo='Church Council',
                    ministrySupervises='Church Ministries',
                    ministryPhoneNumber='111 222 3333x55')
ChildcareP = ChurchMinistry(ministryTitle='Child Care Paid',
                    ministryPaid='Yes',
                    ministrySalary='Rate Schedule 1',
                    ministryDuties='Childcare as outlined in S2.8',
                    ministryDaysAvailable='All Week',
                    ministryReportsTo='Child Care Supervisor',
                    ministrySupervises='Children and Child Care Volunteers',
                    ministryPhoneNumber='none')
Safety = ChurchMinistry(ministryTitle='Safety',
                    ministryPaid='No',
                    ministrySalary='None',
                    ministryDuties='Maintain Campus Safety',
                    ministryDaysAvailable='All Week',
                    ministryReportsTo='Safety Director',
                    ministrySupervises='None',
                    ministryPhoneNumber='None')

ministryL = [Pastor, ChildcareP, Safety]
ministryPaidL = 0
ministryVolunteerL = 0

for ChurchMinistry in ministryL:
	if (ChurchMinistry.ministryPaid == 'Yes'):
		ministryPaidL = ministryPaidL + 1
	if (ChurchMinistry.ministryPaid == 'No'):
		ministryVolunteerL = ministryVolunteerL + 1


print("Paid = ", ministryPaidL)
print("Volunteers = ", ministryVolunteerL)

def paidStaff():
	return ministryPaidL

def volunteerStaff():
	return ministryVolunteerL



if (1 > 2):
		print("Church Ministry Listing: ")
		for ChurchMinistry in ministryL:
			print('Ministry Title: ' + ChurchMinistry.ministryTitle)
			print('Paid?: ' + ChurchMinistry.ministryPaid)
			print('Duties: ' + ChurchMinistry.ministryDuties)
			print('Available: ' + ChurchMinistry.ministryDaysAvailable)
			print('Reports to: ' + ChurchMinistry.ministryReportsTo)
			print('Supervises: ' + ChurchMinistry.ministrySupervises)
			print('Phone Number: ' + ChurchMinistry.ministryPhoneNumber)
			print("")


# Inventory Section
Inventory = namedtuple("Inventory", ['itemName',
                                    'itemCost',
                                    'itemQuantity',
                                    'itemSupplierName',
                                    'itemSupplierReorderPart',
                                    'itemSupplierPhone',
                                    'itemStoredLocation',
                                    'itemComments'])


Wrench = Inventory(itemName='Wrench',
                    itemCost='12.00',
                    itemQuantity='5',
                    itemSupplierName='Church Supplier Goods',
                    itemSupplierReorderPart='112-xyz',
                    itemSupplierPhone='111 123 4567',
                    itemStoredLocation='Tool Shed',
                    itemComments='Durable, 10 year warranty, bought on 2000-01-02')
CommunionWafers = Inventory(itemName='Communion Wafers',
                            itemCost='1.00',
                            itemQuantity='500',
                            itemSupplierName='Church Supplier Goods',
                            itemSupplierReorderPart='777-holy',
                            itemSupplierPhone='111 123 4567',
                            itemStoredLocation='Kitchen',
                            itemComments='Perishable, re-order monthly')

items = [Wrench, CommunionWafers]
if (1 > 2):
		print("Church Inventory: ")
		for Inventory in items:
			print('Item Name: ' + Inventory.itemName)
			print('Item Cost: ' + Inventory.itemCost)
			print('Item Quantity: ' + Inventory.itemQuantity)
			print('Supplier Name: ' + Inventory.itemSupplierName)
			print('Reorder number: ' + Inventory.itemSupplierReorderPart)
			print('Supplier Phone: ' + Inventory.itemSupplierPhone)
			print('Location: ' + Inventory.itemStoredLocation)
			print('Comments: ' + Inventory.itemComments)
			print("")

'''
titheService
titheDate
titheAmount
titheType
titheGivenBy
titheEarmarked
titheEarmarkDesignation
titheComments
'''
#    def tithe(self):        pass
Tithe = namedtuple("Tithe", ['titheService',
                                    'titheDate',
                                    'titheAmount',
                                    'titheType',
                                    'titheGivenBy',
                                    'titheEarmarked',
                                    'titheEarmarkDesignation',
                                    'titheComments'])


TWeek1 = Tithe(titheService='Sunday',
                    titheDate='12.01.16',
                    titheAmount='5000',
                    titheType='Envelope',
                    titheGivenBy='Lucy',
                    titheEarmarked='General',
                    titheEarmarkDesignation='General Funds',
                    titheComments='No comments')
TWeek1a = Tithe(titheService='Sunday',
                    titheDate='12.01.16',
                    titheAmount='250',
                    titheType='Credit',
                    titheGivenBy='Jose',
                    titheEarmarked='Christmas Offering',
                    titheEarmarkDesignation='Building Funds',
                    titheComments='No comments')

TitheL = [TWeek1, TWeek1a]
if (1 > 2):
	print("Church Tithe: ")
	for Tithe in TitheL:
		print('Tithe Service: ' + Tithe.titheService)
		print('Tithe Date: ' + Tithe.titheDate)
		print('Tithe Amount: ' + Tithe.titheAmount)
		print('Tithe Type: ' + Tithe.titheType)
		print('Tithe Given By: ' + Tithe.titheGivenBy)
		print('Tithe Earmarked?: ' + Tithe.titheEarmarked)
		print('Tithe Designation: ' + Tithe.titheEarmarkDesignation)
		print('Tithe Comments: ' + Tithe.titheComments)
		print("")

'''
payrollFirstName
payrollLastName
payrollPosition
payrollPayRate
payrollHoursLogged
payrollSickTime
payrollPTO
payrollComments
payrollSSN
payrollPeriod
payrollRaises
'''



Payroll = namedtuple("Payroll", ['payrollFirstName',
                                 'payrollLastName',
                                 'payrollPosition',
                                 'payrollPayRate',
                                 'payrollHoursLogged',
                                 'payrollSickTime',
                                 'payrollPTO',
                                 'payrollComment',
                                 'payrollSSN',
                                 'payrollPeriod',
                                 'payrollRaises'])


PDrew = Payroll(payrollFirstName='Andrew',
                payrollLastName='Maitland',
                payrollPosition='Safety',
                payrollPayRate='10.00',
                payrollHoursLogged='2',
                payrollSickTime='none',
                payrollPTO='none',
                payrollComment='Worked paid event',
                payrollSSN='111-11-1111',
                payrollPeriod='2016-01-01/2016-02-01',
                payrollRaises='none')

PRob = Payroll(payrollFirstName='Robert',
                payrollLastName='Mansfield',
                payrollPosition='Pastor',
                payrollPayRate='50.00',
                payrollHoursLogged='40',
                payrollSickTime='10',
                payrollPTO='5',
                payrollComment='None',
                payrollSSN='111-11-2221',
                payrollPeriod='2016-01-01/2016-02-01',
                payrollRaises='none')
payrollL = [PDrew, PRob]
if (1 > 2):
	print("Payroll List: ")
	for Payroll in payrollL:
		print('Name: ' + Payroll.payrollFirstName + ' ' + Payroll.payrollLastName)
		print('Position: ' + Payroll.payrollPosition)
		print('Pay Rate: $' + Payroll.payrollPayRate)
		print('Hours logged: ' + Payroll.payrollHoursLogged)
		print('Sick Time: ' + Payroll.payrollSickTime)
		print('PTO: ' + Payroll.payrollPTO)
		print('Comment: ' + Payroll.payrollComment)
		print('SSN: ' + Payroll.payrollSSN)
		print('Pay Period: ' + Payroll.payrollPeriod)
		print('Raise?: ' + Payroll.payrollRaises + "\n")


# EOF