''' find second larest no from a list '''
# l = [1,3,8,3,5,9,9,9]
# l = sorted(l)

# larest = l[-1]

# for i in l[::-1]:
#     if i != larest:
#         sl = i 
#         break

# print(sl)

# print(list(set(l))[-2])

'''print max version'''
# s = '10.29.39 11.22.33'
# sl = s.split()
# print(max(sl[0], sl[1]))


# l = [((11,22), (33,44))]

'''date formate change'''
# import datetime 
# today_date = datetime.datetime.now()
# today_date = datetime.date.today()
# print(today_date)
# today_date = datetime.datetime.strftime(today_date, '%d-%m-%Y')

'''timer'''
# import time

# def countdown(t):
	
# 	while t:
# 		mins, secs = divmod(t, 60)
# 		timer = '{:02d}:{:02d}'.format(mins, secs)
# 		print(timer, end="\r")
# 		time.sleep(1)
# 		t -= 1
	
# 	print('Done')
	
# t = input("Enter the time in seconds: ")
# countdown(int(t))


'''shuffle list'''
# l = ['nitesh', 'sahu', 'uma', 'shankar', 'sahu']
# import random
# random.shuffle(l)
# print(l)

'''flatten list'''

# def f(l):
#     fl = []
#     for i in l:
#         if isinstance(i, list):
#             fl.extend(f(i))
#         else:
#             fl.append(i)
#     return fl

# l = [4,3,[2,[3,4,[1,2,3,4]]]]
# ll = f(l)
# print(ll)

'''brackets balanced or not'''

# def bal(s):
#     stack = []
#     for i in s:
#         if i in '({[':
#             stack.append(i)
#         elif i==')':
#             if not stack or stack[-1] != '(':
#                 return False
#             stack.pop()
#         elif i=='}':
#             if not stack or stack[-1] != '{':
#                 return False
#             stack.pop()
#         elif i==']':
#             if not stack or stack[-1] != '[':
#                 return False
#             stack.pop()
#     return not stack

# s = input('stack value:- ')
# if bal(s):
#     print('Balance')
# else:
#     print('Not Balance')

'''reverseWords'''
# def reverseWords(s):
#         sl = s.split('.')
#         rsl = sl[::-1]
#         srsl = ".".join(rsl)
#         return srsl

# s = 'i.like.this.program.very.much'
# print(reverseWords(s))


# def isValid(s):
#     #code here
#     s = str(s).split('.')
#     if len(s) > 4:
#         return 0
#     for i in s:
#         if not i.isdigit() or int(i) > 255:
#             return 0
#     else:
#         return 1
    
# s = '0000.0000.0000.0000'
# if isValid(s):
#     print('y')
# else:
#     print('n')



# s = 'iabccaghjytmdda'
# checked_s = []
# sub_string = ''
# l = len(s)

# ii = 0

# while s != "":

#     for i in range(l-1):
#         sub_string += s[i]
#         if s[i+1] in sub_string:
#             checked_s.append(sub_string)
#             ii = i
#             continue
        
#             s = s[ii:]

# print(checked_s)
# print(sub_string)

def length_of_longest_substring(s):
    n = len(s)
    max_length = 0
    start = 0
    char_index = {}

    for end in range(n):
        if s[end] in char_index and start <= char_index[s[end]]:
            start = char_index[s[end]] + 1
        else:
            max_length = max(max_length, end - start + 1)

        char_index[s[end]] = end

    return max_length


# Example usage:
input_string = input("Enter a string: ")
result = length_of_longest_substring(input_string)
print("The length of the longest substring without repeating characters is:", result)



