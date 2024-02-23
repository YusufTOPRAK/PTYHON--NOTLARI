# #class
#
# class Person:
#     #class attributes
#     address = 'No information'
#     #constructor(yapıcı metod)
#     def __init__(self, name,surname, year):    #'self' yerine başka bir şey de belirtebiliriz.
#         #object attributes
#         self.name = name
#         self.sur = surname
#         self.birthyear = year
#
#         #methods
#
# #object(instance)
# p1 = Person(name = 'Yusuf', surname = 'TOPRAK', year = 2002)  #Okunurluluğu dahi iyi
# p2 = Person('Ali', 'VELİ', 1998)
#
# #update
# p1.name = 'Kazım'
# p2.sur = 'Öztürk'
#
# # accessing object attributes
# print(f'Name: {p1.name}\nSurname: {p1.sur}\nYear: {p1.birthyear}\nAddress: {p1.address}')
# print('-------------------------------')
# print(f'Name: {p2.name}\nSurname: {p2.sur}\nYear: {p2.birthyear}\nAddress: {p2.address}')
# #
# # # print(p1)
# # # print(p2)
# # # print(type(p1))
# # # print(type(p2))
# # # print(p1 == p2)


# class araba:
#     hiz = 0
#     renk = ''
#     teker = 4
#     def hizlan(self):
#         self.hiz = self.hiz + 1
#
# x = araba()
# print(x.hiz)
# x.hiz = 100
# x.hizlan()
# print(x.hiz)
#
# y = araba()
# y.hiz = 70
# y.hizlan()
# print(y.hiz)
# print(x.hiz)


# class Person:
#     #class attributes
#     address = 'No information'
#     #constructor(yapıcı metod)
#     def __init__(self, name, year):    #'self' yerine başka bir şey de belirtebiliriz.
#         #object attributes
#         self.name = name
#         self.year = year
#
#     # instance methods
#     def intro(self):
#         print('Hello There. I am ' + self.name)
#
#     # instance methods
#     def calculateAge(self):
#         return 2021 - self.year
#
# #object(instance)
# p1 = Person(name = 'Yusuf', year = 2002)
# p2 = Person(name = 'Ali', year = 1998)
#
#
# p1.intro()
# p2.intro()
#
# print('Ad:', p1.name, 'Yaş:', p1.calculateAge())
# print('Ad:', p2.name, 'Yaş:', p2.calculateAge())


# class Circle:
#     pi = 3.14
#
#     def __init__(self, yaricap = 1):
#         self.yaricap = yaricap
#
#     def alan_hesaplama(self):
#         return self.pi * (self.yaricap ** 2)
#
#     def cevre_hesaplama(self):
#         return 2 *(self.pi * self.yaricap)
#
# c1 = Circle(5)
# print(f'Dairenin Alanı: {c1.alan_hesaplama()}\nDairenin Çevresi: {c1.cevre_hesaplama()}')


#Inheritance(Kalıtım): Miras alma
# Person => name, lastname, age, eat(), walk(), drink()
# Student(Person), Teacher(Person)

#Animal => Dog(Animal), Cat(Animal)

# class Person:
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#         print('Person Created')
#
#     def who_am_i(self):
#         print('I am a person')
#
#
# class Student(Person):
#     def __init__(self, name, lastname, number):
#         Person.__init__(self, name, lastname)
#         self.number = number
#         print('Student Created')
#     #override (geçersiz kılmak)
#     def who_am_i(self):
#         print('I am a student')
#
#     def say_hello(self):
#         print('Hello. I am a student.')
#
# class Teacher(Person):
#     def __init__(self, name, lastname, branch):
#         super().__init__(name, lastname)
#         self.branch = branch
#
#     def who_am_i(self):
#         print(f'I am a {self.branch} teacher.')
#
#
# p1 = Person(name = 'Yusuf', lastname = 'TOPRAK')
# s1 = Student(name = 'Ali', lastname = 'VELİ', number = 123)
# t1 = Teacher(name = 'Kamil', lastname = 'Demir', branch = 'Math')
#
# print(f'Name: {p1.name}, Last Name: {p1.lastname}')
# print(f'Name: {s1.name}, Last Name: {s1.lastname}, Number: {s1.number}')
#
# p1.who_am_i()
# s1.who_am_i()
# s1.say_hello()
# t1.who_am_i()


#Special Methods
# class Movie:
#     def __init__(self, title, director, duration):
#         self.title = title
#         self.director = director
#         self.duration = duration
#         print('Movie objesi oluşturuldu.')
#
#     def __str__(self):
#         return f'{self.title} by {self.director}'
#
#     def __len__(self):
#         return self.duration
#
#     def __del__(self):
#         print('Film silindi.')
#
#
# m = Movie('Film Adı:', 'Yönetmen Adı:', 120)
#
# # print(str(m))
# # print(len(m))
#
# # print(type(m))
# # print(len(m))
#
# print(m)



# #Questions
# class Question():
#     def __init__(self, text, choices, answer):
#         self.text = text
#         self.choices = choices
#         self.answer = answer
#
#     def checkAnswer(self, answer):
#         return self.answer == answer
#
# #Quiz
# class Quiz():
#     def __init__(self, questions):
#         self.questions = questions
#         self.score = 0
#         self.questionsIndex = 0
#
#     def getQuestion(self):
#         return self.questions[self.questionsIndex]
#
#     def displayQuestion(self):
#         question = self.getQuestion()
#         print(f'Soru: {self.questionsIndex + 1}: {question.text}')
#
#         for q in question.choices:
#           print('-', q)
#
#         answer = input('Cevap: ')
#         self.guess(answer)
#         self.loadQuestion()
#
#     def guess(self, answer):
#         question = self.getQuestion()
#
#         if question.checkAnswer(answer):
#             self.score += 1
#         self.questionsIndex += 1
#
#     def loadQuestion(self):
#         if len(self.questions) == self.questionsIndex:
#             self.showScore()
#         else:
#             self.displayProgress()
#             self.displayQuestion()
#
#     def showScore(self):
#         print('Score: ', self.score)
#
#     def displayProgress(self):
#         totalQuestion = len(self.questions)
#         questionNumber = self.questionsIndex + 1
#
#         if questionNumber > totalQuestion:
#             print('Quiz bitti.')
#         else:
#             print(f'Question {questionNumber} of {totalQuestion}'.center(100, '*'))
#
#
#
# q1 = Question('En iyi programlama dili hangisidir?', ['Python', 'Java', 'C#', 'Javascript'], 'Python')
# q2 = Question('En popüler programlama dili hangisidir?', ['Python', 'Java', 'C#', 'Javascript'], 'Python')
# q3 = Question('En çok kazandıran programlama dili hangisidir?', ['Python', 'Java', 'C#', 'Javascript'], 'Python')
# questions = [q1, q2, q3]
#
# quiz = Quiz(questions)
# quiz.loadQuestion()



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