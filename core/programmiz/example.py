
import math
import cmath
import random
import calendar

# Squre root of complex number
'''n = 625
c = 1+2j
sr = n ** 0.5
# sr = math.sqrt(n)
csr = cmath.sqrt(c) 
print(sr)
print(csr)
print('Square root of {0} is {1:0.2f}+{2:0.2f}j' .format(sr, csr.real, csr.imag))'''

#area of trangle
'''a,b,c = 5,6,7
s = (a+b+c)/2
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print(area)'''

# find root of Quadratic equation
'''a,b,c = 1,5,6
d = (b**2) - (4*a*c) 
r1 = (-b - cmath.sqrt(d))/(2*a)
r2 = (-b + cmath.sqrt(d))/(2*a)
print(r1)
print(r2)'''

# swap
'''a = 5
b = 10

# temp = a
# a = b
# b = temp

# a,b = b,a

a = a + b
b = a - b
a = a - b

print(a)
print(b)'''

# generate random number 
'''print(random.randint(0,10))'''

# leap year
'''year = 1994
print('Is {} a leap year'.format(year))
if year % 400 == 0:
    print(True)
elif year % 100 == 0:
    print(False)
elif year % 4 == 0:
    print(True)
else:
    print(False)'''

# is prime
'''n = int(input('Enter Number: '))
flag = 1
if n>1:
    for i in range(2,n):
        if n % i == 0:
            flag = 0
            break
if flag:
    print('True')
else:
    print('False')'''

# is prime
'''n = int(input('Enter a positive Number: '))
if n>1:
    for i in range(2,n):
        if n % i == 0:
            print(False)
            break
    else:
        print(True)
else:
    print('invalid input')'''

# print prime numbers up to n 
'''def isPrime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n % i == 0:
                return False
                break
        else:
            return True
num = 100
for i in range(1,num+1):
    if (isPrime(i)):
        print(i, end=' ')'''

# print first n prime number
'''def nextPrime(n):
    while True:
        n += 1
        for i in range(2,n):
            if n%i == 0:
                break
        else:
            return n
def primeProducer(N):
    c,num = 1,1
    while c<=N:
        num = nextPrime(num)
        yield num
        c += 1

num = int(input('How many prime numbers do you want: '))
l = [x for x in primeProducer(num)]
print(l)'''

# prime number within a range
'''x,y = 10,50
for num in range(x,y+1):
    if num > 1:
        for i in range(2,(num//2)+1):
            if num%i == 0:
                break
        else:
            print(num)'''

# factorial
'''def fac(n):
    if n==1:
        return 1
    else:
        return n * fac(n-1)
n = 6
res = fac(n)
print(res)'''

'''n,fac = 6,1
if n<1:
    print("Factorial does not exist for negative number.")
elif n==0:
    print('factorial of 0 is 1')
else:
    for i in range(1,n+1):
        fac = fac * i
print(fac)'''

# table
'''n = 2
for i in range(1,11):
    res = i * n 
    print(n, 'X', i, '=', res)'''

# fibonacci
'''a,b = 0,1
n = 10'''

'''for i in range(n+1):
    if i == 0:
        print(a)
    elif i == 1:
        print(b)
    else:
        a,b = b,a+b
        print(b)'''

'''if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    print(a)
    print(b)
    for i in range((n-1)):
        c = a + b
        a = b
        b = c
        print(b)'''

# fn for nth fibonacci number
'''def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(6))'''

# check armstrong
'''n = 1634
t = n
sum = 0

order = len(str(n))

while(t>0):

    d = t % 10
    d = d ** order
    sum += d
    t //= 10

# print(sum)

if sum == n:
    print('{} is an armstrong number'.format(n))
else:
    print('{} is not an armstrong number'.format(n))'''

# armstrong
'''start = 100
n = 1634

for i in range(start, n+1):
    
    t = i 
    sum  = 0 
    order = len(str(i))

    while( t > 0):

        d = t % 10
        d = d ** order 
        sum += d 
        t //= 10 

    if sum == i :
        print('{} is an armstrong numebr'.format(i))'''

# sum of n 
'''start = 0
n = 16
sum = 0 
for i in range(start, n+1):
    sum = sum + i 
print(sum)'''

