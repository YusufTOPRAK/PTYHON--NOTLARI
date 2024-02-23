# Modüller
# Math Modülü

# 1.YÖNTEM
#import math
# value = dir(math)
# value = help(math)
# value = help(math.factorial)
#value = math.sqrt(25)
# value = math.factorial(5)
# value = math.floor(6.4)
# value = math.ceil(8.7)
#print(value)


# # 2.YÖNTEM
# import math as islem
# value = islem.factorial(5)
# print(value)

# # 3.YÖNTEM
# #from math import*
# from math import sqrt
# value = sqrt(4)
# value = factorial(5)
# print(value)

# from math import sqrt,factorial
# def sqrt(x):
#     print(f'x: {x}')
# value = sqrt(16)

# #random Modülü
# import random
#
# # result = dir(random)
# # result = help(random.choices)
# value = random.random()
# value = random.random() * 100
# value = random.uniform(1, 10)
# value = random.randint(1, 10)
#
# names = ['Yusuf', 'Ali', 'Veli', 'Kemal', 'Kazım']
# # value = names[random.randint(0, len(names) - 1)]
# value = random.choice(names)
#
# greeting = 'Hello There'
# value = random.choice(greeting)
#
# liste = list(range(10))
# random.shuffle(liste)
# value = liste
#
# liste = range(100)
# value = random.sample(liste, 15)
# value = random.sample(names, 2)
# print(value)


### DATETIME MODULE ###
# from datetime import*
# from datetime import datetime
# result = dir(datetime)


# now = datetime.now() ==> SAME
# now = datetime.today()
# # result = datetime.now().year
# result = now.year
# result = now.day
# result = now.hour
# result = now.minute
# result = now.second
# result = now.month
# result = datetime.ctime(now)  # Açıklayıcı bir bilgi verdi.
# result = datetime.strftime(now, '%Y')
# result = datetime.strftime(now, '%X')
# result = datetime.strftime(now, '%d')
# result = datetime.strftime(now, '%A')
# result = datetime.strftime(now, '%B')
# result = datetime.strftime(now, '%B %Y %A')
# print(result)
#
# now = datetime.today()
#
# t = '28 August 2021  10:12:30'
# dt = datetime.strptime(t, '%d %B %Y  %H:%M:%S')
# result = dt.minute
#
# birthday = datetime(2002,1,26, 15,12,25)
# result = datetime.time(birthday)
# result = datetime.timestamp(birthday)
# result = datetime.fromtimestamp(result)
# result = datetime.fromtimestamp(0)
#
# now = datetime.today()
# result = now - birthday
# # result = result.microseconds
#
# from datetime import timedelta
# result = now + timedelta(days=365)
# result = now - timedelta(days=8)
#
# print(result)

### Os MODULE ###
# import os
# import datetime
# result = os.name

### dizin değiştirme ###
# os.chdir('C:\\')
# os.chdir('../..')

### klasör oluşturma ###
# os.mkdir('newdirectory')
# os.makedirs('newdirectory/yeniklasör')  (C:\\)  you may do this
# os.rename('newdirectory', 'yeniklasör')
# os.rmdir('newdirectory') ###siler
# os.removedirs('yeniklasör/yeniklasör') ###konum belirterek silme

### etkin dizin öğrenme ###
# result = os.getcwd()

### listing ###
# result = os.listdir()
# result = os.listdir('C:\\')
# for file in os.listdir():
#     if file.endswith('.py'):
#         print(file)

# result = os.stat('main.py')
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi

# os.system('notepad.exe')

### path ###
# result = os.path.abspath('_os.py')
# result = os.path.dirname('C:/Users/Mehmet TOPRAK/PycharmProjects/PYTHON ÖĞREN/venv/Scripts/_os.py')
# result = os.path.dirname(os.path.abspath('_os.py'))
# result = os.path.exists('C:/Users/Mehmet TOPRAK/PycharmProjects/PYTHON ÖĞREN/venv/Scripts/_os1.py')
# result = os.path.exists('C:/Users/Mehmet TOPRAK/PycharmProjects/PYTHON ÖĞREN/venv/Scripts')
# result = os.path.isdir('C:/Users/Mehmet TOPRAK/PycharmProjects/PYTHON ÖĞREN/venv/Scripts')
# result = os.path.isfile('C:/Users/Mehmet TOPRAK/PycharmProjects/PYTHON ÖĞREN/venv/Scripts')
# result = os.path.join('C:\\','deneme','deneme1')
# result = os.path.split('C:\\deneme')
# result = os.path.splitext('_os.py')
# result = result[0]
# print(result)

