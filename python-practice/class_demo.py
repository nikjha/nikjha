#!/usr/bin/python3
class Person:
    def set_details(self):
        self.name=input("Enter your name: ")
        self.age=input("Enter your age : ")
        return self

    def display(self):
       #list_a = Person.set_details(self)
       #print(list_a.name)

        print(self.name, "is in reboot mode at age of ",self.age)

    def greet(self):
        print("All the best", self.name, "!")

p1 = Person()
#p2 = Person()

#p1.set_details()
p1.display()
p1.greet()

#
