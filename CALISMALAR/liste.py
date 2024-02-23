#List

# my_list = [1,'s',True,5.4]
# print(my_list)

# list1 = ['one','two','three']
# list2 = ['four','five','six']
# numbers = list1 + list2
# print(numbers)
# print(len(numbers))
# print(numbers[4])

# userA = ['Yusuf',19]
# userB = ['Ali',14]
# users = [userA, userB] # liste içinde liste oluşturduk
# print(users)
# print(users[1][1])
# print(users[0][0])
#
# numbers = [-5,1,45,321,5,9,78,156,75412,9,21]
# letters = ['d','f','e','z','a','g','e','i','w','l']
#
# print(max(numbers))
# print(min(numbers))
# print(min(letters))
# print(max(letters))
#
# print(numbers[3:6])
# print(numbers[:6])
#
# numbers[1] = 54
# print(numbers)
#
# numbers.append(46)
# print(numbers)

# a = ['1','2','3','4','5','6','7','8']
# a.insert(5,5.5)
# print(a)

# numbers.pop(6)
# print(numbers)
#
# numbers.remove(21)
# print(numbers)
#
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
#
# letters.sort()
# print(letters)
# letters.reverse()
# print(letters)
#
# print(numbers.count(9))
# print(letters.count('j'))
#
# numbers.clear()
# print(numbers)



#Tuple

# tuple = ('Yusuf',1,True)
# print(type(tuple))
# print(tuple)
#
# a = ('Ali','Namık','Lale')
# b = ('İsmet','Kemal','Şükrü')
# names = a + b
# print(names)
#
# print(names[2])
#
# print(names.count('Namık'))
# print(names.index('Kemal'))


#Dictionary
# a = {'Name':'Yusuf',
#     'Surname':'TOPRAK',
#     'Age':19,
#      }

# print(a['Age'])

# a['Wight'] = 75
# print(a)
#
# a['Name'] = 'Ali'
# print(a)
#
# b = {'Yusuf TOPRAK':{
#      'Age': 19,
#      'email':'sdsadad',
# 'Address': ['Kayseri','Talas'],
#      'Roles':['Admin','User']
# },
#      'Ali TOPRAK':{
#      'Age': 10,
#      'email':'sdsadad',
#      'Address': {'Konya','Talas'}
# }
#
#       }
# print(b['Yusuf TOPRAK']['Roles'][0])
# print(b['Ali TOPRAK']['email'])
#
# b['Yusuf TOPRAK']['Color'] = 'Black'
# print(b)

#SET
# fruits = {'orange','banana','apple','watermelon'}
# print(fruits)
#
# # print(fruits[2]) set indekslenemez
#
# for x in fruits:
#     print(x)
#
# fruits.add('cherry')
# print(fruits)
#
# fruits.update(['mango','grape'])
# print(fruits)
#
# fruits.update(['apple','cherry'])
# print(fruits)
#
# fruits.remove('apple')
# fruits.discard('apple')  #HEPSİ SİLER
# fruits.pop()
# print(fruits)
#
# fruits.clear()
# print(fruits)

# myList = [1,2,3,4,5,6,1,2,3,4,5,6]
# print(myList)
# myList = (set(myList))
# print(myList)

# # Value&Reference Types
# # valu types => str , number(int, float)
# x = 5
# y = 25
#
# x = y
#
# y = 10
# # print(x,y)
#
# #reference types => list
# a = ['apple','banana']
# b = ['apple','banana']
#
# a = b
# b[0] = 'grape'
# print(a,b)
