from tkinter import *
from romanos import *
root = Tk()
root.geometry("550x400")
root.title("Números Romanos")
root.iconbitmap("img/romanos.ico")
root.config(background="gray17")

def convertir():
	numero_convertido = numero_romano(numero.get())
	salida.set(numero_convertido)


label = Label(root, text="CONVERSOR DE NÚMEROS ROMANOS",bg="gray17", fg="white", font=("Helvetica 16"))
label.grid(row=0, column=0, pady=25, columnspan=2)

label2 = Label(root, text="Ingrese un número", width=20,bg="gray17", fg="white", font=("Helvetica 14"))
label2.grid(row=1, column=0, padx=15, pady=10)


numero = IntVar()
ingreso_numero = Entry(root, textvariable=numero, width=20,bg="gray21", fg="white", relief=FLAT, font=("Helvetica 14"))
ingreso_numero.grid(row=1, column=1, padx=15, pady=25)

boton = Button(root, text="Convertir", command=convertir, width=55, relief=FLAT,bg="BLACK", fg="white", font=("Helvetica 12"))
boton.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

salida=StringVar()
salida_numero_romano = Label(root, text="", textvariable=salida,bg="gray17", fg="white", font=("Times New Roman",25))
salida_numero_romano.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()