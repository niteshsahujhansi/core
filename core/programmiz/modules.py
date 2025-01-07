import itertools

# iteartors 
'''numbers=[1,4,9]
# value = numbers.__iter__()
value = iter(numbers)
# item1 = value.__next__()
item1 = next(value)
print(item1)
# item2 = value.__next__()
item2 = next(value)
print(item2)
# item3 = value.__next__()
item3 = next(value)
print(item3)'''

counter = itertools.count()

'''print(next(counter))
print(next(counter))
print(next(counter))'''

'''for num in counter:
    print(num)'''

data = [100, 200, 300, 400]
'''daily_data = list(zip(itertools.count(1, 2), data))
print(daily_data)'''


