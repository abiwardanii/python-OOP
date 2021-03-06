class User: # class name
    # def __init__(self, name, email, age): # constructor
    # (self, name, email) ->  #parameters
    total = 0 # instance variable
    # total juga sebagai variable global
    def __init__(self, name, email, role): 
        self.name = name #attributes
        self.email = email
        self.__role = role
        User.total += 1

    # method
    def biodata(self):
        return f'{self.name} {self.email} {self.__role}'

    def update_name(self, new_name):
        if self.__role == 'admin':
            self.name = new_name
    #property
    @property
    def role(self):
        return self.__role

    #setter
    @role.setter
    def role(self, new_role):
        if new_role == 'admin':
            self.__role = new_role
        else:
            print('Role must be admin')
    # def getRoles(self):
    #     return self.__role

    #classmethod = mengacu parameter ke class
    @classmethod
    def set_total(cls, new_total):
        User.total = new_total

    @staticmethod
    def print_total():
        print(f'Total user: {User.total}')

# abi -> instance variables
abi = User('Abi', 'abi@gmail.com', 'admin')
print(abi.biodata())
abi.update_name('dani')
print(abi.biodata())
print(abi.__dict__)
# print(abi.getRoles())
print(User.total)

print("===========")

xian = User('Xian', 'xian@gmail.com', 'user')
print(xian.biodata())
xian.update_name('chris')
print(xian.biodata()) #nama tidak berubah
print(xian.__dict__)
xian.role = 'admin'
print(xian.biodata()) #role berubah
print(User.total)

User.set_total(10) #dari classmethod
print(User.total)

User.print_total() #dari staticmethod

# print(xian.__role) #output error


# print(abi.name)
# print(abi.email)

# private variable (tidak bisa diakses dari luar class) contoh:
# __name = 'Abi' (mengunakan underscore/__)
