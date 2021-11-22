class Employee:
    def __init__(self,age,name,salary):
        self.name = 'Abi'
        self.age = 22
        self.salary = 1000
    def __str__(self):
        return f'Halo namaku {self.name} umur {self.age} gaji {self.salary}'
    def __len__(self):
        return self.age
    def __del__(self):
        print('data sudah terhapus')
abi = Employee(22,'Abi',1000)
print(abi)
print(str(abi))
print(len(abi))
del abi