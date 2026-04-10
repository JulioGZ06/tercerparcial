import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import os


signos_chinos = {
    "Rata": "rata.png",
    "Buey": "buey.png",
    "Tigre": "tigre.png",
    "Conejo": "conejo.png",
    "Dragón": "dragon.png",
    "Serpiente": "serpiente.png",
    "Caballo": "caballo.png",
    "Cabra": "cabra.png",
    "Mono": "mono.png",
    "Gallo": "gallo.png",
    "Perro": "perro.png",
    "Cerdo": "cerdo.png"
}

def imprimir():
    try:
        nombre = entry_nombre.get()
        ap = entry_ap.get()
        am = entry_am.get()

        if nombre == "" or ap == "" or am == "":
            messagebox.showerror("Error", "Llena todos los campos")
            return

        if sexo.get() == "":
            messagebox.showerror("Error", "Selecciona un sexo")
            return

        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        anio = int(entry_anio.get())

        try:
            fecha_nacimiento = datetime(anio, mes, dia)
        except:
            messagebox.showerror("Error", "Fecha inválida")
            return

        hoy = datetime.now()
        edad = hoy.year - fecha_nacimiento.year
        if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1

        if mes == 1 or (mes == 2 and dia < 4):
            anio -= 1

        animales = list(signos_chinos.keys())
        indice = (anio - 1900) % 12
        signo = animales[indice]

        gen = "Masculino" if sexo.get() == "M" else "Femenino"

        resultado.set(f"Hola {nombre} {ap} {am}\n"
                      f"Sexo: {gen}\n"
                      f"Tienes {edad} años\n"
                      f"Tu signo chino es: {signo}")

        carpeta = "imagenes/"
        archivo_img = carpeta + signos_chinos[signo]


        img = Image.open(archivo_img)
        img = img.resize((120, 120))
        img_tk = ImageTk.PhotoImage(img)

        label_img.config(image=img_tk)
        label_img.image = img_tk

    except ValueError:
        messagebox.showerror("Error", "Ingresa números válidos en fecha")
    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Error", "Ocurrió un error")


def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_ap.delete(0, tk.END)
    entry_am.delete(0, tk.END)
    entry_dia.delete(0, tk.END)
    entry_mes.delete(0, tk.END)
    entry_anio.delete(0, tk.END)

    resultado.set("")
    label_img.config(image=None)
    label_img.image = None
    sexo.set("")


ventana = tk.Tk()
ventana.title("ZODIACO")
ventana.geometry("500x400")

frame1 = tk.Frame(ventana)
frame1.pack(side="left", padx=20, pady=20)

tk.Label(frame1, text="Nombre").pack()
entry_nombre = tk.Entry(frame1)
entry_nombre.pack()

tk.Label(frame1, text="Apellido Paterno").pack()
entry_ap = tk.Entry(frame1)
entry_ap.pack()

tk.Label(frame1, text="Apellido Materno").pack()
entry_am = tk.Entry(frame1)
entry_am.pack()

tk.Label(frame1, text="Día").pack()
entry_dia = tk.Entry(frame1)
entry_dia.pack()

tk.Label(frame1, text="Mes").pack()
entry_mes = tk.Entry(frame1)
entry_mes.pack()

tk.Label(frame1, text="Año").pack()
entry_anio = tk.Entry(frame1)
entry_anio.pack()

sexo = tk.StringVar()
tk.Radiobutton(frame1, text="Masculino", variable=sexo, value="M").pack()
tk.Radiobutton(frame1, text="Femenino", variable=sexo, value="F").pack()

tk.Button(frame1, text="Imprimir", command=imprimir).pack(pady=5)
tk.Button(frame1, text="Limpiar", command=limpiar).pack(pady=5)

frame2 = tk.Frame(ventana)
frame2.pack(side="right", padx=20, pady=20)

resultado = tk.StringVar()
tk.Label(frame2, textvariable=resultado, justify="left").pack()

label_img = tk.Label(frame2)
label_img.pack()

ventana.mainloop()
