class Teen:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} !')

class TeenMilenial(Teen):
    email = None
    __password = None

    # public method
    def set_age(self, age):
        self.age = age

    # public method
    def set_pass(self, password):
        self.__password = password
    
    # private method (proses encapsulation)
    def __myPass(self):
        return self.__password.replace('a', '*')

    # public method
    def info(self):
        print(f'My name is {self.name} I am {self.age} my password is {self.__myPass()}')

abi = TeenMilenial('Abi')
abi.set_age(23)
abi.set_pass('rahasia123')
abi.info()

 
