import tkinter as tk

diccionario = {}

def agregar():
    es = entrada_es.get().lower()
    en = entrada_en.get().lower()

    if es == "" or en == "":
        resultado.set("Completa ambos campos")
    else:
        diccionario[es] = en
        resultado.set("Palabra agregada")

def traducir():
    palabra = entrada_buscar.get().lower()

    if palabra == "":
        resultado.set("Escribe una palabra")
        return

    if opcion.get() == 1:
        # Español → Inglés
        resultado.set(diccionario.get(palabra, "No encontrado"))
    else:
        # Inglés → Español
        for es, en in diccionario.items():
            if palabra == en:
                resultado.set(es)
                return
        resultado.set("No encontrado")

def limpiar():
    entrada_es.delete(0, tk.END)
    entrada_en.delete(0, tk.END)
    entrada_buscar.delete(0, tk.END)
    resultado.set("")

ventana = tk.Tk()
ventana.title("Traductor ES - EN")
ventana.geometry("400x400")

tk.Label(ventana, text="Traducir").pack(pady=10)

entrada_buscar = tk.Entry(ventana)
entrada_buscar.pack()

opcion = tk.IntVar()
opcion.set(1)

tk.Radiobutton(ventana, text="Español → Inglés", variable=opcion, value=1).pack()
tk.Radiobutton(ventana, text="Inglés → Español", variable=opcion, value=2).pack()

tk.Label(ventana, text="Agregar palabra").pack(pady=5)

tk.Label(ventana, text="Español").pack()
entrada_es = tk.Entry(ventana)
entrada_es.pack()

tk.Label(ventana, text="Inglés").pack()
entrada_en = tk.Entry(ventana)
entrada_en.pack()

tk.Button(ventana, text="Agregar", command=agregar).pack(pady=5)

tk.Button(ventana, text="Traducir", command=traducir).pack(pady=5)
tk.Button(ventana, text="Limpiar", command=limpiar).pack()

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack(pady=10)

ventana.mainloop()
