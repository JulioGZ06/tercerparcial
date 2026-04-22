import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
import os

archivo = "ventas.txt"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pizzeria")
        self.geometry("1100x600")

        contenedor = ctk.CTkFrame(self)
        contenedor.pack(fill="both", expand=True)

        frame_izq = ctk.CTkFrame(contenedor)
        frame_izq.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        frame1 = ctk.CTkFrame(frame_izq)
        frame1.pack(pady=5)

        ctk.CTkLabel(frame1, text="Nombre").grid(row=0, column=0)
        self.nombre = ctk.CTkEntry(frame1)
        self.nombre.grid(row=0, column=1)

        ctk.CTkLabel(frame1, text="Direccion").grid(row=0, column=2)
        self.direccion = ctk.CTkEntry(frame1)
        self.direccion.grid(row=0, column=3)

        ctk.CTkLabel(frame1, text="Telefono").grid(row=0, column=4)
        self.telefono = ctk.CTkEntry(frame1)
        self.telefono.grid(row=0, column=5)

        ctk.CTkLabel(frame1, text="Fecha").grid(row=1, column=0)
        self.fecha = ctk.CTkEntry(frame1)
        self.fecha.grid(row=1, column=1)

        # ---------------- FRAME 2 ----------------
        frame2 = ctk.CTkFrame(frame_izq)
        frame2.pack(pady=5)

        self.tamano = tk.StringVar(value="Chica")

        ctk.CTkLabel(frame2, text="Tamaño").grid(row=0, column=0)
        ctk.CTkRadioButton(frame2, text="Chica $40", variable=self.tamano, value="Chica").grid(row=1, column=0)
        ctk.CTkRadioButton(frame2, text="Mediana $80", variable=self.tamano, value="Mediana").grid(row=2, column=0)
        ctk.CTkRadioButton(frame2, text="Grande $120", variable=self.tamano, value="Grande").grid(row=3, column=0)

        ctk.CTkLabel(frame2, text="Ingredientes").grid(row=0, column=1)

        self.jamon = tk.IntVar()
        self.pina = tk.IntVar()
        self.champ = tk.IntVar()

        ctk.CTkCheckBox(frame2, text="Jamon $10", variable=self.jamon).grid(row=1, column=1)
        ctk.CTkCheckBox(frame2, text="Piña $10", variable=self.pina).grid(row=2, column=1)
        ctk.CTkCheckBox(frame2, text="Champ $10", variable=self.champ).grid(row=3, column=1)

        ctk.CTkLabel(frame2, text="Cantidad").grid(row=0, column=2)
        self.cantidad = ctk.CTkEntry(frame2, width=60)
        self.cantidad.grid(row=1, column=2)

        ctk.CTkButton(frame2, text="Agregar", command=self.agregar).grid(row=2, column=2)

        # ---------------- FRAME 3 ----------------
        frame3 = ctk.CTkFrame(frame_izq)
        frame3.pack(pady=10)

        self.tabla = ttk.Treeview(frame3, columns=("tam","ing","cant","total"), show="headings")

        self.tabla.heading("tam", text="Tamaño")
        self.tabla.heading("ing", text="Ingredientes")
        self.tabla.heading("cant", text="Cantidad")
        self.tabla.heading("total", text="Total")

        self.tabla.pack()

        # ---------------- FRAME 4 ----------------
        frame4 = ctk.CTkFrame(frame_izq)
        frame4.pack(pady=5)

        ctk.CTkButton(frame4, text="Quitar", command=self.eliminar).pack(side="left", padx=5)
        ctk.CTkButton(frame4, text="Terminar", command=self.terminar).pack(side="left", padx=5)

        # ---------------- FRAME DERECHO ----------------
        frame5 = ctk.CTkFrame(contenedor, width=300)
        frame5.pack(side="right", fill="y", padx=10, pady=10)

        ctk.CTkLabel(frame5, text="Ventas del día").pack(pady=5)

        self.texto_ventas = ctk.CTkTextbox(frame5, width=280, height=500)
        self.texto_ventas.pack(pady=5)

        self.mostrar_ventas()

    def agregar(self):
        try:
            cant = int(self.cantidad.get())

            if cant <= 0:
                messagebox.showerror("Error", "La cantidad debe ser mayor a 0")
                return

        except:
            messagebox.showerror("Error", "Cantidad incorrecta")
            return

        if self.tamano.get() == "Chica":
            precio = 40
        elif self.tamano.get() == "Mediana":
            precio = 80
        else:
            precio = 120

        ing = ""

        if self.jamon.get():
            precio += 10
            ing += "Jamon "
        if self.pina.get():
            precio += 10
            ing += "Piña "
        if self.champ.get():
            precio += 10
            ing += "Champ "

        total = precio * cant

        self.tabla.insert("", tk.END, values=(self.tamano.get(), ing, cant, total))

        self.cantidad.delete(0, tk.END)

    def eliminar(self):
        for item in self.tabla.selection():
            self.tabla.delete(item)

    def terminar(self):
        if self.nombre.get() == "" or self.fecha.get() == "":
            messagebox.showerror("Error", "Faltan datos")
            return

        total = 0

        for item in self.tabla.get_children():
            datos = self.tabla.item(item)["values"]
            total += int(datos[3])

        with open(archivo, "a") as f:
            f.write(self.nombre.get() + "," + self.fecha.get() + "," + str(total) + "\n")

        messagebox.showinfo("Total", "Total a pagar: $" + str(total))

        # LIMPIAR TABLA
        self.tabla.delete(*self.tabla.get_children())

        # LIMPIAR CAMPOS
        self.nombre.delete(0, tk.END)
        self.direccion.delete(0, tk.END)
        self.telefono.delete(0, tk.END)
        self.fecha.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)

        # RESETEAR OPCIONES
        self.tamano.set("Chica")
        self.jamon.set(0)
        self.pina.set(0)
        self.champ.set(0)

        # ACTUALIZAR VENTAS
        self.mostrar_ventas()

    def mostrar_ventas(self):
        texto = ""
        suma = 0

        if os.path.exists(archivo):
            with open(archivo, "r") as f:
                for linea in f:
                    partes = linea.strip().split(",")

                    if len(partes) == 3:
                        nombre = partes[0]
                        fecha = partes[1]
                        total = partes[2]

                        texto += nombre + " (" + fecha + ") $" + total + "\n"
                        suma += int(total)

        texto += "\nTotal del día: $" + str(suma)

        self.texto_ventas.delete("1.0", tk.END)
        self.texto_ventas.insert("1.0", texto)


if __name__ == "__main__":
    app = App()
    app.mainloop()