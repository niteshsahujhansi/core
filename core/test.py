# def s(arr):
#     if len(arr) == 1:
#         return 1
#     else:
#         return arr[0] + s(arr[1:])

# print(s([1,2,4]))

# lst1 = ['c', 'a', 'r']
# lst2 = ['p', 'e', 't']

# res1 = (zip(lst1, lst2) == lst1 + lst2 )
# res2 = (lst1.extend(lst2) == lst1 + lst2)

# print(res1, res2)

# d = {1:'one', 2:'two', 3:'three'}
# print(d.get(4,'Four')) 

# d = {'a':1, 'b':2, 'c':3}

# l = [2,4,6,8]
# l.remove(d['b'])

# print(l)

# list1 = ['c','a', 'r']
# list2 = ['p', 'e', 't']

# res = zip(list1, list2)

# print(res)

# dic = {'a':1, 'b':2, 'c':3}
# result = ''
# for d in dic:
#     result += str(d)
# print(result)

# d = {'a':1, 'b':2, 'c':3}
# l = [2,4,6,8]

# l.remove(d['b'])
# print(d)

# l1 = [1,3,5,7,9, 10, 13]
# l2 = [2,4,6,8, 22]
# l = l1+l2
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i] < l[j]:
#             l[i], l[j] = l[j], l[i] 
# print(l)

# arr = [1, 2, 3, 4]
# S = 0
# N = 4

# r,l = 0,0
# c_s = 0

# while(r<N):
#     c_s += arr[r]
#     while(c_s>S):
#         c_s -= arr[l]
#         l+=1
#     if c_s == S:
#         print(l+1,r+1)
#         break 
#     r+=1

# def MissingNumber(self,array,n):
#         array_set = set(array)
#         complete_set = set(range(1, n+1))
#         missing = complete_set - array_set
#         return missing.pop()




