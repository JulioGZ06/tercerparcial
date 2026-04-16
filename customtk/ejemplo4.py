import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
      
        self.title("My App")
        self.geometry("400x250")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
      
        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
      
        self.checkbox_1 = customtkinter.CTkCheckBox(self.checkbox_frame, text="Checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
      
        self.checkbox_2 = customtkinter.CTkCheckBox(self.checkbox_frame, text="Checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
      
        self.button = customtkinter.CTkButton(self, text="Mostrar selección", command=self.button_callback)
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
      
    def button_callback(self):
        seleccionados = []
        
        if self.checkbox_1.get():
            seleccionados.append("Checkbox 1")
        if self.checkbox_2.get():
            seleccionados.append("Checkbox 2")
        
        if seleccionados:
            print("Seleccionados:", ", ".join(seleccionados))
        else:
            print("Ninguno seleccionado")


app = App()
app.mainloop()
