'''enumerate()'''
# grocery = ['bread', 'milk', 'butter']
# for count, item in enumerate(grocery):
#   print(count, item)

'''filter()'''
# letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# def filter_vowels(letter):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     return True if letter in vowels else False

# filtered_vowels = filter(filter_vowels, letters)
# vowels = tuple(filtered_vowels)
# print(vowels)

'''map()'''
# numbers = [2, 4, 6, 8, 10]

# def square(number):
#   return number * number

# squared_numbers_iterator = map(square, numbers)
# squared_numbers = list(squared_numbers_iterator)
# print(squared_numbers)

# num1 = [4, 5, 6]
# num2 = [5, 6, 7]
# result = map(lambda n1, n2: n1+n2, num1, num2)
# print(list(result))

'''zip()'''
# languages = ['Java', 'Python', 'JavaScript']
# versions = [14, 3, 6]
# result = zip(languages, versions)
# print(list(result))

# numbersList = [1, 2, 3]
# str_list = ['one', 'two']
# numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')
# result = zip(numbersList, str_list, numbers_tuple)
# result_set = list(result)
# print(result_set)

'''reduce'''



