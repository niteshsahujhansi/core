import random

# def  rock_paper_scissor()








player_1 = {0:'roak', 1:'paper', 2:'scissor'}
player_2 = {0:'roak', 1:'paper', 2:'scissor'}

# num_1 = input('player one, Enter your choise: ')
num_1 = str(random.randint(111,999))
print(num_1)
# num_2 = input('player two, Enter your choise: ')
num_2 = str(random.randint(111,999))
print(num_2)
bit_1 = int(input('player one, Enter the secret bit position'))
bit_2 = int(input('player two, Enter the secret bit position'))

p1 = int(num_1[bit_1])
p2 = int(num_2[bit_2])

print(p1)
print(p2)
