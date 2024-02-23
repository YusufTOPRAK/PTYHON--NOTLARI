'''''
websıte = 'http://www.sadikturan.com'
course = 'Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)'

#1 'course' karakter dizisinde kaç karakter bulunmaktadır?
print(len(course))

#2 'websıte' içindeki www karakterlerini al.
print(websıte[7:10])

#03 'websıte' içinden com karakterlerini al.
print(websıte[22:])   #veya     #lenght = len(websıte)
                               #print(websıte[lenght-3:lenght])

#4 'course' içinden ilk 15 ve son 15 karakterleri bul.
print(course[0:16])
print(course[-15:])

#5 'course' ifadesindeki karakterleri tersten yazdırın.
print(course[::-1])

name,surname, age, job = 'Bora','Yılmaz',32,'mühendis'
#6 Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdır.
# 'Benim adım Bora Yılmaz,yaşım 32 ve mesleğim mühendis.'
print(f'Benim adım {name} {surname},yaşım {age} ve mesleğim {job}.')

#7 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
x = 'Hello world'
x = x[0:6] + 'W' + x[-4:]
print(x)

#8 'abc' ifadesini yan yana 3 defa yazdır.
print('abc'*3)
'''''

'''
website = 'http://www.sadikturan.com'
course = 'Python Kursu: Baştan Sona Python Proglamlama Rehberiniz (40 saat)'

#1 ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini sil.
result = '   Hello World  '.strip()

#2 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri sil.
result='www.sadikturan.com'.strip('w.com')

#3 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
#result = course.lower()

#4 'website' içinde kaç tane a karakteri vardır? (count('a'))
#result=website.count('a')
#result= website.count('w',0,10) # (0,10)=> 0 ile 10 arasında olup olmadığını kontrol eder.

#5 'website' www ile başlayıp com ile bitiyor mu?
#result = website.startswith('website')
#result = website.endswith('com')

#6 'website' içinde .com ifadesi var mı?
#result = website.find('.com') #find yerinde index de kullanabiliriz.
#result = course.rfind('Python') # index exception (hata) verir.

#7 'course' içindeki karakterlein hepsi alfabetik mi? (isalpha,isdigit)
#result = course.isalpha()
#result = '5'.isdigit()

#8 'Contents' ifadesini satırda 50 karakter içine yerleştir.
#result = 'Contents'.center(30,'*')
#result= 'Contents'.ljust(50,'*')
#result = 'Contents'.rjust(50,'*')

#9 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştir.
#result = course.replace(' ','-')

#10 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.
#result = 'Hello World'.replace('World','There')

#11 'course' karakter dizisini boşluk karakterlerinden ayırın.
#result = course.split(' ')

print(result)
'''
'''
#1 'BMW, Mercedes, Opel, Mazda' elemanlarına sahip bir liste oluştur.
a = ['BMW','Mercedes','Opel','Mazda']
#2 Liste kaç elemanlıdır?
print(len(a))
#3 Listenin ilk ve son elemanı nedir?
print(a[0])
print(a[-1])
#4 Mazda değerini Toyota ile değiştirin.
a[-1]= 'Toyota'
print(a)
#5 Mercedes listenin bir elemanı mıdır?
b='Mercedes' in a
print(b)
#6 Listenin -2 indeksindeki değer nedir?
print(a[-2])
#7 Listenin ilk 3 elemanını alın.
print(a[:3])
#8 Listenin son 2 elemanı yerine 'Toyoto' ve 'Renault' değerlerini ekle.
a[-2:] = ['Toyoto', 'Renault']
print(a)
#9 Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekle.
a = a +  ['Audi'] + ['Nissan']
print(a)
#10 Listenin son elemanını sil.
del a[-1]
print(a)
#11 Liste elemanlarını tersten yazdır.
print(a[::-1])
#12 Aşağıdaki verileri bir liste içinde saklayınız
    # studentA : Yiğit Bilgi 2010, (70,60,70)
    # studentB : Sena Turan 1999, (80,80,70)
    # studentC : Ahmet Turan 1998, (80,70,90)
studentA = ['Yiğit','Bilgin',2010,[70,60,70]]
studentB = ['Sena', 'Turan', 1999, [80,80,70]]
studentC = ['Ahmet', 'Turan', 1998,[80,70,90]]
students = [studentA, studentB, studentC]

#13 Liste elemanlarını ekrana yazdır.
print(students)
print(studentA[3][1])

print('Yiğit Bilgin 11 yaşında ve not ortalaması 66')
print(f'{studentA[0]} {studentA[1]} {2021-studentA[2]} yaşında ve not ortalaması{(studentA[3][0] + studentA[3][1] + studentA[3][2])//3}')
'''