#### RE MODULE ####
# import json
# import re
## re module ##
# str = 'Hi. My name is Yusuf and my last name TOPRAK. I am 19 years old.'

# result = re.findall('Yusuf', str)
# result = re.split('n', str)
# result = re.sub('TOPRAK', 'DEMİR', str)
# result = re.search('Yusuf', str)  # match objesi oluştu.
# result = result.span()
# result = result.start()
# result = result.end()
# result = result.group()
# result = result.string

# regular expression
'''
    [] - Köşeli parantezler arasına yazılan bütün karakterler aranır.

         [abc] => a      : 1 match
                  ab     : 2 match

         [a-e] => [abcde]
         [1-5] => [12345]
         [0-39] => [01239]

         [^abc] => abc dışındaki karakterler
         [^0-9] => rakam olmayan karakterler
'''
# result = re.findall('[fsnm]',str)
# result = re.findall('[Yusf]',str)
# result = re.findall('[a-z]', str)
# result = re.findall('[19]', str) # 1 ve 9 iki ayrı eleman
# result = re.findall('[^a-l]', str) # a den l'ye kadar haricinde

'''
       . -Herhangi bir karakteri ifade eder.
            .. => a    : No match  # İki basamklı olmalı varsa da yok sayılır.
                  ab   : 1 match
                  abc  : 1 match    
                  abcd : 2 match
'''
# result = re.findall('...', str) # her üç adımda bir ayırır
# result = re.findall('Yu..f', str)

'''
        ^ - Belirtilen string karakterle başlıyor mu?

        ^a => a   : 1 match
              abc : 1 match
              bac : No match

        $ - Belirtilen string karakterle bitiyor mu?

        a$ => a      : 1 match
              lamba  : 1 match
              Hi     : No match

'''
# result = re.findall('^H',str)
# result= re.findall('l.$', str)

'''
    * - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.

        ma*n => mn    : 1 match
                man   : 1 match
                maaan : 1 match
                main  : No match (a'nın arkasına n gelmiyor.)
'''
# result = re.findall('Yu*uf', str)
# ex = 'saat'
# result = re.findall('sa*t', ex)
# print(result)
'''
    + - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.


        ma+n => mn    : No match
                man   : 1 match
                maaan : 1 match
                main  : No match (a' nın arkasına n gelmiyor.)               
'''
# result = re.findall('Yu+uf', str)
# ex = 'saat'
# result = re.findall('sa+t', ex)

'''
    ? - Bir karakterin sıfır ya da bir kez olmasını kontrol eder.

         ma+n => mn    : No match
                 man   : 1 match
                 maaan : 1 match
                 main  : No match (a' nın arkasına n gelmiyor.) 
'''
# ex = 'saat'
# result = re.findall('sa?t', ex)

'''
    {} - Karakter sayısını kontrol eder.

        al{2}      => a karakterinin arkasına 1 karakteri 2 kez tekrarlanmalı.
        al{2,3}    => a karakterinin arkasına 1 karakteri en az 2 en fazla 3 kez tekrarlanmalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar
'''
# ex = 'saat'
# result = re.findall('a{2}', ex)
# result = re.findall('[0-9]{2}', str)

'''
    | - Alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da b

              cde =>    no match  
              ade =>    1 match   
              acdbea => 3 match  
'''

'''
    () - Grulamak için kullanılır.

         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
'''

'''
    \ - Özel karakterleri aramanızı sağlar.
        \$ => $ karakterinin arkasına a karakterini arar.Yani
              $ regular exp. engine tarafından yorumlanmaz.

    \A - Belirtilen karakter string'in başında mı?
         \Athe => the string'in başında mı?            

    \Z - Belirtilen karakter string'in sonunda mı?
         the\Z => the string'in sonunda mı

    \b - Belirilen karakter kelimenin başında ya da sonunda mı?
         \bthe => the kelimenin başında mı?
         the\b => the kelimenin sonunda mı?

    \B - Belirtilen karakter kelimenin naşında ya da sonunda değil mi?
         \Bthe => the kelimenin başında değil mi?      
         the\B => the kelimenin sonunda değil mi?

    \d - [0-9] ile aynı anlama gelir yani rakamları arar.     
         \d => 12abc3

    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.     
         \D => 1ab44_50

    \s - Boşluk karakterlerini arar.
    \S - Boşluk karakterleri dışındakiler  
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri
    \W - \w' tersi   
'''
# print(result)

