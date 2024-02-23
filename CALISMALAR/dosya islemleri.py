## OPENING FILES & WRITING:
# Dosya açmak ve oluşturmak için open() fonksiyonu:
# Kullanımı: open(file_name, file_access_mode)
# file_access_mode => Dosyayı hangi amaçla açtığımızı belirtir.

# 'w': (Write) Yazma. Dosyayı konumda oluştutur.
#    **Dosyayı konumda oluşturur.
#    **Dosya içeriğini siler ve yeniden ekler.
# file = open('newfile.txt', 'w')
# file.close()
# file = open('C:/users/Mehmet TOPRAK/desktop/newfile.txt', 'w')

# file = open('newfile.txt', 'w', encoding='utf-8')
# file.write('Yusuf Toprak')
# file.close()


# 'a': (Append) Ekleme. Dosya konumda yoksa oluşturur.
# file = open('newfile.txt', 'a', encoding='utf-8')
# file.write('\nAli Veli')
# file.close()


# 'x': (Create) Oluşturma. Dosya varsa hata verir.
# file = open('newfile2.txt', 'x',  encoding='utf-8')

# 'r': (Read) Okuma. Varsayılan dosya konumda yoksa hata verir.
# try:
#     file = open('newfile.txt', 'r', encoding='utf-8')
#     print(file)
# except FileNotFoundError as error:
#     print(f'Dosya bulunamadı.', error)

# file = open('newfile.txt', 'r', encoding='utf-8')

# read() fonksiyonu
# for i in file:
#     print(i, end='')

# print('içerik1')
# print(file.read())
#
# file = open('newfile.txt', 'r', encoding='utf-8')
# print('içerik2')
# print(file.read())

# print(file.read(6))
# print(file.read(4))
# print(file.read(2))

#readline() fonksiyonu
# print(file.readline(),end='')
# print(file.readline(),end='')
# print(file.readline(),end='')
# print(file.readline(),end='')
# print(file.readline(),end='')
# print(file.readline(),end='')
# print(file.readline())
# print(file.readline())
# print(file.readline())

#readlines() fonksiyonu
# liste = file.readlines()
# print(liste)
# print(liste[0])
# print(liste[1])
# print(liste[2])
# file.close()


# with open('newfile.txt', 'r+', encoding='utf-8') as file:
#     file.seek(20)
#     file.write('DENEME')
# with open('newfile.txt', 'r+', encoding='utf-8') as file:
#     print(file.read())

#*******SAYFANIN SONUNA GÜNCELLEME
# with open('newfile.txt', 'a', encoding='utf-8') as file:
#     file.write('OVER')
# with open('newfile.txt', 'r', encoding='utf-8') as file:
#     print(file.read())

#*******SAYFANIN BAŞINA GÜNCELLEME
# with open('newfile.txt', 'r+', encoding='utf-8') as file:
#     content = file.read()
#     content = 'HELLO' + content
#     file.seek(0)
#     file.write(content)
# with open('newfile.txt', 'r', encoding='utf-8') as file:
#     print(file.read())

#*******SAYFANIN ORTASINA GÜNCELLEME
# with open('newfile.txt', 'r+', encoding='utf-8') as file:
#     liste = file.readlines()
#     liste.insert(1, 'KAZIM\n')
#     file.seek(0)
#     for i in liste:
#         file.write(i)

#alternative
# with open('newfile.txt', 'r+', encoding='utf-8') as file:
#     liste = file.readlines()
#     liste.insert(1, 'Ömer\n')
#     file.seek(0)
#     file.writelines(liste)
# with open('newfile.txt', 'r', encoding='utf-8') as file:
#     print(file.read())


# def calculate_average(line):
#     line = line[:-1]
#     liste = line.split(':')
#     student_name = liste[0]
#     student_grade = liste[1].split(',')
#
#     grade1 = student_grade[0]
#     grade2 = student_grade[1]
#     grade3 = student_grade[2]
#
#     average = (int(grade1) + int(grade2) + int(grade3)) / 3
#     if average >= 90 and average <= 100:
#         letter = 'AA'
#     if average >= 85 and average <= 89:
#         letter = 'BA'
#     if average >= 80 and average <= 84:
#         letter = 'BB'
#     if average >= 75 and average <= 79:
#         letter = 'CB'
#     if average >= 70 and average <= 74:
#         letter = 'CC'
#     if average >= 65 and average <= 69:
#         letter = 'DC'
#     if average >= 60 and average <= 64:
#         letter = 'DD'
#     if average >= 50 and average <= 59:
#         letter = 'FD'
#     if average <= 49:
#         letter = 'FF'
#
#     return f'{student_name}: {letter}\n'
#
#
# def read_gread():
#     with open('student.txt', 'r', encoding='utf-8') as file:
#         for line in file:
#             print(calculate_average(line))
#
# def enter_grade():
#     name = input('Enter student name: ')
#     last_name = input('Enter student last name: ')
#     exam1 = int(input('Enter first exam grade: '))
#     exam2 = int(input('Enter second exam grade: '))
#     exam3 = int(input('Enter third exam grade: '))
#     yazdir = f'{name} {last_name}: {exam1}, {exam2}, {exam3}\n'
#
#     with open('student.txt', 'a', encoding='utf-8') as file:
#         file.write(yazdir)
#
#
# def save_grade():
#     with open('student.txt', 'r', encoding='utf-8') as file:
#         liste = []
#
#         for i in file:
#             liste.append(calculate_average(i))
#
#             with open('exam_grade.txt', 'w', encoding='utf-8') as file2:
#                 for i in liste:
#                     file2.write(i)
# while True:
#     islem = input('1-Read Greade\n2-Enter Grade\n3-Save Grades\n4-Exit\nChoose: ')
#
#     if islem == '1':
#         read_gread()
#
#     elif islem == '2':
#         enter_grade()
#
#     elif islem == '3':
#         save_grade()
#
#     elif islem == '4':
#         break
