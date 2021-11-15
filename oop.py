class User: # class name
    # def __init__(self, name, email, age): # constructor
    # (self, name, email) ->  #parameters
    total = 0 # instance variable
    # total juga sebagai variable global
    def __init__(self, name, email, role): 
        self.name = name #attributes
        self.email = email
        self.role = role
        User.total += 1

    # method
    def biodata(self):
        return f'{self.name} {self.email} {self.role}'

    def update_name(self, new_name):
        if self.role == 'admin':
            self.name = new_name

# abi -> instance variables
abi = User('Abi', 'abi@gmail.com', 'admin')
print(abi.biodata())
abi.update_name('dani')
print(abi.biodata())
print(User.total)

print("===========")

xian = User('Xian', 'xian@gmail.com', 'user')
print(xian.biodata())
xian.update_name('chris')
print(xian.biodata())
print(User.total)


# print(abi.name)
# print(abi.email)

# private variable (tidak bisa diakses dari luar class) contoh:
# __name = 'Abi' (mengunakan underscore/__)