#### jSON MODULE ####
# import json
## json string to dict ##
# person ='{"name":"Yusuf", "languages":["Pytgon","C#"]}'
# print(type(person))
# result = json.loads(person)
# print(result)
# print(type(result))
# print(result['name'])

## dosyadan json bilgiyi okuma ##
# with open('exam_grade.txt') as file:
#     data = json.load(file)
#     print(data["languages"])

## dict to json string ##
# person = {"name":"Yusuf", "languages":["Python", "C#"]}
# print(type(person))
# result = json.dumps(person)
# print(result)
# print(type(result))

## json dosyaya yazma ##
# person = {"name":"Yusuf", "languages":["Python", "C#"]}
# with open('exam_grade.txt', 'w') as file:
#     data = json.dump(person, file)

# person = '{"name":"Yusuf", "languages":["Python", "C#"]}'
# person = json.loads(person)
# result = json.dumps(person, indent = 4, sort_keys = True)
# print(result)
# print(type(result))

## UYGULAMA ##
# import json
# import os
#
# class User:
#     def __init__(self, user_name, email, password):
#         self.user_name = user_name
#         self.email = email
#         self.password = password
#
# class UserRepository:
#     def __init__(self):
#         self.users = []
#         self.isLoggedIn = False
#         self.currentUser = {}
#
#         # load users from .json file
#         self.loadUsers()
#
#     def loadUsers(self):
#         if os.path.exists('user.txt'):
#             with open('user.txt', 'r', encoding='utf-8') as file:
#                 users = json.load(file)
#                 for i in users:
#                     user=json.loads(i)
#                     new_user = User(user_name=user['user_name'], password=user['password'], email=user['email'])
#                     self.users.append(new_user)
#                 print(self.users)
#
#     def register(self, user:User):
#         self.users.append(user)
#         self.savetoFile()
#         print('Kullanıcı oluşturuldu.')
#
#
#     def login(self, user_name, password):
#         for i in self.users:
#             if i.user_name == user_name and i.password == password:
#                 self.isLoggedIn = True
#                 self.currentUser = i
#                 print('Login işlemi tamamlandı.')
#                 break
#     def logout(self):
#         self.isLoggedIn = False
#         self.currentUser = {}
#         print('Çıkış yapıldı.')
#
#     def identity(self):
#         if self.isLoggedIn:
#             print(f'username: {self.currentUser.user_name}')
#         else:
#             print('Giriş yapılmadı.')
#
#     def savetoFile(self):
#         liste = []
#         for i in self.users:
#             liste.append(json.dumps(i.__dict__))
#
#         with open('user.txt','w', encoding='utf-8') as file:
#            json.dump(liste, file)
#
#
# repository = UserRepository()
#
# while True:
#     print('Menu'.center(50,'*'))
#     secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçin: ')
#
#     if secim == '5':
#         break
#     else:
#         if secim == '1':
#             username = input('username: ')
#             email = input('email: ')
#             password = input('passsword: ')
#             user = User(user_name=username, email=email, password=password)
#             repository.register(user)
#
#         elif secim == '2':
#             if repository.isLoggedIn:
#                 print('Zaten login etmişsiniz.')
#             else:
#                 user_name = input('username: ')
#                 password = input('password')
#                 repository.login(user_name, password)
#         elif secim == '3':
#             repository.logout()
#         elif secim == '4':
#             repository.identity()
#         else:
#             print('Yanlış değer girdiniz.')

#### Requests Module ####
# import requests
# import json
#
# result = requests.get('https://jsonplaceholder.typicode.com/todos')
# result = json.loads(result.text)
#
# # for i in result:
# #     print(i['title'])
# for i in result:
#     if i['userId'] == 1:
#         print(i['title'])
# print(type(result))

