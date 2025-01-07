# init() is the constructor function that is called whenever a new object of that class is instantiated.


# check_pass_fail
'''class student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

roll_no_1 = student('ram',43)
roll_no_2 = student('shyam', 39)
did_pass_1 = roll_no_1.check_pass_fail()
did_pass_2 = roll_no_2.check_pass_fail()
print('Did roll No.1 passed :- ', did_pass_1)
print('Did roll No.2 passed :- ', did_pass_2)'''

# add complex number 
'''class complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    
    def add(self,num):
        real = self.real + num.real
        imag = self.imag + num.imag
        result = complex(real,imag)
        return result

n1 = complex(2,3)
n2 = complex(1,2)
res = n1.add(n2)
print(res.real)
print(res.imag)'''

# inheritance
'''class bird:
    
    def __init__(self):
        print('Bird is ready')

    def whoisThis(self):
        print('Bird')
    
    def swim(self):
        print('Swim Faster')

class penguin(bird):
    
    def __init__(self):
        super().__init__()
        print('penguin is ready')
    
    def whoisThis(self):
        print('Penguin')
    
    def run(self):
        print('Run faster')

peggy = penguin()
peggy.whoisThis()
peggy.run()
peggy.swim()'''

'''class Person:
    
    def __init__(self, name, aadhar_no):
        self.name = name
        self.aadhar_no = aadhar_no

    def is_hard_working(self):
        print('Yes,',self.name,'is a hardworking person.')

class Emp(Person):
    
    def __init__(self, name, aadhar_no, emp_id):

        self.emp_id = emp_id
        Person.__init__(self, name, aadhar_no)


emp_1 = Emp('nitesh', 236098350086, 101)

print(emp_1.name)

emp_1.is_hard_working()'''

# Encapsulation
class computer:

    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        # print('Price is ', self.__maxprice)
        print('Price is {}'.format(self.__maxprice))
    
    def setMaxPrice(self,price):
        self.__maxprice = price

asus = computer()

asus.sell()
# __maxprice is encapsulated can not change like this
# asus.__maxprice = 1000
asus.setMaxPrice(1100)
asus.sell()

#polymorphism

# polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function

# in-built poly-morphic
'''print(len("geeks"))

print(len([10, 20, 30]))'''

# Data Abstraction
