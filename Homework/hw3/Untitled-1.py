import json

class Person:

    def __init__ (self, age, name, email):
        self.name =name
        self.age=age
        self.email =email


    
#inherits from person
class Student(Person):
    def __init__(self, name, age, email, StudentId):
        self.name =name
        self.age=age
        self.email =email
        self.StudentId=StudentId


    def Json(self):

