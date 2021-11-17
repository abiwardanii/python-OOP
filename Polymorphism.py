class Teen:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} !')

class Student(Teen):
    def info(self):
        print(f'My name is {self.name} and I am a student')

class Employee(Teen):
    def info(self):
        print(f'My name is {self.name} and I am an employee')
    
    #over riding
    def info(self, data):
        self.data = data
        print(f'My name is {self.name} and I am an employee for {self.data}')

student = Student('Abi')
student.info()

employee = Employee('Xian')
employee.info('PT. ABC')

# Polimorfisme dalam OOP merupakan sebuah konsep OOP di mana class memiliki banyak “bentuk” method yang berbeda, 
# meskipun namanya sama
