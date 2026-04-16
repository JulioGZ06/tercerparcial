import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import os

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

precio = 5
dinero = 0

stock_coca = 5
stock_fanta = 5
stock_sprite = 5
stock_sidral = 5
stock_aga = 5
stock_jarrito = 5

imagen = None


def actualizar():
    label_dinero.configure(text="Dinero: $" + str(dinero))
    label_precio.configure(text="Precio por refresco: $" + str(precio))

    if dinero >= precio:
        rb_coca.configure(state="normal")
        rb_fanta.configure(state="normal")
        rb_sprite.configure(state="normal")
        rb_sidral.configure(state="normal")
        rb_aga.configure(state="normal")
        rb_jarrito.configure(state="normal")
        btn_comprar.configure(state="normal")
    else:
        rb_coca.configure(state="disabled")
        rb_fanta.configure(state="disabled")
        rb_sprite.configure(state="disabled")
        rb_sidral.configure(state="disabled")
        rb_aga.configure(state="disabled")
        rb_jarrito.configure(state="disabled")
        btn_comprar.configure(state="disabled")

    mostrar_stock()


def mostrar_stock():
    texto = "Coca: " + str(stock_coca) + "\n"
    texto += "Fanta: " + str(stock_fanta) + "\n"
    texto += "Sprite: " + str(stock_sprite) + "\n"
    texto += "Sidral: " + str(stock_sidral) + "\n"
    texto += "Aga: " + str(stock_aga) + "\n"
    texto += "Jarrito: " + str(stock_jarrito)

    label_stock.configure(text=texto)


def meter_dinero(cantidad):
    global dinero
    dinero += cantidad
    actualizar()


def ingresar_dinero():
    try:
        cantidad = float(entrada_dinero.get())

        if cantidad in [0.5, 1, 2, 5, 10]:
            meter_dinero(cantidad)
            entrada_dinero.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Moneda no válida")
    except:
        messagebox.showerror("Error", "Ingresa un número válido")


def ver_imagen(nombre):
    global imagen

    try:
        ruta = os.path.join("IMG", nombre)
        img = Image.open(ruta)
        img = img.resize((200,150))
        imagen = ImageTk.PhotoImage(img)
        label_imagen.configure(image=imagen, text="")
    except:
        label_imagen.configure(text="No hay imagen", image="")


def comprar():
    global dinero
    global stock_coca, stock_fanta, stock_sprite, stock_sidral, stock_aga, stock_jarrito

    seleccion = opcion.get()

    if seleccion == "":
        messagebox.showerror("Error", "Elige un refresco")
        return

    if dinero < precio:
        messagebox.showerror("Error", "No alcanza el dinero")
        return

    if seleccion == "Coca":
        if stock_coca <= 0:
            messagebox.showerror("Error", "No hay Coca")
            return
        stock_coca -= 1

    elif seleccion == "Fanta":
        if stock_fanta <= 0:
            messagebox.showerror("Error", "No hay Fanta")
            return
        stock_fanta -= 1

    elif seleccion == "Sprite":
        if stock_sprite <= 0:
            messagebox.showerror("Error", "No hay Sprite")
            return
        stock_sprite -= 1

    elif seleccion == "Sidral":
        if stock_sidral <= 0:
            messagebox.showerror("Error", "No hay Sidral")
            return
        stock_sidral -= 1

    elif seleccion == "Aga":
        if stock_aga <= 0:
            messagebox.showerror("Error", "No hay Aga")
            return
        stock_aga -= 1

    elif seleccion == "Jarrito":
        if stock_jarrito <= 0:
            messagebox.showerror("Error", "No hay Jarrito")
            return
        stock_jarrito -= 1

    cambio = dinero - precio
    dinero = 0

    messagebox.showinfo("Compra", "Disfruta tu refresco\nCambio: $" + str(cambio))

    opcion.set("")
    label_imagen.configure(image="")
    actualizar()


