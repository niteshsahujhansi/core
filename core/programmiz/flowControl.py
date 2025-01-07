'''In this program, we input a number
check if the number is positive or
negative or zero and display
an appropriate message
This time we use nested if statement'''

# using nested if 
'''num = float(input('Enter a number: '))
if num >=0:
    if num == 0:
        print('zero')
    else:
        print('positive')
else:
    print('negative')'''

# using elseif 
'''num = float(input('Enter a number'))
if num > 0:
    print('positive')
elif num == 0:
    print('zero')
else:
    print('negative')'''

# for loop
'''numbers = [1,3,2]
sum = 0
for var in numbers:
    sum = sum + var 
print(sum)'''

'''print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))'''

'''genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
    print('I like', genre[i])'''

'''student = 'radha'
marks = {'ram': 10, 'shyam': 20, 'radha': 30}
for i in marks:
    if i == student:
        print(marks[student])
        break
else:
    print('Data does not exist.')'''

# while loop
'''num = 5
i = 1
sum = 0
while(i<=num):
    sum = sum + i
    i = i + 1
print(sum)'''

'''student = 'ram'
marks = {'ram': 10, 'shyam': 20, 'radha': 30}

while(student in marks):
    print(marks[student])
    break
else:
    print('Data does not exist.')'''

# break & continue & pass
'''for val in 'string':
    if val == 'i':
        continue
    print(val)
print('the end')

for val in 'string':
    if val == 'i':
        break
    print(val)
print('the end')'''

'''pass is just a placeholder for
functionality to be added later.

for val in sequence:
    pass'''

