import math
'''variable'''
# type-inferred language
# number = 3
# x , y = 22, 3
# name = "nitesh"
# sName = '''sahu'''
# anger = None
# print(number)
# print(name)
'''constant''' 
# PI = 22/7
# import constant
# print(constant.PI)

# _ is the answer of the previous operation
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# print(1, 2, 3, 4, sep='#', end='&')
# help()
# print(id(v))
# print(type(x))
# keywords 32
# identifier rules


'''Special operators'''
# Identity operators
# is -- identical,
# is not
# x1 = 1
# x2 = 1
# print(x1 is x2)
# print(id(x1))
# print(id(x2))
# Membership operators
# in 
# not in
# print("ni" in name)

'''Variable Scope'''
# global namespace
# local namespace 
# nested local namespace
# nonlocal 

'''number'''
# a = 5 # any length
# b = 5.1 # up to 15 decimal point
# c = 5+1j 
# print(type(a))
# print(type(b))
# print(type(c))
# print(isinstance(b,complex))
# print(0b111)
# print(0B101)
# print(0o111)
# print(0x111)
# d = a + b # Implicit type conversion
# d = float(a) # Explicit type conversion
# print(d)
# print(0.2 + 0.1)
# import decimal
# import fractions

'''string'''
# is immutable. means charactors in the string can not be changed
st = '''nitesh''' # multiline string
# print(st[1])
# print(st[-1])
# print(st[1:5])
# st[1] = 'I' # not possible (immutable)
# del st[1] # not possible (immutable)
# fName = st
# del st
# print(st)
# print(len(name))

# print('nitesh\'s "laptop"') 
# print(r'c:\user\nitesh')
# print('nitesh\nsahu')

# print('The value of x is {} and y is {}'.format(x,y))
# print('The value of x is {1} and y is {0}'.format('x','y'))
# print('The value of x is {b} and y is {a}'.format(a='x', b='y'))
# print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

# print("Binary representation of {0} is {0:b}".format(7))
# print("Exponent representation: {0:e}".format(10.1))
# print('The value of x is %0.5f' %44)
# print("One third is: {0:.3f}".format(1/3))
# print("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))
'''Docstrings'''
# def double(num):
#     """Function to double the value"""
#     return 2*num
# print(double.__doc__)

'''STRING METHODS'''

str = 'Nitesh Sahu'
str2 = '920@gmail'

# convert only first character to uppercase and 
# all others in lowercase
# print(str.capitalize())

# convert to lowercase
# print(str.casefold())
# print(str.lower())
# print(str.upper())

# print(str.swapcase())


# return true if all characters are in lowercase
# print(str.islower())
# print(str.isupper())

# return a number of occurance of a substring
# print(str.count('s', 0,11))

# return true if str ends with substring
# print(str.endswith(('hu','sh'),0,11))
# print(str.startswith('Ni',0,11))

# return index of substring

# print(str.find('Sa',0,11))        if not found return -1
# print(str.index('Sa', 0, 11))     if not found throws ValueError exception

# return true if string is numaric
# print(str.isnumeric())

# returns a string by joining all the elements of 
# an iterable (list, string, tuple)
# l = ['n','i','t','e','s','h']
# seperator = '-'
# print(seperator.join(l))

# positional and keyword argument 
# print("Hello {0} your balance is {blc}.".format("Adam", blc=230.2346))

# print(str.replace('N', 'n'))

# separates and returns a list
# print(str.    (':', 100))
# print(str.splitlines())




# ****Nitesh****
# str.center()
# convert tab into whitespace 
# str.expandtabs()
# convert string to (utf-15) other encode  
# str.encode() 
# str.isidentifier()
# str.isdecimal()
# str.isdigit()
# str.isalnum()
# str.isalpha()
# str.isprintable()
# str.isspace()
# str.istitle()
# print(str.title())
# print(str.rjust(15,'^'))
# print(str.ljust(15,'^'))
# print(str.lstrip('Ni'))
# print(str.rstrip())
# print(str.strip('t'))
# print(str.partition('sh'))
# print(str.rfind('s'))
# print(str.rindex('s'))
# print(str.rsplit(':', 100))
# str.format_map()



