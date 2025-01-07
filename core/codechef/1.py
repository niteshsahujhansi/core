# t =int(input())
# for i in range(t):
#     x,y,a = map(int,(input().split()))
#     if (a >= x) & (a < y) :
#         print('Yes')
#     else:
#         print('No')

# t =int(input())
# for i in range(t):
#     x,y = map(int,(input().split()))
#     if x>=y:
#         print(x-y)
#     else:
#         a=0
#         print(a)

# t =int(input())
# for _ in range(t):
#     n,x = map(int,(input().split()))
#     if n%6 == 0:
#         no_of_sub = n//6
#     else:
#         no_of_sub = (n//6) + 1

#     total_cost = no_of_sub * x
#     print(total_cost)

# t =int(input())
# for _ in range(t):
#     a,b = map(int,(input().split()))
#     while(a<b):
#         if a%2 != 0:
#             a = a+1
#             print(a)
#         else:
#             a = a+2
#             print(a)
#     if a == b:
#         print('yes')
    
#     elif a>b:
#         print('no')

'''# testCases = int(input())
# testCases = 3
# length, x = map(int, (input().split()))
length, x = 4,1
# list = []
# li = [2,1,3,4]
li = [1,2,3,4]
# li = [3,2,2,3,3]
# list = [int(item) for item in input().split()]
print(li)
# li.sort()
for i in range(0, len(li)):
    for j in range(i+1, len(li)):
        if li[i]>li[j]:
            output = 'a'
            if li[i] + li[j] <= x:
                output = 'yes'
                li[i], li[j] = li[j], li[i]
            else:
                output = 'no'
                break 
        else:
            output='yes'
print(li)
print(output)'''

'''def revsort(li, length, x):
    for i in range(length-1):
        if li[i] > li[i+1]:
            if li[i] + li[i+1] > x:
                return False
            else:
                li[i], li[i+1] = li[i+1], li[i]
    return True

testCases = int(input())
for _ in range(testCases):
    length, x = map(int, (input().split()))
    li = [int(item) for item in input().split()]

    if revsort(li, length, x):
        print('yes')
    else:
        print('no')'''

'''t = int(input())
for _ in range(t):
    p = int(input())
    
    if p <= 1000:

        rem = p//100
        p = p%100
        if p < 10:
            output = rem + p 
        elif p == 10:
            output = 10
        else:
            output = -1
    else:
        output = -1
    print(output)'''

'''from math import gcd
t = int(input())
for i in range(t):
    n = int(input())
    v = [int(i) for i in input().split()]
    pgcd = [None] * n
    pgcd[0] = v[0]
    for i in range(1, n):
        pgcd[i] = gcd(pgcd[i-1], v[i])
    sgcd = [None] * n 
    sgcd[n-1] = v[n-1]
    for i in range(n-2, -1, -1):
        sgcd[i] = gcd(sgcd[i+1], v[i])

    se = 0
    for i in range(n):
        if (i==0) and (sgcd[1]>1) :
            se += 1
        elif (i==n-1) and (pgcd[n-2]>1) :
            se += 1
        
        elif (gcd( pgcd[i-1], sgcd[i] ) > 1) :
            se += 1
    print(se)
'''