## UYGULAMA ##
# import requests
# import json
#
# api_url = 'SİTE ADRESİ'
#
# bozulan_doviz = input('Bozolacak döviz türü: ')
# alinan_doviz = input('Alınacak döviz türü: ')
# miktar = int(input(f'Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: '))
#
# result = requests.get(api_url + bozulan_doviz)
# result = json.loads(result.text)
#
# print('1 {0] = {1} {2}'.format(bozulan_doviz, result['rates'][alinan_doviz], alinan_doviz))
# print('{0] {1} =  {2}'.format(miktar, bozulan_doviz, miktar*result['rates'][alinan_doviz], alinan_doviz))

## UYGULAMA ##
# import requests
#
# class Github:
#     def __init__(self):
#         self.api_url = 'https://api.github.com'
#         self.token =  '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'
#
#     def getUser(self, username):
#         response = requests.get(self.api_url+'/users/'+username)
#         return response.json()
#
#     def getRepositories(self, username):
#         response = requests.get(self.api_url+'/users/'+username+'/repos')
#         response.json()
#
#     def createRepositories(self, name):
#         response = requests.post(self.api_url+'/user/repos?access_token='+self.token, json={
#             'name': 'Helllo-World',
#             'description': 'This is your first repository',
#             'homepage': 'https://github.com',
#             'private': False,
#             'has_issues': True,
#             'has_projects': True,
#             'has_wiki': True
#         })
#         return response
#
# github = Github()
#
# while True:
#     secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nChose: ')
#     if secim == '4':
#         break
#     else:
#         if secim == '1':
#             username = input('Enter user name: ')
#             result = github.getUser(username = username)
#             print(f"Name: {result['name']} public repos: {result['public_repos']} follower: {result['followers']}")
#         elif secim == '2':
#             username = input('Enter user name: ')
#             result = github.getRepositories(username=username)
#             for repo in result:
#                 print(repo['name'])
#
#         elif secim == '3':
#             name = input('Enter repository name: ')
#             result = github.createRepositories(name=name)
#             print(result)
#         else:
#             print('Yanlış seçim.')

## Movie Api ##


### BEAUTIFULSOUP ### ==> html içeriği içerisinden ayıklama yapmak için kullanılır.
# html_doc = '''
# <html lang="tr" >
#     <head>
#         <title>Metin ve Listeleme Çalışmaları</title>
#         <meta charset="utf-8">
#     </head>
#     <body>
#         <h1>Başlık</h1>
#         <h2>Başlık 2-1</h2>
#         <h2>Başlık 2-2</h2>
#         <h2>Başlık 2-3</h2>
#         <div class="grup1">
#             <p>Burası div1 paragrafı</p>
#             <p id="sari">Sarı Lavivert <strong>Deri</strong> <em>Futbol</em> Topu</p>
#             <p>Sarı <u>Lavivert</u> <b>Deri</b> <i>Futbol</i> Topu</p>
#             <ul>
#                 <li>Elma</li>
#                 <li>Armut</li>
#                 <li>Portakal</li>
#             </ul>
#
#             <ol>
#                 <li>Elma</li>
#                 <li>Armut</li>
#                 <li>Portakal</li>
#             </ol>
#             <a href="www.youtube.com1">Youtube</a>
#             <a href="www.youtube.com2">Youtube</a>
#             <a href="www.youtube.com3">Youtube</a>
#         </div>
#         <div class="grup2">
#             <p>Burası div2 paragrafı</p>
#         </div>
#         <div class="grup3">
#             <p>Burası div3 paragrafı</p>
#         </div>
#     </body>
# </html>
# '''
#
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# result = soup.prettify()
# result = soup.title
# result = soup.head
# result = soup.body
# result = soup.title.name
# result = soup.title.string
# result = soup.h1
# result = soup.h2
# result = soup.find_all('h2')
# result = soup.find_all('h2')[1]
# result = soup.div
# result = soup.div.ul
# result = soup.div.ul.li
# result = soup.div.ul.find_all('li')
# result = soup.div.ul.find_all('li')[1]
# result = soup.div.findChildren()
# result = soup.div.findNextSibling()
# result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()
# print(result)
#
# result = soup.find_all('a')
# for i in result:
#     print(i.get('href'))

### UYGULAMA ###
"""
Buraya BeautifulSoup uygulaması yazılacak. 
"""