'''list (mutable)'''
li = [11,12,13,'nitesh',14]
# st = [15,16]
# l = [li, st] # add both saperated by a comma
# L = [li + st] # concatinate
# print(L)
# print(L*2)
# print(l)
# print(li[1])
# print(li[1:])
# print(li[-1])
# print(li[3][2])
# li[2] = 22
# li[1:5] = [1, 2, 3]
# li.append(14.5)
# li.insert(1,11.5)
# li[1:1] = [11.5, 11.6]
# li.extend([111, 222])
# li.remove(12)
# li.pop(1)
# li.pop()
# li.clear()
# del li [3:]
# del li
# print(li.index(12))
# print(li.index(12, 1, 3)) # searches from index 1 to 3
# print(li.count(14))
# listCopy_1 = li.copy()
# listCopy_2 = li
# print(listCopy_1)
# print(listCopy_2)
# li.pop(-2)
# li[0:0] = [16, 17]
# li.sort()
# print(li)

'''tuple (immutable)'''
# tu = (11, 12, 13, 'nitesh', 14, [15,16])
# packing and unpaking
# at least one comma is mandatory
# print(tu[1])
# print(tu[3][1])
# print(tu[-2])
# print(tu[:1])
# item can not be changed or deleted
# tu[-1][0] = 9
# del tu
# print(tu.count(12))
# print(tu.index(12))
# print(tu)

'''set'''
# (element) unordered, no duplicates
# set is mutable (can add or remove items)
# se = {11, 11, 12, 13, 'nitesh', 14} # no duplicate
# se = {11, 12, 13, 'nitesh',14, [1, 2]} # not possible (mutable data)
# se = set([1, 1]) # list into set
# se = {} # dictionary
# se = set() # empty set

# no indexing, no slicing 
# se.add(10)
# se.update([15, 16])
# se.update([17, 18], {19, 20}, (21, 22))
# se.discard(22)
# se.remove(21)
# se.pop()
# se.clear()
# print(se)

# t = {11, 111, 112}
# print(se | t) # union
# print(se.union(t))
# print(t.union(se))
# print(se & t)
# print(se.intersection(t))
# print(t.intersection(se))
# print(se - t)
# print(se.difference(t))
# print(t.difference(se))
# print( se ^ t)
# print(se.symmetric_difference(t))
# print(t.symmetric_difference(se))
# fr = frozenset([111,222,333]) # immutable (no add or remove)

'''dictionary'''
# unordered, key is immutable(unique)
# di = {}
# di = {'name': 'apple', 1: [11, 12]}
# di = ([('name', 'apple'), (1, [11, 12])])
# di = dict()
# print(di[1])
# print(di['name'])     # keyError   
# print(di.get('name')) # none

# di['age'] = 25 # add
# di['name'] = 'sahu' # update
# print(di.popitem())    
# print(di.pop('name'))
# di.clear()
# del di
# print(di)

'''list comprehence'''
# l = []
# for i in range(5):
#     l.append(2**i)
# print(l)

# l = [ 2**i for i in range(5)]
# print(l)

# l = [49, 64, 81, 100, 121]
# nl = [math.sqrt(i) for i in l if i % 2 == 0]
# print(nl)

'''set comprehence'''
# word = 'programming'
# alphabates = {x for x in word}
# print(alphabates)

'''dictionary comprehence '''
# l = [1,2,3,4,5]
# square_dictionary = {x:x**2 for x in l}
# print(square_dictionary)

# old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.9}
# new_price = {key:value*1.5 if value>2 else value for (key, value) in old_price.items()}
# print(new_price)

