#Atama Operatörleri
# x, y, z = 2, 5, 10
# numbers = 1, 5, 7, 10, 6

#1 Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
# number1 = int(input('Birinci sayı:'))
# number2 = int(input('İkinci sayı:'))
# product = (number1*number2)
# fark = product - (x + y + z)
# print(fark)

#2 y'nin x'e kalansız bölümünü hesapla.
# bolum = y // x
# print(bolum)

#3 (x,y,z) toplamının mod 3'ü nedir?
# mod = (x+ y+ z) % 3
# print(mod)

#4 y'nin x. kuvvetini hesaplayınız.
# kuvvet = y ** x
# print(kuvvet)

# #5 x, *y, z = numbers işlemine göre z'nin küpü kaçtır?
# l = x,*y,z = numbers
# kup = z ** 3
# print(kup)

#6 x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
# s = x, *y, z = numbers
# total = y[0] + y[1] + y[2]
# print(total)


#Comparison Operator (Karşılaştırma Operatörleri)
#1 Girilen 2 sayıdan hangisi büyüktür?
# number1 = float(input('1.sayı:'))
# number2 = float(input('2.sayı:'))
# if number1>number2:
#     print('1.sayı büyüktür.')
# elif number1<number2:
#     print('2.sayı büyüktür.')
# else:
#     print('Hata:Eşit sayılar girilemez.')

#2 Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalamasını hesapla.
# #    Eğer ortalama 50 ve üstündeyse 'Geçti', değilse 'Kaldı' yazdırın.
# vize1 = float(input('1.vize notu:'))
# vize2 = float(input('2.vize notu:'))
# final = float(input('final notu:'))
# ortalama = (((vize1 + vize2) / 2) * 0.6) + (final* 0.4)
# print(ortalama)
# if ortalama>=50:
#     print('Geçti')
# elif ortalama<50:
#     print('Kaldı')

#3 Girilen bir sayının tek mi çift mi olduğunu yazdırın.
# sorgu = int(input('Sayıyı gir:'))
# if sorgu%2 == 0:
#     print('Çift')
# elif sorgu%1 == 0 :
#     print('Tek')

#4 Girilen sayının negatif ve pozitif durumunu yazdır.
# sorgu2= float(input('Sayıyı gir:'))
# if sorgu2>=0:
#     print('Pozitif')
# elif sorgu2<0:
#     print('Negatif')

#5 Parola ve email bilgisini isteyip doğruluğunu konrol ediniz.
#   (email: email@yusuftoprak.com, parola:abc123)
# useremail = 'email@yusuftoprak.com'
# password = 'abc123'
#
# email = input('e-mail gir:')
# parola = input('parola gir:')
# if email == useremail and parola == password:
#     print('Doğru hesap')
# else:
#     print('Yanlış hesap')




#1 Girilen bir sayının 0-100 arasında olup olmadığını kontrol et.

# number = float(input('Bir sayı gir:'))
# if number > 0 and number <= 100:
#     print('Girdiğiniz sayı 0 ile 100 arasındadır.')
# else:
#     print('Girdiğiniz sayı 0 ile 100 arasında değildir.')


#2 Girilen bir sayının pozitif ve çift sayı olup olmadığını kontrol et.

# number = float(input('Sayıyı gir:'))
# if number >= 0 and number%2 == 0:
#     print('Pozitif ve çifttir.')
# else:
#     print('Pozitif veya çift değil.')


#3 Email ve parola bilgileri ile giriş kontrolü yap.

# user = 'toprak.123@gmail.com'
# passs = '147lkj'
# users = input('e-postanı gir:')
# password = input('Şifre gir:')
# if users == user and password == passs :
#     print('Girildi.')
# else:
#     print('Olmadı.')


#4 Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# number1 = float(input('1.Sayı:'))
# number2 = float(input('2.Sayı:'))
# number3 = float(input('3.Sayı:'))
# numbers = number1, number2, number3
# numbers = list(numbers)
# numbers.sort()
# print(numbers)

# a = float(input('1.Sayı:'))
# b = float(input('2.Sayı:'))
# c = float(input('3.Sayı:'))
#
# result = a>b and a>b
# print(result)
#
# result = b>a and b>c
# print(result)
#
# result = c>a and c>b
# print(result)

#5 Kullanıcıdan 2 vize (%60) ve final (%40) notu al ve ortalamasını hesapla.
#  Eğer ortalama 50 üstündeyse 'geçti', değilse 'kaldı' yazdır.
# a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
# b) Finalden 70 alındığında ortalamanın önemi olmasın.

# vize1 = float(input('1.vize:'))
# vize2 = float(input('2.vize:'))
# final = float(input('final:'))
# ortalama = ((vize1 + vize2 /2)*0.6) + final*0.4

#a)
# if ortalama >= 50 and final >= 50:
#     print('Geçti')
# else:
#     print('Kaldı')

#b)
# if ortalama >= 50 or final >=70:
#     print('Geçti')
# else:
#     print('Kaldı')


#6 Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesapla.
# Formül: (Kilo / boy uzunluğunun karesi)
# 0-18.4 --> Zayıf
# 18.5-24.9 --> Normal
# 25.0-29.9 --> Fazla Kilolu
# 30.0-34.9 --> Şişman(Obez)

# name = input('Ad:')
# weight = float(input('Kilo:'))
# height = float(input('Boy:'))
# index = (weight/(height**2))
#
# if index >= 0 and index <= 18.4:
#     print(name)
#     print(index, 'Zayıf')
# elif index >= 18.5 and index <= 24.9:
#     print(name)
#     print(index, 'Normal')
# elif index >= 25.0 and index <= 29.0:
#     print(name)
#     print(index, 'Fazla Kilolu')
# elif index >= 30.0 and index <= 34.9:
#     print(name)
#     print(index, 'Şiman(Obez)')


# # Identity Operator(Kimlik Operatörleri): is
# x = y = [1,2,3]
# z = [1,2,3]
#
# print(x == y)
# print(x == z)
# print(x is y)
# print(x is z)
# print(x is not z)


# Membership Operator(Üyelik Operatörleri): in

# x = ['apple','banana']
# print('banana' in x)
#
# y = 'Yusuf'
# print('f' in  y)
# print('k' in y)
# print('Y' not in y)