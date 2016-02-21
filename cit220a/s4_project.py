__author__ = 'Andrew'
_project_ = 'Session4'

''''You’ve been exposed to multiple ways to store data. Create a program in which you:

    Use multiple (at least 2) data structures.
    Design arrays for storing your big data scenario data.
    Print the contents of the arrays.'''

'''
For People we have the following fields
firstName
lastName
dateOfBirth
ssn
address
tithe
spiritualGifts
member
ministries
phoneNumber
startDate
endDate
leftReason
'''

class ChurchP:
    def __init__(self, firstName, lastName, dateOfBirth, ssn, address, tithe,
                 spiritualGifts, member, ministries, phoneNumber, startDate, endDate, leftReason):
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.ssn = ssn
        self.address = address
        self.tithe = tithe
        self.spiritualGifts = spiritualGifts
        self.member = member
        self.ministries = ministries
        self.phoneNumber = phoneNumber
        self.startDate = startDate
        self.endDate = endDate
        self.leftReason = leftReason

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

# Missing a puzzle piece here.

x = ChurchP(firstName, lastName, dateOfBirth, ssn, address, tithe,
                 spiritualGifts, member, ministries, phoneNumber, startDate, endDate, leftReason)
x.firstName.setter = 'Bob'
x.dateOfBirth = 10-20-2012


print(x)


robert_Mansfield = dict(firstName='Robert',
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
andrew_Maitland = dict(firstName='Andrew',
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



# I can make each person a dictionary entry and add them here, but this is not satisfying to me, I want to get this to be more automated.

# List array for now,
list1 = [robert_Mansfield,andrew_Maitland]

# How many entries
list1Count = len(list1)

i = 0
# Want to interate the list [x] should be a for or while loop.
while i < list1Count:
    print(list1[i])
    i = i + 1