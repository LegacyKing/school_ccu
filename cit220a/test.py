__author__ = 'Andrew'

#import s3_helloworld    # Imports from another file

#x = s3_helloworld.HelloWorld("") # Playing with import and class

#print(x.greeting)   # This outputs the actual message

%quickref

import numpy as np


from enum import Enum

PlanetType = Enum('PlanetType',
                  'gas ice storm barren temperate lava oceanic plasma shattered')
class Planet:
    def __init__(self, name, url, planet_type, x, y, z):
        self._firstName = firstName
        self._lastName = lastName
        self._planet_type = planet_type
        self._x = x
        self._y = y
        self._z = z

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


Rob = Person(firstName='Robert',
                                lastName='Mansfield',
                                dateOfBirth='1/1/2000',
                                ssn='111 11 1111',
                                address='111 main street',
                                tithe='yes',
                                spiritualGifts='Discernment',
                                member='no',
                                ministries=['youth', 'hospital visitation'],
                                phoneNumber='111 222 3333',
                                startDate='Jan 01 2016',
                                endDate='Feb 01 2016',
                                leftReason='None given')
Drew = Person(firstName='Andrew',
                                lastName='Maitland',
                                dateOfBirth='1/3/2000',
                                ssn='111 11 1112',
                                address='112 main street',
                                tithe='yes',
                                spiritualGifts='Discernment',
                                member='yes',
                                ministries=['safety', 'youth'],
                                phoneNumber='111 222 4444',
                                startDate='Jan 02 2016',
                                endDate='Feb 03 2016',
                                leftReason='Moving')
#print(robert_Mansfield)
#print(andrew_Maitland)

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

#    def ministery(self):        pass

'''
itemName
itemCost
itemQuantity
itemSupplierName
itemSupplierReorderPart
itemSupplierPhone
itemStoredLocation
itemComments
'''

#    def inventory(self):        pass


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
#    def ministry(self):         pass


#Dictionary format
robert_Mansfield = dict(firstName='Robert',
                                lastName='Mansfield',
                                dateOfBirth='1/1/2000',
                                ssn='111 11 1111',
                                address='111 main street',
                                tithe='yes',
                                spiritualGifts='Discernment',
                                member='no',
                                ministries=['youth', 'hospital visitation'],
                                phoneNume='111 222 3333',
                                startDate='Jan 01 2016',
                                endDate='Feb 01 2016',
                                leftReason='None given')
andrew_Maitland = dict(firstName='Andrew',
                                lastName='Maitland',
                                dateOfBirth='1/3/2000',
                                ssn='111 11 1112',
                                address='112 main street',
                                tithe='yes',
                                spiritualGifts='Discernment',
                                member='yes',
                                ministries=['safety', 'youth'],
                                phoneNume='111 222 4444',
                                startDate='Jan 02 2016',
                                endDate='Feb 03 2016',
                                leftReason='Moving')


#PlanetType = Enum('PlanetType', 'gas ice storm barren temperate lava oceanic plasma shattered')







Ministries = Enum('Ministries',
                  'Youth Safety CR Men Women Childcare')

class ChurchP:
    def __init__(self, firstName, lastName, dateOfBirth, ssn, address, tithe,
                 spiritualGifts, member, ministries, phoneNumber, startDate, endDate, leftReason):
        self._firstName = firstName
        self._lastName = lastName
        self._dateOfBirth = dateOfBirth
        self._ssn = ssn
        self._address = address
        self._tithe = tithe
        self._spiritualGifts = spiritualGifts
        self._member = member
        self._ministries = ministries
        self._phoneNumber = phoneNumber
        self._startDate = startDate
        self._endDate = endDate
        self._leftReason = leftReason

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, firstName):
        self._firstName = firstName

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName

    @property
    def dateOfBirth(self):
        return self._dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth):
        self._dateOfBirth = dateOfBirth

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
    def spiritualGifts(self):
        return self._spiritualGifts

    @spiritualGifts.setter
    def spiritualGifts(self, spiritualGifts):
        self._spiritualGifts = spiritualGifts

    @property
    def member(self):
        return self._member

    @member.setter
    def member(self, member):
        self._member = member

    @property
    def ministries(self):
        return self.ministries

    @ministries.setter
    def ministries(self, ministries):
        self._ministries = ministries

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    @property
    def startDate(self):
        return self._startDate

    @startDate.setter
    def startDate(self, startDate):
        self._startDate = startDate

    @property
    def endDate(self):
        return self._endDate

    @endDate.setter
    def endDate(self, endDate):
        self._endDate = endDate

    @property
    def leftReason(self):
        return self._leftReason

    @leftReason.setter
    def leftReason(self, leftReason):
        self._leftReason = leftReason

from pandas import Series, DataFrame
import pandas as pd

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': {1.5, 1.7, 3.6, 2.4, 2.9}}
frame = DataFrame(data)

frame





from collections import namedtuple
from enum import Enum

, first_name, last_name, date_of_birth, ssn, address, tithe, spiritual_gifts, member, ministries,
	             phone_number, start_date, end_date, left_reason



 @property
    def firstName(self):
        return self.firstName

    @firstName.setter
    def firstName(self, firstName):
        self.firstName = firstName

    @property
    def lastName(self):
        return self.lastName

    @lastName.setter
    def lastName(self, lastName):
        self.lastName = lastName

    @property
    def dateOfBirth(self):
        return self.dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth

    @property
    def ssn(self):
        return self.ssn

    @ssn.setter
    def ssn(self, ssn):
        self.ssn = ssn

    @property
    def address(self):
        return self.address

    @address.setter
    def address(self, address):
        self.address = address

    @property
    def tithe(self):
        return self.tithe

    @tithe.setter
    def tithe(self, tithe):
        self.tithe = tithe

    @property
    def spiritualGifts(self):
        return self.spiritualGifts

    @spiritualGifts.setter
    def spiritualGifts(self, spiritualGifts):
        self.spiritualGifts = spiritualGifts

    @property
    def member(self):
        return self.member

    @member.setter
    def member(self, member):
        self.member = member

    @property
    def ministries(self):
        return self.ministries

    @ministries.setter
    def ministries(self, ministries):
        self.ministries = ministries

    @property
    def phoneNumber(self):
        return self.phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    @property
    def startDate(self):
        return self.startDate

    @startDate.setter
    def startDate(self, startDate):
        self.startDate = startDate

    @property
    def endDate(self):
        return self.endDate

    @endDate.setter
    def endDate(self, endDate):
        self.endDate = endDate

    @property
    def leftReason(self):
        return self.leftReason

    @leftReason.setter
    def leftReason(self, leftReason):
        self.leftReason = leftReason



        		self._firstName = firstName
		self._lastName = lastName
		self._dateOfBirth = dateOfBirth
		self._ssn = ssn
		self._address = address
		self._tithe = tithe
		self._spiritualGifts = spiritualGifts
		self._member = member
		self._ministries = ministries
		self._phoneNumber = phoneNumber
		self._startDate = startDate
		self._endDate = endDate
		self._leftReason = leftReason