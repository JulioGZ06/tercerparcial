import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Diccionario de imágenes
signos_chinos = {
    "Rata": "rata.png",
    "Buey": "buey.png",
    "Tigre": "tigre.png",
    "Conejo": "conejo.png",
    "Dragon": "dragon.png",
    "Serpiente": "serpiente.png",
    "Caballo": "caballo.png",
    "Cabra": "cabra.png",
    "Mono": "mono.png",
    "Gallo": "gallo.png",
    "Perro": "perro.png",
    "Cerdo": "cerdo.png"
}

ventana = tk.Tk()
ventana.title("ZODIACO CHINO")
ventana.geometry("500x400")


imagenes = {}
for signo, archivo in signos_chinos.items():
    try:
        img = Image.open(archivo)
        img = img.resize((120, 120))
        imagenes[signo] = ImageTk.PhotoImage(img)
    except Exception as e:
        print("Error cargando:", archivo, e)
        imagenes[signo] = None


def calcular():
    try:
        nombre = entrada_nombre.get()
        paterno = entrada_paterno.get()
        materno = entrada_materno.get()
        ano = int(entrada_anio.get())
        mes = int(entrada_mes.get())
        dia = int(entrada_dia.get())

        if nombre == "" or paterno == "" or materno == "":
            messagebox.showerror("Error", "Completa todos los datos")
            return

        if sexo.get() == "":
            messagebox.showerror("Error", "Selecciona un sexo")
            return
        
        signos = ["Mono", "Gallo", "Perro", "Cerdo", "Rata", "Buey",
                  "Tigre", "Conejo", "Dragon", "Serpiente", "Caballo", "Cabra"]

        signo = signos[ano % 12]

        # Fecha actual
        dia_actual = 27
        mes_actual = 3
        anio_actual = 2026

        edad = anio_actual - ano

        if (mes_actual, dia_actual) < (mes, dia):
            edad -= 1

        genero = "Masculino" if sexo.get() == "M" else "Femenino"

        label_resultado.config(
            text=f"Hola {nombre} {paterno} {materno}\n"
                 f"Sexo: {genero}\n"
                 f"Tienes {edad} años\n"
                 f"Tu signo zodiacal es:\n{signo}"
        )

        label_imagen.config(image=imagenes[signo])
        label_imagen.image = imagenes[signo]

    except:
        messagebox.showerror("Error", "Datos inválidos")


def limpiar():
    entrada_nombre.delete(0, tk.END)
    entrada_paterno.delete(0, tk.END)
    entrada_materno.delete(0, tk.END)
    entrada_dia.delete(0, tk.END)
    entrada_mes.delete(0, tk.END)
    entrada_anio.delete(0, tk.END)

    label_resultado.config(text="")
    label_imagen.config(image=None)
    label_imagen.image = None
    sexo.set("")


# Frame izquierdo
frame1 = tk.Frame(ventana)
frame1.pack(side="left", padx=20, pady=20)

tk.Label(frame1, text="Nombre").pack()
entrada_nombre = tk.Entry(frame1)
entrada_nombre.pack()

tk.Label(frame1, text="Apellido Paterno").pack()
entrada_paterno = tk.Entry(frame1)
entrada_paterno.pack()

tk.Label(frame1, text="Apellido Materno").pack()
entrada_materno = tk.Entry(frame1)
entrada_materno.pack()

tk.Label(frame1, text="Día").pack()
entrada_dia = tk.Entry(frame1)
entrada_dia.pack()

tk.Label(frame1, text="Mes").pack()
entrada_mes = tk.Entry(frame1)
entrada_mes.pack()

tk.Label(frame1, text="Año").pack()
entrada_anio = tk.Entry(frame1)
entrada_anio.pack()

# Sexo
sexo = tk.StringVar()

tk.Label(frame1, text="Sexo").pack()
tk.Radiobutton(frame1, text="Masculino", variable=sexo, value="M").pack()
tk.Radiobutton(frame1, text="Femenino", variable=sexo, value="F").pack()

tk.Button(frame1, text="Calcular", command=calcular).pack(pady=5)
tk.Button(frame1, text="Limpiar", command=limpiar).pack(pady=5)

# Frame derecho
frame2 = tk.Frame(ventana)
frame2.pack(side="right", padx=20, pady=20)

label_resultado = tk.Label(frame2, text="", justify="left")
label_resultado.pack()

label_imagen = tk.Label(frame2)
label_imagen.pack()

ventana.mainloop()
