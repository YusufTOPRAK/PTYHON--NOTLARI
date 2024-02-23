import tkinter as tk

form=tk.Tk()
form.title('ENTRY DERSİ')
form.geometry('500x450+250+250')

giris=tk.Entry(form,fg='black',bg='white')
giris.pack(side=tk.LEFT)
form.mainloop()

# ------------------------------UYGULAMA-----------------------------------#
import tkinter as tk
form= tk.Tk()
form.title('Çalışma')
form.geometry('500x350')

email = tk.Label(form,text='email:',fg='red',bg='black',font='Arial')
email.place(x=10,y=30)

email_entry= tk.Entry(form,bg='gray')
email_entry.place(x=60,y=33)

sifre = tk.Label(form,text='şifre:',fg='red',bg='black',font='Arial')
sifre.place(x=10,y=60)

sifre_entry= tk.Entry(form,bg='gray')
sifre_entry.place(x=60,y=63)

giris_buton= tk.Button(form,text='Giriş Yap')
giris_buton.place(x=60,y=85)



def kayit():
    email = tk.Label(form, text='email:', fg='red', bg='black', font='Arial')
    email.place(x=10, y=130)

    email_entry = tk.Entry(form, bg='gray')
    email_entry.place(x=60, y=133)

    sifre = tk.Label(form, text='şifre:', fg='red', bg='black', font='Arial')
    sifre.place(x=10, y=160)

    sifre_entry = tk.Entry(form, bg='gray')
    sifre_entry.place(x=60, y=163)

kayit_buton= tk.Button(form,text='Kayıt Ol',command=kayit)
kayit_buton.place(x=130,y=85)

form.mainloop()