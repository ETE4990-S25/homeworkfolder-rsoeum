import json

class Person:
    def __init__ (self, name, age, email):
        self.name =name
        self.age=age
        self.email =email

def to_dict(self):
    return {
        "name": self.name,
        "age": self.age,
        "email": self.email
    }
    
class Student(Person):
    def __init__(self, name, age, email, StudentId):
        super().__init__(name,age,email)
        self.StudentId=StudentId


    def Json(self):
        return json.dumps(self.to_dict(), indent=4)
    
def save_to_json(data, filename="students.json"):
    with open (filename, "w")as file:
        json.dump(data, file, indent=4)
