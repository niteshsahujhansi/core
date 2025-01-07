# function 
'''def greet(name):

    This function greets to
    the person passed in as
    a parameter
    
    print('hello, '+ name + '. Goodmorning!')

name = input('Enter the name: ')
greet(name)
print(greet.__doc__)'''

'''def positive(num):
    if num >= 0:
        print(num)
    else:
        print(-num)
num = 5
positive(num)'''

# Python Default Arguments
# Python Keyword Arguments
'''def greet(name, msg = 'Goodmorning'):
    print('Hello',name,msg)
greet('ram')
greet('ram', 'goodnight')
greet(name = 'nik')
greet('nitesh', msg = 'goodafternoon')'''

# Python Arbitrary Arguments
'''def greet(*names):
    for name in names:
        print('Hello ' + name + ' Goodmorning')
greet('nik', 'nitesh', 'ram')'''

# recursion 
'''def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)
n=6
print(fac(n))'''

# lambda filter map 
l = [1, 15, 4, 6, 8, 11, 3, 12]
nl1 = list( filter( lambda x: (x%2==0), l ) ) # filter even
nl2 = list( map( lambda x: x*2, l ) ) # double
print(nl1)
print(nl2)

# global nonlocal
