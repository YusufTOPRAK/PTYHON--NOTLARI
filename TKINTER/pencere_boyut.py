# import tkinter as tk
# form = tk.Tk()
# form.title('Pencere')
#
# form.geometry('500x250+470+200')
# ### geometry ###
# '''
# Yazılan ilk iki değer pencerenin boyutunu belirler. İlki x ekseni ikincisi y ekseni için
# Son iki değer formun ekrandaki konumunu belirler. İlki x ekseni ikincisi y ekseni için
# '''
# form.resizable(False, True) # ==> Ekran büyüklüğü erişimini kaldırır. İlk değer x ekseni, ikinci değer y ekseni içindir.
#
# # form.minsize(450,400) # ==> Minimum ekran büyüklüğü belirlenir.
# # form.maxsize(550,500) # ==> Maksimum ekran büyüklüğü belirlenir.
#
# form.mainloop()

################### Pencere Durumları #######################
# import tkinter as tk
# form = tk.Tk()
#
# form.state('normal')
# '''
# normal ==> Belirtilen boyutta açılır.
# zoomed ==> Tam ekran yapar.
# iconic ==> Çalışır ama altta ikon olarak gelir ekrana ikon tıklanmadığı sürece gelmez.
# '''
# form.wm_attributes('-alpha',0.3) # ==> Formu saydam yapar. 1'den küçük değer almalıdır.
#
# form.mainloop()