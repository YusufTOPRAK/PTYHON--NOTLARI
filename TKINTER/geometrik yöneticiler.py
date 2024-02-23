# import tkinter as tk
#
# form = tk.Tk()
# form.geometry('500x250+450+200')
#
# label=tk.Label(form,text='Geometrik Yöneticiler',bg='yellow')
# label.pack(side=tk.RIGHT) # ==> side ile yön belirlenir.
# '''
# TOP: Üste konumlandırır.
# BOTTOM: Aşağı konumlandırır.
# RIGHT: Sağa konumlandırır.
# LEFT: Sola konumlandırır.
# '''
#
# buton = tk.Button(text='Pack()',fg='red',bg='black')
# buton.pack(fill=tk.X) # ==> Buton x ekseni boyunca genişledi. y ekseni için side ile kullanılmalı.
#
# buton2 = tk.Button(text='Pack2()',bg='gray')
# buton2.pack(side=tk.LEFT,fill=tk.Y,expand=tk.YES) # ==> y ekseni için side ile kullanılmalı. expand ile tk.YES veya 1 kullanılarak y ekseninde ortaya buton ortaya konumlandırılır.
#
# form.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------#
# import tkinter as tk
#
# form = tk.Tk()
# form.geometry('500x250+450+200')
#
# buton = tk.Button(text='Pack()',fg='red',bg='black')
# buton.pack(padx=20,pady=50) # ==> Buton ile kenarlar arasındaki mesafeyi ayarlamak için kullanılır.
#
# buton2 = tk.Button(text='Pack()',fg='white',bg='gray')
# buton2.pack(ipadx=100,ipady=250) # ==> Butonun kenar kalınlığını ayarlar.
#
# form.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------------#
# import tkinter as tk
# form = tk.Tk()
# form.title('ANCHOR')
# form.geometry('500x350+350+150')
#
# buton = tk.Button(form,text='Tıkla',fg='yellow',bg='green',command=print('A'))
# buton.pack(expand=1,anchor='sw')
#
# buton = tk.Button(form,text='Tıkla',fg='yellow',bg='green',command=print('A'),anchor='e') # ==> Tıkla yazısı için kullanılan anchor
# buton.pack(expand=1,ipadx=15,ipady=10,anchor='sw')
#
# #ANCHOR#
# '''
# n ==> Yukarı
# s ==> Aşağı
# e ==> Sağ
# w ==> Sol
# ne ==> Yukarı Sağ
# se ==> Aşağı sağ
# nw ==> Yukarı sol
# sw ==> Aşağı sol
# '''
#
# form.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------------#
### PLACE ###
# import tkinter as tk
# form = tk.Tk()
# form.title('PLACE')
# form.geometry('500x350+250+50')
#
# def yaz():
#     print('Place örneği')
#
# buton = tk.Button(form,text='TIKLA',fg='yellow',bg='green',font='Arial',command=yaz)
# #buton.place(x=140,y=120) # ==> Konum ayarlanır.
# #buton.place(relx=0.5,rely=0.5) # ==> Konuma göre butonu dinamikleştirmek için kullanılır. Yüzdelik değer alır.
# buton.place(width=150,heigh=60) # ==> Genişlik ve uzunluğu ayarlar.
#
# form.mainloop()
