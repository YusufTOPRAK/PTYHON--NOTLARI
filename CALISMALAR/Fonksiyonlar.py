# method (metod)  class içinde tanımlanır.

# list = [1,2,3]  # class => list
#
# list.append(4) # append => method
# list.pop()     # pop => method
# print(list)
#
# print(type(list))
#
# a = 'Yusuf'       # class => str
# print(a.upper())  # upper => method
#
# print(type(a))



# functions (fonksiyonlar)
# def sayHello(name = ' User'):
#     print('Hello' + name)
#
# sayHello(' Yusuf')
# sayHello(' Ali')
# sayHello(' Veli')
# sayHello()



# def sayHello(name, surname):
#     return 'Hello' + name + surname
#
# msg = sayHello(' Yusuf', ' TOPRAK')
# print(msg)


# def total(num1, num2):
#     return num1 + num2
#
# a = total(10, 20)
# print(a)


# def yasHesapla(dogumyili):
#     return 2021 - dogumyili

# age = yasHesapla(19)
# print(age)


# def yasHesapla(dogumyili):
#     return 2021 - dogumyili
#
# def EmekliligeKacYilKaldi(dogumYili, isim):
#     '''
#     DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
#     INPUT: Dogum yili
#     OUTPUT: Hesaplanan yil bilgisi
#     '''
#     yas = yasHesapla(dogumYili)
#     emeklilik = 65 - yas
#
#     if emeklilik > 0:
#         print(f'Sayın {isim} emekliliğinize {emeklilik} yıl kaldı.')
#     else:
#         print('Zaten emeklisiniz.')
#
# EmekliligeKacYilKaldi(2002, 'Yusuf TOPRAK')
#
# print(help(EmekliligeKacYilKaldi))


#help kullanımı
# list1 = [1,2,3]
# print(help(list1.sort))


# function parameters (fonksiyon parametreleri)
# def change(n):
#     n[0] = 'İstanbul'
#
# sehirler = ['İzmir', 'Ankara']
#
# change(sehirler)
# print(sehirler)

# def change(n):
#     n[0] = 'İstanbul'
#
# sehirler = ['İzmir', 'Ankara']
#
# change(sehirler[:])       #slicing Bu işlemle kopyaladık ve 0. elemanı değiştirmedi
# print(sehirler)


# def add(*params):
#     return sum((params))   #sum toplama yapan bir fonksiyondur..
#
# print(add(10, 20))
# print(add(10, 20, 30))
# print(add(10, 20, 40, 50, 100, 25, 89))
# #ALTERNATİFİ
# def num(*params):
#     total = 1
#     for x in params:
#         total *= x
#     return total
# print(num(1,2,3,4,5,6,7,8,9))

# def add(*params):
#     sum = 0
#     for x in params:
#         sum += x
#     return sum
#
# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,40,50,100,25,89))


# def displayUser(**args):
#     for key, value in args.items():
#         print(key, value)
#
# displayUser(name='Yusuf', age=19 , city='Kayseri')
# displayUser(name='Ali', age=22, city='İstanbul', phone=146589465)

# def myFunc(a, b, *args, **kwargs):
#     print(a)
#     print(type(a))
#     print(b)
#     print(args)
#     print(type(args))
#     print(kwargs)
#     print(type(kwargs))
#
# myFunc(10, 20, 30, 40, 50, 70, 80, key1='value1', key2='value2')


#1) Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yaz.
#eğitmenin yaptığı
# def yazdir(kelime, adet):
#     print(kelime*adet)
# yazdir('Yusuf\n', 4)

#benim yaptığım
# def say():
#     kelime = input('Kelimeyi girin: ')
#     adet = int(input('Kaç kez yazdırılsın?: '))
#     i = 0
#     while i < adet:
#         print(kelime)
#         i += 1
# print(say())

#2) Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon yaz.
#eğitmenin yaptığı
# def listeyeCevir(*params):
#     liste = []
#     for i in params:
#         liste.append(i)
#     return liste
# print(listeyeCevir(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,32))

#benim yaptığım
# def unlimited():
#     liste = []
#     kac = int(input('Kaç sayı girmek istiyorsunuz?: '))
#     i = 0
#     while i < kac:
#         adet = (int(input('Sayı gir: ')))
#         i += 1
#         liste.append(adet)
#     print(liste)
# print(unlimited())


