# import turtle
# import time
#
# while True:
#     form = turtle.Screen()
#     form.bgcolor('black') # Arka plan rengini belirler.
#     form.title('Proje') # Başlık belirler.
#     #form.bgpic() # Arka plana resim ekler
#     t = turtle.Turtle() # Ekranı oluşturur.
#     t.shape('turtle') # Çizimde kullanılan kalemin şeklini belirler.
#     #print(help(turtle.shape))
#     t.color('red', 'green') # İlk renk çizginin rengi, ikinci renk ise kalemin kendi rengidir.
#     t.forward(75) # Çizilen çizginin gideceği mesafeyi belirler.(px olarak)
#     t.left(90) # left ile sola 90 derece açıyla döndü.
#     time.sleep(1)
#     t.forward(75)
#     t.left(90)
#     time.sleep(1)
#     t.forward(75)
#     t.left(90)
#     time.sleep(1)
#     t.forward(75)
#
#     for i in range(4): # ==> for döngüsü ile yapımı
#         t.right(90)
#         t.forward(200)
#
#     for i in range(4):
#         t.right(90)
#         t.forward(210)
#
#     for i in range(4):
#         t.right(90)
#         t.forward(220)
#
#     t.backward(350)
#
#     time.sleep(2)
#     break


############ ALIŞTIRMA #############
# import turtle
# import time

# while True:
#     t = turtle.Turtle()
#     form = turtle.Screen()
#     t.shape('turtle')
#     t.color('red', 'green')
#     form.bgcolor('black')
#     t.forward(100)
#
#     for i in range(3):
#         t.left(90)
#         time.sleep(0.5)
#         t.forward(100)
#
#     t.forward(50)
#
#     time.sleep(2)
#     break


############# HAREKETLERİ AYARLAMA VE BOYAMA ##################
import turtle
import time

#print(help(turtle.speed))

while True:
    t = turtle.Turtle()
    t.speed(4) # ==> Hızı ayarlar. Sayı arttıkça hız da artar.
    form = turtle.Screen()
    form.title('BOYAMA')
    t.shape('turtle')
    t.begin_fill() # begin_fill ile end_fill arasındaki işler tamamlandıktan sonra çalışır.
    t.fillcolor('green')
    for i in range(4):
        t.forward(200)
        time.sleep(0.5)
        t.left(90)
    t.end_fill()

    time.sleep(0.6)
    break

####################### DAİRE ÇİZME #########################
# import turtle
# import time

# print(help(turtle.circle)) # Üç argüman alır. Birinci: Yarıçap      İkinci: Açı            Üçüncü: Step ==> Kaç adım gideceği(gen sayısı)

# while True:
#     t = turtle.Turtle()
#     form = turtle.Screen()
#     form.title('Daire')
#     form.bgcolor('white')
#     t.color('red', 'green')

#     # t.circle(100)
#     # t.circle(100,90)
#     t.circle(100,steps=4)

#     time.sleep(1)
#     break

############### UYGULAMA ####################
# import turtle
# import time
#
# while True:
#     t = turtle.Turtle()
#     form = turtle.Screen()
#     form.title('UYGULAMA')
#     form.bgcolor('blue')
#     t.speed(10)
#
#     for i in range(100):
#         if i % 2 == 0:
#             t.color('yellow')
#             t.circle(i, steps=5)
#         elif i%5 == 0:
#             t.color('gray')
#             t.circle(i)
#         else:
#             t.color('red')
#             t.circle(i)
#
#     time.sleep(1)
#     break


####### up, down, goto fonksiyonları ########
# import turtle
# import time
#
# while True:
#     t = turtle.Turtle()
#     form = turtle.Screen()
#     form.title('UP, DOWN, GOTO')
#     form.bgcolor('gray')
#     t.shape('arrow')
#     t.color('green', 'red')
#     t.speed(1)
#     # t.goto(100,100) # ==> Bulunduğu konumdan belirtilen x(ilk paramatre) ve y(ikinci parametre) koordinatlarına gider.
#     # t.up() # ==> Kalemi kaldırır.
#     # t.down() # ==> Kalemi indirir.
#
#     # t.up()   # ==> Konuma direkt(çizgisiz) gidildi.
#     # t.goto(100,100)
#
#     t.forward(50)
#     t.up()
#     t.forward(50)
#     t.down()
#     t.forward(100)
#     t.up()
#     t.goto(60,100)
#     t.down()
#     t.forward(50)
#
#     time.sleep(1)
#
#     break

################# ALIŞTIRMA ####################
# import turtle
# import time
# while True:
#     t = turtle.Turtle()
#     form = turtle.Screen()
#     t.shape('arrow')
#     t.color('green', 'blue')
#     form.bgcolor('red')
#     t.speed(1)
#     t.circle(40)
#     t.up()
#     t.goto(-100,100)
#     t.down()
#     t.circle(40)
#
#     time.sleep(1)
#     break


############### ALIŞTIRMA ##################
#
# import turtle
# import time
#
# while True:
#     t = turtle.Turtle()
#     form = turtle.Screen()
#     form.title('Alıstırma')
#     form.bgcolor('white')
#     t.speed(1)
#     t.shape('arrow')
#     t.color('red', 'blue')
#
#     t.begin_fill()
#     t.fillcolor('orange')
#     t.up()
#     t.goto(-100,100)
#     t.down()
#     t.circle(50)
#     t.end_fill()
#
#
#     t.up()
#     t.goto(150,100)
#     t.down()
#     t.begin_fill()
#     t.fillcolor('black')
#     for i in range(4):
#         t.left(90)
#         t.forward(100)
#     t.end_fill()
#
#     time.sleep(1)
#
#     break