# 2 rise to power i
'''term  = 5
result = list(map(lambda x: 2 ** x , range(term)))
for i in range(term):
    print('2 rise to power', i, 'is', result[i])'''

# multiple of a number

# decimal and ASCII and Calander
'''decimal = 7
print ('binary of {} is {} '.format(decimal, bin(decimal)))
print ('octal of {} is {} '.format(decimal, oct(decimal)))
print ('Hexadecimal of {} is {} '.format(decimal, hex(decimal)))
ch = 'A'
print('ASCII value of {} is {}'.format(ch, ord(ch)))
print(calendar.month(yy, mm))'''

# HCF or GCG
'''def gcd(x,y):
    # if x < y :
    #     smaller = x 
    # else:
    #     smaller = y
    for i in range(1, x + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf 
print(gcd(24,72))'''

'''def gcd(x,y):
    while(y):
        x, y = y, x % y 
    return x
print(gcd(54,24))'''

# lcm
'''def lcm(x,y):
    if x < y:
        greater = y
    else:
        greater = x
    while(True):
        if(greater % x == 0) and (greater % y == 0):
            lcm = greater 
            break 
        greater += 1
    return lcm 
print(lcm(24,54))'''

'''def gcd(x,y):
    while(y):
        x, y = y, x % y 
    return x
def lcm(x,y):
    lcm = (x * y) // gcd(x, y)
    return lcm
print(lcm(24,54))'''

# factors of a number 
'''n = 320
for i in range(1, n+1) :
    if (n % i == 0) :
        print(i)'''

# decimal to binary using recursion
'''def decimal_to_binary(n):
    if n > 1 :
        decimal_to_binary(n//2)
    print(n % 2, end=' ')
decimal_to_binary(34)'''

# add matrix
'''X = [[12,7,3],
    [4 ,5,6],
    [7,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
# print(result)
for r in result:
    print(r)'''

'''X = [[12,7,3],
    [4,5,6],
    [7,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [X[i][j] + Y[i][j] for j in range(len(X[0])) for i in range(len(X))]
print(result)'''

# multiply matrix
'''X = [[2,3],
    [4,5]]

Y = [[6,1],
    [2,3]]

result = [[0,0],
            [0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for r in result:
    print(r)'''

# check palindrome string
'''str = 'aIbohPhoBiA'
str = str.casefold()
reverse_str = reversed(str)
if list(str) == list(reverse_str):
    print('yes palindrome')
else:
    print('not palindrome')'''

# short words
'''str = 'Sita Ram radha krishna Lakshmi narayan'
str = str.lower()
word = str.split()
word.sort()
print(word)'''

'''str = 'Sita Ram radha krishna Lakshmi narayan'
word = [i.lower() for i in str.split()]
word.sort()
print(word)'''

# count vowels
'''str = 'nitesh'
v = 'aeiouAEIOU'
count = 0
for i in str:
    for j in v:
        if i == j:
            count += 1
print(count)'''

'''str = 'nitesh'
v = 'aeiouAEIOU'
count = 0
for i in str:
        if i in v:
            count += 1
print(count)'''

# count each vowel 
'''str = 'Nitesh Sahu loves programming'
str = str.casefold()
vowel = 'aeiou'
each_vowel = dict.fromkeys(vowel,0)
for i in str:
    if i in each_vowel:
        each_vowel[i] += 1
print(each_vowel)'''

# mail marge
'''with open('text_files/message','w') as message:
    message.write('You are invited for dinner on 30/02/2023')
with open('text_files/message','r') as message:
    message = message.read()
    print(message)
    with open('text_files/names','w') as names:
        names.write('ni')
    with open('text_files/names','r') as names:
        # names = names.read()
        for i in names:
            mail = 'Hello' + i + '\n' + message 
            with open(i.strip()+".txt", 'w') as mails:
                mails.write(mail)

            with open('text_files/mails','r') as mails:
                mails = mails.read()
                print(mails)'''

'''with open('text_files/names','r') as names:
    with open('text_files/message','r') as message:
        message = message.read()
    for i in names:
        mail = 'Hello ' + i.strip() + '\n' + message

        with open(i.strip()+'.txt', 'w') as mails:
            mails.write(mail)'''

