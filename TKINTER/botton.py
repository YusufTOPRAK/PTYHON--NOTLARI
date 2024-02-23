# import tkinter as tk

# form = tk.Tk()
# form.title('Button')
# form.geometry('500x500+500+100')

# def topla():
#     print('Topla')

# buton = tk.Button(form,text='Tıkla',fg='white',bg='black',command=topla) # ==> command ile yapılcak işlem belirlenir.
# buton.pack(side=tk.LEFT)

# buton2= tk.Button(form,text='Tıkla2',command=topla)
# buton2.pack(side=tk.RIGHT)

# form.mainloop()


####################### UYGULAMA ######################
# import tkinter
# import tkinter as tk
# import random as rd

# form=tk.Tk()
# form.title('Title Uygulaması')
# form.geometry('500x400+500+350')

# liste=[]

# for i in range(5):
#     while len(liste)!=6:
#         a=rd.randint(1,50)
#         if a not in liste:
#             liste.append(a)

# def goster():
#     label.config(text=liste,bg='green')

# def saydam():
#     form.wm_attributes('-alpha',0.3)

# def dondur():
#     form.wm_attributes('-alpha', 0.9)

# def maxyap():
#     form.state('zoomed')
# def minyap():
#     form.state('iconic')

# label=tk.Label(form,fg='red',bg='red',font='Times 20 bold')
# label.pack()

# goster=tk.Button(form,text='göster',fg='black',bg='yellow',command=goster)
# goster.pack(side=tk.LEFT)

# saydam=tk.Button(form,text='saydamlaştır',fg='black',bg='yellow',command=saydam)
# saydam.pack(side=tk.LEFT)

# dondur=tk.Button(form,text='döndür',fg='black',bg='yellow',command=dondur)
# dondur.pack(side=tk.LEFT)

# max=tk.Button(form,text='Büyüt',fg='black',bg='yellow',command=maxyap)
# max.pack(side=tk.LEFT)

# min=tk.Button(form,text='Küçült',fg='black',bg='yellow',command=minyap)
# min.pack(side=tk.LEFT)
# form.mainloop()
