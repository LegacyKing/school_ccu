__author__ = 'Andrew'

class HelloWorld:
    def __init__(self, greeting):
        self.greeting = "Hello World"

    def get_value(self):
        return self.greeting

class HelloWorldOverride(HelloWorld):   # Playing with overide, a function of OOP
    def get_value(self):
        return self.greeting + " from the Child"

a = 0
z = 0

while a == 0:
    z = input("Enter 1 for Hello World, or 2 for Child version: ")
    if z == "1":
        a = 1
    if z == "2":
        a = 2

class DisplayHelloWorldParent:
    x = HelloWorld("")  # Playing with import and class
    y = HelloWorldOverride("")
    if a == 1:
        print(x.greeting)   # This outputs the actual message
    if a == 2:
        print(y.get_value())
    print("In any case, Python 3.x sends greetings!\nHere are both greetings!", x.greeting, "&", y.get_value())


