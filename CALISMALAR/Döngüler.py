# Loop of for (for Döngüsü)

# numbers = [1,2,3,4,5,6]
#
# for x in numbers:
#     print(x)

# name = ['Yusuf', 'Ali', 'Akif']
#
# for y in name:
#     print(f'My name is {y}')

# name = 'Yusuf TOPRAK'
#
# for ad in name:
#     print(ad)


# tuple = [(1,2),(3,4),(5,6)]
#
# for x,z in tuple:
#     print(z,x)


# dc = {'K1':1, 'K2':2, 'K3':3}
# print(len(dc))
# for x in dc.items():
#     print(x)

# sayilar = [1,3,5,7,9,12,19,21]

#1 sayilar listesindeki hangi sayılar 3'ün katıdır?
# for x in sayilar:
#     if (x%3 == 0):
#         print(x)

#2 sayılar listesinde sayıların toplamı kaçtır?
# toplam = 0
# for x in sayilar:
#     toplam +=  x
# print(toplam)

#3 sayılar listesindeki tek sayıların karesini al
# for x in sayilar:
#     if (x%2 == 1):
#         print(x**2)


# sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

#4 Şehirlerden hangileri en fazla 5 karakterlidir.
# for x in sehirler:
#     if (len(x)<=5):
#         print(x)

# urunler = [
#     {'name':'samsung S6', 'price':'3000'},
#     {'name':'samsung S7', 'price':'4000'},
#     {'name':'samsung S8', 'price':'5000'},
#     {'name':'samsung S9', 'price':'6000'},
#     {'name':'samsung S10','price':'6000'}
# ]

#5 Ürünlerin fiyatları toplamı nedir?
# total = 0
# for x in urunler:
#     price=int(x['price'])
#     total += price
# print(total)

#6 Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.
# for x in urunler:
#     if (int(x['price'])) <= 5000:
#         print(x['name'])


# Loop of while (while döngüsü)
# x = 0
# while x<=50:
#     if x%2==1:
#         print(f'Tek sayılar:{x}')
#     else:
#         print(f'Çift sayılar:{x}')
#     x += 1


# name = '' #False
# while not name.strip():
#     name = input('İsim:')
# print(f'Merhaba {name}')

# sayilar = [1,3,5,7,9,12,19,21]

#1 sayilar listesini while ile ekrana yazdır.

# i = 0
# while i < len(sayilar):
#     print(i)
#     i += 1


#2 Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#  tek sayıları ekrana yazdır.

# first = int(input('Başlangıç Değeri:'))
# end = int(input('Bitiş Değeri:'))
# i = first
#
# while i < end:
#     if i % 2 == 1:
#         print(i)
#     i += 1


#3 1-100 arasındaki sayıları azalan şekilde yazdırın.

# i = 100
# while i > 0:
#     print(i)
#     i -= 1

#4 Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdır.

# numbers = []
# i = 0
#
# while i < 5:
#     n=int(input('Sayı gir:'))
#     numbers.append(n)
#     i += 1
#
# numbers.sort()
# print(numbers)


#5 Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesinde sakla
#  NOT: ürün sayısını kullanıcıya sorun
#  NOT: dictionary listesi yapısı (name, price) şeklinde olsun
#  NOT: ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listele.

# urun = []
#
# adet = int(input('Kaç ürün girmek istiyorsunuz?:'))
#
# i = 0
# while i < adet:
#     ad = input('Ürün Adı:')
#     fiyat = float(input('Ürün Fiyatı:'))
#     urun.append({
#         'Ürün Adı':ad,
#         'Ürün Fiyatı':fiyat
# })
#     i += 1
#
# for x in urun:
#     print(f"Ürün Adı:{x['Ürün Adı']} Ürün Fiyatı: {x['Ürün Fiyatı']} ")

#break
# i = 0
# while i < 11:
#     if i== 5:
#         break
#     print(i)
#     i += 1

#continue
# i = 0
# while i < 11:
#     i += 1
#     if i == 5:
#         continue
#     print(i)


# 1-100'e kadar tek sayıların toplamı?
# total = 0
# i = 0
# while i <= 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     total += i
# print(total)


#range
# for x in range(10,100,15):
#     print(x)
#
# print(list(range(10,20,2)))


#enumerate(numaralandırmak)
# a = 'Yusuf TOPRAK'

# for x in enumerate(a):
#     print(x)

#zip
# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# list3 = ['+','-','*','/','%']
# print(list(zip(list1,list2,list3)))
#
# for x in zip(list1,list2,list3):
#     print(x)
#
# for x,y,z in zip(list1,list2,list3):
#     print(x,y,z)


# list Comprehensions (Liste Anlamaları)
# numbers = []
#
# for x in range(10):
#     numbers.append(x)
# print(numbers)
#
# numbers = [x for x in range(10)]
# print(numbers)


# for x in range(10):
#     print(x**2)
# numbers = [x**2 for x in range(10)]
# print(numbers)

# numbers = [x for x in range(31) if x%3 == 0]
# print(numbers)

# my = 'Hello'
# hi = []
# for x in my:
#     hi.append(x)
# print(hi)

#
# hi = [x for x in 'Hello']
# print(hi)



# years = [1983, 1999, 2002, 1986]
#
# for x in years:
#     print(2019 - x)

# years = [1983, 1999, 2002, 1986]
# ages = [2019 - x for x in years]
# print(ages)

# results = [x if x%2==0 else'Tek' for x in range(1,11)]
# print(results)



# list1 = []
#
# for x in range(3):
#     for y in range(3):
#         for z in range(3):
#             list1.append((x,y,z))
# print(list1)
#
# listi = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
# print(listi)



#Rastege Verilen Sayıyı Tahmnin Etme
'''
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri
   ile buldurmaya çalış. (hak = 5)
** 'random modülü' için 'python random' şeklinde arama yapın 
** 100 üzerinden puanlama yapın.(Her soru 20 puan)
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
   üzerinden hesaplansın. 
'''

#random metodu
# import random
# print(random.random())
# print(random.uniform(0.5,45))
# print(random.randint(9,39))

import random
sayi = random.randint(1,25)

can = int(input('Kaç hakkınız olsun istersiniz?: '))

hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Sayı tahmin et: '))

    if sayi == tahmin:
        print(f'Doğru tahmin ettiniz. {sayac}.defada bidiniz. Toplam puanınız: {100 - (100/can) * (sayac - 1)} ')
        break
    elif sayi > tahmin:
        print('Yukarı')
    else:
        print('Aşağı')

    if hak == 0:
        print(f'Hakkınız bitti.Tutulan sayı {sayi}')


# Girilen Sayının Asal Sayıyı Olup Olmadığını Öğrenme
'''
Girilen bir sayının asal olup olmadığını bul.
** Asal Sayı 1 ve kendisi dışında tam böleni olmayan sayılardır.
'''

# sayi = int(input('Sayıyı gir: '))
# asalmi = True
#
# if sayi == 1:
#     asalmi = False
#
# for i in range(2,sayi):
#     if sayi%i == 0:
#         asalmi = False
#         break
#
# if asalmi:
#     print('Sayı asaldır.')
# else:
#     print('Sayı asal değildir.')
#
#
# print(asalmi)