'''
names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998,2000,1998,1987]

#1 'Cenk' ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)
#2 'Sena' değerini listenin başına ekleyiniz.
names.insert(0,'Sena')
print(names)
#3 'Deniz' ismini listeden siliniz.
del names[-2]
print(names)
#names.remove('Deniz')
#names.pop(4)

#4 'Hakan' isminin indeksi nedir?
a = names.index('Hakan')
print(a)
#5 'Ali' listenin bir elemanı mıdır?
a = 'Ali' in names
print(a)
#6  Liste elemanlarını ters çevirin.
# names.revorse()
print(names[::-1])

#7 Liste elemanlarını alfabetik olarak sırala.
names.sort()
print(names)
#8 years listesini rakamsal büyüklüğe göre sırala.
years.sort()
print(years)
#9 str = 'Chevrolet, Dacia' karakter dizisini listeye çeviriniz.
cars = ('Chevrolet','Dacia')
cars = list(cars)
print(cars)
#10 years dizisin en büyük ve en küçük elemanı nedir?
print(max(years))
print(min(years))
#11 years dizisinde kaç tane 1998 değeri vardır?
e=names.count(1998)
print(e)
#12 years elemanlarının tüm elemanlarını siliniz.
years.clear()
print(years)
#13 Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
b = [input('Markaları Giriniz:')]
print('Seçtiğiniz markalar;',b)

b = [input('Markaları Giriniz:')]
print('Seçtiğiniz markalar;',b)

b = [input('Markaları Giriniz:')]
print('Seçtiğiniz markalar;',b)
'''

''' Dictionary

1) Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
  dictionary içinde saklayınız.

2) Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisiniz gösterin.
'''

# ogrenciler= {}
# #
# number = input('Öğrenci No:')
# name = input('Öğrenci Adı:')
# surname = input('Öğrenci Soyadı:')
# phone = input('Öğrenci Telefon Numarası:')
# #
# ogrenciler[number] ={
#     'Ad': name,
#     'Soyad': surname,
#     'Telefon Numarası': phone
# }
# print(ogrenciler)

# ogrenciler.update({
#     number:{
#         'Ad':name,
#         'Soyad':surname,
#         'Telefon Nunamarası':phone
#     }
# })


# number = input('Öğrenci No:')
# name = input('Öğrenci Adı:')
# surname = input('Öğrenci Soyadı:')
# phone = input('Öğrenci Telefon Numarası:')
#
# ogrenciler.update({
#     number:{
#         'Ad':name,
#         'Soyad':surname,
#         'Telefon Nunamarası':phone
#     }
# })

# number = input('Öğrenci No:')
# name = input('Öğrenci Adı:')
# surname = input('Öğrenci Soyadı:')
# phone = input('Öğrenci Telefon Numarası:')

# ogrenciler.update({
#     number:{
#         'Ad':name,
#         'Soyad':surname,
#         'Telefon Nunamarası':phone
#     }
# })

# print(ogrenciler)
#
# ogrNo = input('Öğrenci No:')
# ogrenci = ogrenciler[ogrNo]
# print(ogrenci)

# ogrNo = input('Öğrenci No:')
# ogrenci = ogrenciler[ogrNo]
# print(ogrenci)

# ogrNo = input('Öğrenci No:')
# ogrenci = ogrenciler[ogrNo]
# print(ogrenci)

# print(50*'-')
#
# print(f"Aradağınız {ogrNo} nolu öğrencinin adı {ogrenci[name]}, soyadı{ogrenci[surname]},ve telefonu ise {ogrenci[phone]}")