#1 Kullanıcıdan isim, yaş ve eğitim biligilerini iste ve ehliyet ala-
#  bilme durumunu kontrol et. Ehliyet alma koşulu en az 18 ve eğitim
#  durumu lise ya da üniversite olmalı.

# name = input('Ad-Soyad:')
# age = int(input('Yaş:'))
# education = input('Eğitim Durumu:')

# if age >= 18 and education == 'Lise':
#     print('Kabul edildi.')
# elif education == 'Üniversite' and age >=18 :
#     print('Kabul edildi.')
# else:
#     print('Kabul edilmedi.')

# if (age>=18):
#     if (education == 'Lise' or education == 'Üniversite'):
#         print('Kabul edildi.')
#     else:
#         print("Kabul edilmedi\nEğitim durumunuz lise veya üniversite mezunu olmalı.")
# elif (education == 'Üniversite' or education == 'Lise'):
#     if (age<18):
#         print("Kabul edilmedi.\nYaşınız 18 veya 18'den büyük olmalıdır.")
# else:
#     print('Kabul edilmedi.\nEğitim durumunuz ve yaşınız uygun değil.')

#2 Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya
#  göre not aralığına karşılık gelen not bilgisini yazdır.
#   0-24 => 0
#   25-44 => 1
#   45-54 => 2
#   55-69 => 3
#   70-84 => 4
#   85-100 => 5


# yazili1 = float(input('1.Yazılı Notu:'))
# yazili2 = float(input('2.Yazılı Notu:'))
# sozlu = float(input('Sözlü Notu:'))
# ortalama = (yazili1 + yazili2 + sozlu) /3
#
# if ortalama >= 0 and ortalama <= 24:
#     print(f'Ortalama: {ortalama} Not:0')
# elif ortalama >= 25 and ortalama <= 44:
#     print(f'Ortalama:{ortalama} Not:1')
# elif ortalama >= 45 and ortalama <= 54:
#     print(f'Ortalama:{ortalama} Not:2')
# elif ortalama >= 55 and ortalama <= 69:
#     print(f'Ortalama:{ortalama} Not:3')
# elif ortalama >= 70 and ortalama <= 84:
#     print(f'Ortalama:{ortalama} Not:4')
# elif ortalama >= 85 and ortalama <= 100:
#     print(f'Ortalama:{ortalama} Not:5')
# else:
#     print('Uygun olmayan sayılar girildi.')


#3 Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bil-
#  gilere göre hesaplayınız.
#   1.Bakım => 1.yıl
#   2.Bakım => 2.yıl
#   3.Bakım => 3.yıl
#   ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesapla
#    NOT: detatime modülünü kullanmalısın
#    (şimdi) - (2021/6/9)

# import datetime
#
# tarih = input('Aracanız hangi tarihte trafiğe çıktı?:')
# tarih = tarih.split('/')
#
# trafigecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# simdi = datetime.datetime.now()
# fark = simdi - trafigecikis
# days = fark.days

# print(days)
# if days <= 365:
#     print('1.Bakım yılı')
# elif days > 365 and days <= 365*2:
#     print('2.Bakım yılı')
# elif days > 365*2 and days <= 365*3:
#     print('3.Bakım yılı')
# else:
#     print('Hatalı giriş')


#1 Girilen bir sayının 0-100 arasında olup olmadığını kontrol et.

# number = float(input('Sayıyı Giriniz:'))

# if number >= 0 and number <= 100:
#     print('Girdiğiniz sayı 0 ile 100 arasındadır.')
# else:
#     print('Girdiğiniz sayı 0 ile 100 arasında değildir.')


#2 Girilen bir sayının pozitif çift sayı olup olmadığını kontrol et.

# number = float(input('Sayıyı Giriniz:'))
#
# if number >= 0 and number%2 == 0:
#     print('Girdiğiniz sayı pozitif ve çifttir.')
# elif number >= 0 and number%1 == 0:
#     print('Girdiğiniz sayı pozitif ve tektir.')
# elif number < 0 and number%2 == 0:
#     print('Girdiğiniz sayı negatif ve çifttir.')
# elif number < 0 and number%1 == 0:
#     print('Girdiğiniz sayı negatif ve tektir.')


#3 Email ve parola bilgileri ile giriş kontrolü yap.

# user = 'toprak.321'
# password = '123amed'
#
# email = input('Email:')
# sifre = input('Şifre:')
#
# if email == 'toprak.123' and sifre == password:
#     print('Giriş yapıldı.')
# else:
#     print('Nah girersin.')


#4 Girilen 3 sayıyı büyüklük olarak karşılaştır.

# sayi1 = float(input('1.sayı:'))
# sayi2 = float(input('2.sayı:'))
# sayi3 = float(input('3.sayı:'))
#
# if sayi1 > sayi2 and sayi1 > sayi3:
#     print(f'En büyük sayı {sayi1}')
# elif sayi2 > sayi1 and sayi2 > sayi3:
#     print(f'En büyük sayı {sayi2}')
# elif sayi3 > sayi1 and sayi3 > sayi2:
#     print(f'En büyük sayı {sayi3}')


#5 Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalamasını hesapla.
#   a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#   b) Finalden 70 aldığında ortalamanın önemi olmasın.

# vize1 = float(input('1.Vize:'))
# vize2 = float(input('2.Vize:'))
# final = float(input('Final:'))
# ortalama = (((vize1 + vize2)/2)*0.6) + final*0.4
# print(ortalama)

#a)
# if ortalama >= 50 and final >= 50:
#     print('Geçti')
# else:
#     print('Kaldı')

#b)
# if ortalama >= 50 or final>= 70:
#     print('Geçti')
# else:
#     print('Kaldı')


#6 Kişinin ad,kilo ve boy bilgilerini alıp kilo indeksini hesapla.
#  Formül:(Kilo/boy uzunluğunun karesi)
#  0-18.4    => Zayıf
#  18.5-24.9 => Normal
#  25.0-29.9 => Fazla Kilolu
#  30.0-34.9 => Şişman(Obez)

# name = input('Ad-Soyad:')
# kilo = float(input('Kilo:'))
# boy = float(input('Boy:'))
# indeks = (kilo/(boy**2))
# print(indeks)
#
# if indeks >= 0 and indeks <=18.4:
#     print(f'{name} kilo indeksin {indeks}:Zayıf')
# elif indeks >= 18.5 and indeks <= 24.9:
#     print(f'{name} kilo indeksin {indeks}:Normal')
# elif indeks >= 25.0 and indeks <= 29.9:
#     print(f'{name} kilo indeksin {indeks}:Fazla Kilolu')
# elif indeks >= 30.0 and indeks <= 34.9:
#     print(f"{name} kilo indeksin {indeks}:Şişman(Obez)")