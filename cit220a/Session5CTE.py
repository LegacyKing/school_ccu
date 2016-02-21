__author__ = 'Andrew'
_project_ = 'Session5CTE'
# Date: Feb 8th, 2016

'Enter your comments about what the errors were and how you corrected them'
'''
Add staticmethod        @staticmethod
remove self - not referenced
all print methods missing enclosing parenthesis
pprint only takes one object, split last statement
'''

from pprint import pprint


class Session5CTE:
    @staticmethod
    def demo():
        names = ['Smith, John', 'Rollins, Mary', 'Mullen, Bill', 'Thomas, Harry', 'Kneir, Jan', 'Hill, Joan',
                 'Rodriguez, Toby', 'Simpson, Camelle', 'Doe, Jane', 'Aziz, Omar']
        dateJoined = [19990130, 19901130, 20000301, 20020608, 20001023, 20041101, 19980615, 20100131, 20010919,
                      20000826]
        together = names + dateJoined
        print(names, dateJoined)
        print(together)
        pprint(names)
        pprint(dateJoined)
        pprint(together, indent=4, width=60, depth=2)

        for names, dateJoined in zip(names, dateJoined):
            if dateJoined > 20000000:
                pprint(names)
                pprint(dateJoined)

Session5CTE().demo()

