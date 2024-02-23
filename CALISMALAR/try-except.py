# # error handling
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except ZeroDivisionError:
#     print("0'a bölemezsin.")

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError, ValueError) as e:
#     print('Yanlış değer girdiniz.')
#     print(e)

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('Yanlış bir değer girdiniz:')

# while True:
#     try:
#        x = int(input('x: '))
#        y = int(input('y: '))
#        print(x/y)
#     except Exception as ex:
#        print('Yanlış bilgi girdiniz.', ex)
#     else:
#        print('Her şey yolunda.')
#        break
#     finally:
#         print('try except sonlandı.')

#Raising an Exception
# x = 10
# if x > 5:
#     raise Exception('x 5 ten büyük değer alamaz.')

# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception('Parolanız en az 8 karakter içermelidir.')
#
#     elif not re.search('[a-z]', psw):
#         raise Exception('Parola küçük harf içermelidir.')
#
#     elif not re.search('[A-Z]', psw):
#         raise Exception('Parola büyük harf içermelidir.')
#
#     elif not re.search('[0-9]', psw):
#         raise Exception('Parola rakam içermelidir.')
#
#     elif not re.search('[_@£$]', psw):
#         raise Exception('Parola alpha numeric karakter içermelidir.')
#
#     elif re.search('\s', psw):
#         raise Exception('Parola boşluk içermemelidir.')
#
# parola = input('Parola giriniz: ')
#
# try:
#     check_password(parola)
# except Exception as ex:
#     print(ex)
# else:
#     print('Parolanız oluşturuldu.')
# finally:
#     print('KOD TAMAMLANDI.')

# class Person():
#     def __init__(self, name, year):
#         if len(name) > 10:
#             raise Exception('name alanı fazla karakter içeriyor.')
#         else:
#           self.name = name
#           print('No problem')
# try:
#     name = input('Enter your name: ')
#     p = Person(name, 2002)
# except Exception as err:
#     print(err)

# liste = ['1', '2', '5a', '10b', 'abc', '10', '50']

#1) Liste elemanları içindeki sayısal değerleri bul.
# for i in liste:
#     try:
#         cevir = int(i)
#         print(cevir)
#     except:
#         continue

#2) Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayisal değer
   #olduğundan emin ol aksi halde hata mesajı yazın.
# while True:
#     sayi = input('Sayı gir: ')
#     if sayi == 'q':
#         break
#     try:
#         cevir = int(sayi)
#         print(sayi)
#         break
#     except:
#         print('Lütfen sayısal bir değer giriniz.')
#         continue

#3) Girilen parola için türkçe karakter hatası ver.
# turkce_karakterler = 'çğıİöşü'
# parola = input('Parola gir: ')
#
# for i in parola:
#     if i in turkce_karakterler:
#         raise Exception('Parola türkçe karakter içeremez.')
# print('Parolanız oluşturuldu.')

#4) Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı ver.
# def faktoriyel(x):
#     x = int(x)
#
#     if x < 0:
#         raise Exception('Negatif sayıların faktöriyeli alınamaz.')
#
#     fact = 1
#     for sayi in range(1, x+1):
#         fact *= sayi
#     print(fact)
#
# sayi1 = input('Sayı gir: ')
# try:
#     faktoriyel(sayi1)
# except Exception as e:
#     print('Hesaplanamadı.', e)
