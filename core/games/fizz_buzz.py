n = 30
for i in range(n):
    if (i % 15 == 0):
        print('fizz buzz')
        continue
    elif (i % 3 == 0):
        print('fizz')
        continue
    elif (i % 5 == 0):
        print('buzz')
        continue
    else:
        print(i)