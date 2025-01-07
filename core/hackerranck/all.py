# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

'''n = int(input())
if n % 2 != 0:
    print('weird')
else:
    if n in range(2,5):
        print('not weird')
    if n in range(6,21):  # why 21 here
        print('weird')
    if n > 20:
        print('not weird')'''


# permutation of i, j, k
'''x = 2
y = 1
z = 3
n = 3
li = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k == n:
                continue
            else:
                li.append([i,j,k])
for i in li:
    print(i)'''

# second largest 
'''n = 5
arr = [2,3,6,6,5]
# arr = list(arr)
arr.sort()
print(arr)
largest = arr[0]
s_largest = arr[0]
for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]
for i in range(len(arr)):
    if arr[i] != largest and arr[i] > s_largest:
        s_largest = arr[i] 
print(s_largest)'''


'''# noOfStudent = int(input('Enter the number of Student: '))
# for i in range(noOfStudent):
#     name = input('Enter student name: ')
#     score = float(input('enter score: '))

# noOfStudent = 3
# row, col = 0, 0
# li = []
# for i in range(noOfStudent):
#     col = []
#     for j in range(i):
#         col.append(input('Enter name: '))
#         col.append(int(input('Enter score: ')))
#     li.append(col)
# print(li)
# li.sort()
# print(li)'''

'''# n = int(input())
n = 3
# student_marks = {}
student_marks = {'ram': [], 'shyam': [3.0, 4.0], 'radhan': [4.0, 5.0, 6.0, 7.0]}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()

for i in student_marks:
    p = student_marks['shyam']
    print(p)
    break
pp = 0 
for i in range(len(p)):
    pp += p[i]
print(pp/len(p))'''

'''N = int(input())
l =[]
for i in range(N):
    s = input().split()

    for j in range(1,len(s)):
        s[j] = int(s[j])
    
    if s[0] == 'insert':
        l.insert(s[1], s[2])
    
    elif s[0] == 'remove':
        l.remove(s[1])
    
    elif s[0] == 'append':
        l.append(s[1])
    
    elif s[0] == 'sort':
        l.sort()
    
    elif s[0] == 'pop':
        l.pop()
    
    elif s[0] == 'reverse':
        l.reverse()
    
    elif s[0] == 'print':
        print(l)'''

