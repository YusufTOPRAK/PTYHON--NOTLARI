# def greeting(name):
#     print('Hello', name)
# print(greeting('Yusuf'))
# print(greeting)
# sayHello = greeting
# print(sayHello)
# print(greeting)
# print(greeting('Ali'))
# print(sayHello('Ali'))
# del sayHello
# print(greeting)
# print(sayHello)

# # encapsulation
# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)
#
# outer(10)


# def factorial(number):
#     if not isinstance(number, int):
#         raise TypeError('number must be an integer.')
#     if not number >=0:
#         raise ValueError('number must be zero or positive.')
#
#     def inner_factorial(number):
#         if number <= 1:
#             return 1
#         return number* inner_factorial(number-1)
#     return inner_factorial(number)
# try:
#     print(factorial('5'))
# except Exception as err:
#     print(err)

# def usalma(number):
#
#     def inner(power):
#         return number ** power
#
#     return inner
#
# two = usalma(2)
# print(two(3))

# def yetki_sorgula(page):
#     def inner(role):
#         if role == 'Admin':
#             return '{0} rolü {1} sayfasına ulaşabilir.'.format(role, page)
#         else:
#             return '{0} rolü {1} sayfasına ulaşamaz.'.format(role, page)
#     return inner
#
# user = yetki_sorgula('Produc Edit')
# print(user('Admin'))

# def islem(islem_adı):
#
#     def toplama(*args):
#         toplam = 0
#         for i in args:
#             toplam += i
#         return toplam
#
#     def carpma(*args):
#         carp = 1
#         for i in args:
#             carp *= i
#         return carp
#
#     def cıkarma(first, *args):
#         toplam = first
#         for i in args:
#             toplam -= i
#         return toplam
#
#     if islem_adı == 'Toplama':
#         return toplama
#     elif islem_adı == 'Çarpma':
#         return carpma
#     else:
#         return cıkarma
#
# islem1 = islem('Çıkarma')
# print(islem1(-15,-7))

# def toplama(a,b):
#     return a+b
# def cıkarma(a,b):
#     return a-b
# def carpma(a,b):
#     return a*b
# def bolme(a,b):
#     return a/b
#
# def islem(f1, f2, f3, f4, islem_adı):
#     if islem_adı == 'toplama':
#         print(f1(2,3))
#     elif islem_adı == 'cıkarma':
#         print(f2(5,2))
#     elif islem_adı == 'carpma':
#         print(f3(5,6))
#     elif islem_adı == 'bolme':
#         print(f4(18,3))
#     else:
#         print('Geçersiz işlem.')
#
# islem(toplama, cıkarma, carpma, bolme, 'toplama')
# islem(toplama, cıkarma, carpma, bolme, 'cıkarma')
# islem(toplama, cıkarma, carpma, bolme, 'carpma')
# islem(toplama, cıkarma, carpma, bolme, 'bolme')
# islem(toplama, cıkarma, carpma, bolme, 'yok')


## decorator fonctions
# def my_decorator(func):
#     def wrapper(name):
#         print('Process before the function')
#         func(name) # ==> Buraya direkt Yusuf da yazabilirsin wraper ve sayHello'ya parametre vermeyerek.
#         print('Process after the function')
#     return wrapper
#
# # ASIL YAPTIĞIM ŞEY
# # def sayHello():
# #     print('Hello')
# # sayHello = my_decorator(sayHello)
# # sayHello()
#
# @my_decorator
# def sayHello(name):
#     print('Hello', name)
# sayHello('Yusuf')

# import math
# import time
#
# def calculate_time(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         time.sleep(1)
#         func(*args, **kwargs)
#         finish = time.time()
#         print(f'Fonksiyon {finish - start} sürede çalıştırıldı.')
#     return inner
#
# @calculate_time
# def usalama(a,b):
#     print(math.pow(a,b))
#
# @calculate_time
# def factorial(x):
#     print(math.factorial(x))
#
# usalama(2,3)
# factorial(8)

#### ITERATORS ####
# liste = [1,2,3,4,5]

# iterator = iter(liste)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# liste = [1,2,3,4,5]
#
# iterator = iter(liste)
#
# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break



# class MyNumbers:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start <= self.stop:
#             x = self.start
#             self.start += 1
#             return x
#         else:
#             raise StopIteration
#
# count = MyNumbers(0,10)
#
# iterator = iter(count)
# while True:
#     try:
#         element = next(count)
#         print(element)
#     except StopIteration:
#         break

# for i in count:
#     print(i)

### GENERATORS ###
# def cube():
#     for i in range(5):
#         yield i**3
# for i in cube():
#     print(i)

# liste = (i**3 for i in range(5))
# print(liste)

# print(next(iter(liste)))
# for i in liste:
#     print(i)
