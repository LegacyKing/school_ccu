__author__ = 'Andrew'
_project_ = 'Session4CTE'
# Date: 2016-02-05

'''
Per previous instructions, using Python 3.5 for solving the problems.
1. print statement missing enclosing parenthesis
2. print a becomes print(a)
3. def demo(self) becomes demo() - we have no instances of self being used
4. Add '@staticmethod' so we do not need self
5. 'a' becomes print(a) for 6 lines
'''

class Session4CTE:
    @staticmethod
    def demo():
        a = [66.25, 333, 333, 1, 1234.5]
        print(a.count(333), a.count(66.25), a.count('x'))
        a.insert(2, -1)
        print(a)
        a.append(333)
        print(a)
        a.index(333)
        print(a)
        a.remove(333)
        print(a)
        a.reverse()
        print(a)
        a.sort()
        print(a)
        a.pop()
        print(a)

Session4CTE.demo()

