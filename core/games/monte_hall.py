import random
'''swap = 0
dont_swap = 0
doors = [0]*3
goatDoor = [0]*2

x = random.randint(0,2)
doors[x] = 'BMW'
for i in range(0,3):
    if i == x:
        continue
    else:
        doors[i] = 'Goat'
        goatDoor.append(i)

choice = int(input('Enter your choise out of 0,1 or 2 : '))

door_open = random.choice(goatDoor)
while door_open == choice:
    door_open = random.choice(goatDoor)

ch = input('Do you want to swap? y/n ')
if ch == 'y':
    if doors[choice] == 'Goat':
        print('player wins')
        swap += 1
    else:
        print('player lost')
else:
    if doors[choice] == 'Goat':
        print('player lost')
    else:
        print('player wins')
        dont_swap += 1

# print(door_open)
# print(doors)
# print(goatDoor)'''

swap = 0
swaps = 0
dont_swap = 0
dont_swaps = 0
doors = [0]*3
goatDoor = [0]*2
j = 0
while(j<5):
    x = random.randint(0,2)
    doors[x] = 'BMW'
    for i in range(0,3):
        if i == x:
            continue
        else:
            doors[i] = 'Goat'
            goatDoor.append(i)

    # choice = int(input('Enter your choise out of 0,1 or 2 : '))
    choice = random.randint(0,2)


    door_open = random.choice(goatDoor)
    while door_open == choice:
        door_open = random.choice(goatDoor)

    # ch = input('Do you want to swap? y/n ')
    ch = random.choice(['y','n'])
    if ch == 'y':
        swaps += 1
        if doors[choice] == 'Goat':
            print('player wins')
            swap += 1
        else:
            print('player lost')
    else:
        dont_swaps += 1
        if doors[choice] == 'Goat':
            print('player lost')
        else:
            print('player wins')
            dont_swap += 1
    j += 1
# print(door_open)
# print(doors)
# print(goatDoor)

print('no of swaps: ',swaps,'no of win: ',swap )
print('no of dont_swaps: ',dont_swaps, 'no of wins: ',dont_swap)