# resolution of image 
'''with open('img1.jpg','rb') as img:
    img.seek(163)
    a = img.read(2)
    height = (a[0] << 8) + a[1]
    a = img.read(2)
    width = (a[0] << 8) + a[1]
print(height, 'x', width)'''

# hash of a file (error)
'''import hashlib
def hash_file(file_name):
    h = hashlib.sha1()
    with open('file_name','rb') as file:
        chunk = 0
        while chunk != b' ':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

hash_value = hash_file('nitesh')
print(hash_value)'''

# half pyramid 
'''n = 5
for i in range(n):
    for j in range(i):
        print('*', end=' ')
    print()'''
# inverted half pyramid
'''n = 5
for i in range(n):
    for j in range(i,n):
    # for j in range(i,n):
        print('*', end=' ')
    print()'''

# inverted half pyramid
'''n = 5
for i in range(n,0,-1):
    for j in range(i):
    # for j in range(i,n):
        print('*', end=' ')
    print()'''

# full pyramid
'''n = 5
for i in range(n):
    for j in range(0,n-i-1):
        print(end=' ')
    for j in range(0,i+1):
        print('*',end=' ')
    print()'''

# full pyramid
'''n = 5
k = 1 # print *
i = 1
while i <= n:
    # print space
    b = 1
    while b <= n-i:
        print(' ',end=' ')
        b += 1
    j = 1
    # print *
    while j <= k:
        print('*',end=' ')
        j += 1
    k = k + 2 # increase * by 2
    print()
    i = i + 1'''

# iterate dictionary 
'''d = {1:'a', 2:'b',3:'c'}
for i,j in d.items():
    print(i,j)
# for i in d:
#     print(i,d[i])'''

# check key is present in dictionary or not
'''# for i in d1:
#     if 'a1' == i:
#         print('matckes')
#         break
#     else:
#         print('not matches')
#         break
d1 = {'a1':1, 'b':2}
if 'a1' in d1:
    print('present') 
else:
    print('not present')'''

# marge two dictionary
'''d1 = {'a':1, 'b':2}
d2 = {'b':2, 'c':3}
# print(d1 | d2)
# print({**d1, **d2})
d3 = d2.copy()
d3.update(d1)
print(d3)'''

# concate two list
'''l1 = [1, 'a',3]
l2 = [3, 4, 5]
# print(l1 + l2)
# print(*l1, *l2)
# print( list ( set ( l1 + l2 ) ) ) # unique value
l1.extend(l2)
print(l1) '''

# Split a List Into Evenly Sized Chunks
'''l = [1,2,3,4,5,6,7,8,9]
def split(l):
    for i in range(0,len(l)):
        yield(l[i:i+2])
print(list(split(l)))'''

# reverse string
'''str = 'nitesh'
for i in range((len(str)-1),-1,-1):
    print(str[i])'''

# enumerate
'''l = [11,22,33,44]
for i in range(len(l)):
    print(i, l[i])
# print(tuple(enumerate(l,start=1)))'''

# flattern a nasted list 
'''l = [[1], 
    [2, 3],
    [4, 5, 6, 7]]
li = []
for i in l:
    for j in i:
        li.append(j)
# li = [j for i in l for j in i]
print(li)'''

# check is list empty
'''l = [11,22,33,44]
# li = []
# if l == li:
#     print(True)
# else:
    # print(False)
if not l:
    print(True)
else:
    print(False)'''

# colored output 
'''print('\x1b[38;2;5;86;243m' + 'Programiz' + '\x1b[0m')
from termcolor import colored
print(colored('Programiz', 'red'))'''

# Convert Two Lists Into a Dictionary
'''l1 = [2,3]
l2 = [22,33,44]
print(dict((zip(l1,l2))))'''

# remove whitespace 
'''str = 'nitesh    sahu   love               programming'
strr = ' '.join(str.split())
print(strr)'''

# reverse number
'''n = 2345
rn = 0
while n!=0:
    r = n % 10
    rn = rn * 10 + r
    n = n // 10
print(rn)'''

str = 'sahu'

# timer
# permutation of a string