def surtir():
    global stock_coca, stock_fanta, stock_sprite, stock_sidral, stock_aga, stock_jarrito

    nombre = simpledialog.askstring("Surtir", "Coca / Fanta / Sprite / Sidral / Aga / Jarrito")

    try:
        cantidad = int(simpledialog.askstring("Cantidad", "¿Cuántos?"))
        if cantidad < 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Número inválido")
        return

    if nombre == "Coca":
        stock_coca += cantidad
    elif nombre == "Fanta":
        stock_fanta += cantidad
    elif nombre == "Sprite":
        stock_sprite += cantidad
    elif nombre == "Sidral":
        stock_sidral += cantidad
    elif nombre == "Aga":
        stock_aga += cantidad
    elif nombre == "Jarrito":
        stock_jarrito += cantidad
    else:
        messagebox.showerror("Error", "Nombre incorrecto")

    actualizar()


def cambiar_precio():
    global precio

    try:
        nuevo = float(simpledialog.askstring("Precio", "Nuevo precio"))
        if nuevo < 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Precio inválido")
        return

    precio = nuevo
    actualizar()


ventana = ctk.CTk()
ventana.title("Maquina de Refrescos")
ventana.geometry("400x750")

ventana.columnconfigure(0, weight=1)

menu = tk.Menu(ventana)
ventana.config(menu=menu)

opciones = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Opciones", menu=opciones)
opciones.add_command(label="Surtir", command=surtir)
opciones.add_command(label="Cambiar precio", command=cambiar_precio)

label_dinero = ctk.CTkLabel(ventana, text="Dinero: $0")
label_dinero.grid(row=0, column=0, pady=10)

ctk.CTkLabel(ventana, text="Ingresa moneda (0.5, 1, 2, 5, 10)").grid(row=1, column=0)

entrada_dinero = ctk.CTkEntry(ventana)
entrada_dinero.grid(row=2, column=0, pady=5)

ctk.CTkButton(ventana, text="Ingresar dinero", command=ingresar_dinero).grid(row=3, column=0, pady=5)

label_precio = ctk.CTkLabel(ventana, text="", font=("Arial", 12, "bold"))
label_precio.grid(row=4, column=0, pady=5)

opcion = tk.StringVar()

rb_coca = ctk.CTkRadioButton(ventana, text="Coca", variable=opcion, value="Coca", state="disabled", command=lambda: ver_imagen("coca.png"))
rb_coca.grid(row=5, column=0, sticky="w")

rb_fanta = ctk.CTkRadioButton(ventana, text="Fanta", variable=opcion, value="Fanta", state="disabled", command=lambda: ver_imagen("fanta.png"))
rb_fanta.grid(row=6, column=0, sticky="w")

rb_sprite = ctk.CTkRadioButton(ventana, text="Sprite", variable=opcion, value="Sprite", state="disabled", command=lambda: ver_imagen("sprite.png"))
rb_sprite.grid(row=7, column=0, sticky="w")

rb_sidral = ctk.CTkRadioButton(ventana, text="Sidral", variable=opcion, value="Sidral", state="disabled", command=lambda: ver_imagen("sidral.png"))
rb_sidral.grid(row=8, column=0, sticky="w")

rb_aga = ctk.CTkRadioButton(ventana, text="Aga", variable=opcion, value="Aga", state="disabled", command=lambda: ver_imagen("aga.png"))
rb_aga.grid(row=9, column=0, sticky="w")

rb_jarrito = ctk.CTkRadioButton(ventana, text="Jarrito", variable=opcion, value="Jarrito", state="disabled", command=lambda: ver_imagen("jarrito.png"))
rb_jarrito.grid(row=10, column=0, sticky="w")

label_imagen = ctk.CTkLabel(ventana, text="")
label_imagen.grid(row=11, column=0, pady=10)

btn_comprar = ctk.CTkButton(ventana, text="Tomar refresco", state="disabled", command=comprar)
btn_comprar.grid(row=12, column=0, pady=10)

label_stock = ctk.CTkLabel(ventana, text="")
label_stock.grid(row=13, column=0, pady=10)

actualizar()

ventana.mainloop()