#3) Gönderilen 2 sayı arasındaki tüm asal sayıları bul.
# def asalSayilariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if sayi%i == 0:
#                     break
#             else:
#                 print(sayi)
# sayi1 = int(input('1.sayıyı gir: '))
# sayi2 = int(input('2.sayıyı gir: '))
# asalSayilariBul(sayi1, sayi2)

#4) Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür.
# def tamBolenleriniBul(sayi):
#     liste = []
#     for i in range(2, sayi):
#         print(i)
#         if sayi%i == 0:
#             liste.append(i)
#     return liste
# print(tamBolenleriniBul(10))


#map kullanımı
# def square(num): return num**2
#
# numbers = [2,3,4,5,6,7]
# print(set(map(square, numbers)))
# #alternative
# for x in map(square, numbers):
#     print(x)

# lambda expression(ifadeleri) kullanımı
# number = [2,3,4,5,6,7]
# # def square(num): return num**2   #karşılaştırmak için yazdım.
# print(list(map(lambda num: num**2, number)))
#
# square = lambda num: num**2
# print(list(map(square, number)))
#
# square = lambda num: num**2
# print(square(14805))


#global ve local variables(global ve local değişkenler)
#global scope
# x = 'global x'
#
# def function():
#     #local scope
#     x = 'local x'
#     print(x)
# function()
# print(x)

#global
# name = 'Yusuf'
#
# def changeName(new_name):
#     #local
#     name = new_name
#     print(name)
# changeName('Ali')
# print(name)

# name = ' global string'
#
# def greeting():
#     name = ' Ali'
#     print(name)
#
#     def hello():
#         name = ' Yusuf'
#         print(name)
#     hello()
# greeting()
# print(name)


# x = 50                     # global olarak tanımlanan x'i fonksiyon
# def test():                # içinde değiştirmek
#     global x
#     print(f'x: {x}')
#
#     x = 100
#     print(f'changed x to: {x}')
# test()
# print(x)

# x = 'global x'
#
# def func1():
#     x = 'enclosing x'
#     print(x)
#
#     def func2():
#         nonlocal x
#         x = 'local x'
#     func2()
#     print(x)
# func1()
# print(x)


#Bankamatik Uygulaması:
# YusufHesap = {
#     'Ad': 'Yusuf TOPRAK',
#     'HesapNo': '123456789',
#     'Bakiye': 3000,
#     'EkHesap': 2000
# }
#
# AliHesap = {
#     'Ad': 'Ali Veli',
#     'HesapNo': '123456789',
#     'Bakiye': 2000,
#     'EkHesap': 1000
# }
#
# hello = print(f"Merhaba {YusufHesap['Ad']}")
# def paraCekme(hesap, miktar):
#     global hello
#
#     if hesap['Bakiye'] >= miktar:
#         kalan = hesap['Bakiye'] - miktar
#         print(f"İşleminiz tamamlanmıştır. Bakiyenizde {kalan} TL kaldı.")
#     else:
#         sor1 = (input(f"Bakiyenizde {hesap['Bakiye']} TL bulunmaktadır. Ek hesabınızdan para çekmek ister misiniz?(Evet/Hayır): "))
#         if sor1 == 'Evet':
#             miktar2 = int(input(f"Ek hesabınızda {hesap['EkHesap']} TL bulunmaktadır. Ne kadar para çekmek istiyorsunuz?: "))
#
#             if hesap['EkHesap'] >= miktar2:
#                 kalan2 = hesap['EkHesap'] - miktar2
#                 print(f"İşleminiz tamamlanmıştır. Ek hesabınızda {kalan2} TL kalmıştır.")
#             else:
#                 print(f"İşleminiz tamamlanamamıştır. Ek hesabınızda yeterli TL bulunmamaktadır.")
#
#         else:
#             print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} TL bulunmaktadır.")
#             print(f"Ek hesabınızda {hesap['EkHesap']} TL bulunmaktadır.")
#
#
# miktar = int(input('Çekmek istediğiniz para miktarını giriniz: '))
# paraCekme(YusufHesap, miktar)