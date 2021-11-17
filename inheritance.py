class Teen:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} says I am a teenager!')

#contoh inheritence class TeenMilenial dari class Teen
class TeenMilenial(Teen):
    def set_age(self, age):
        self.age = age
    def info(self):
        print(f'My name is {self.name} I am {self.age}')

abi = TeenMilenial('Abi')
abi.set_age(20)
abi.speak()
abi.info()
#inherintace adalah mengcopy code dari class yang lain(turunan class)