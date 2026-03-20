'''
manejo de archivos de texto
Apertura de archivos
   open("archivo.txt", "r")

Modos Principales:

Modo Descripción
r     Leer
w     Escribir (sobrescribe)
a     Agregar
x     Crear archivo

***** Lectura de archivos
    * archivo.read()
    * archivo.readline()
    * archivo.readlines()

***** Escritura de archivos
    * archivo.write("Texto a escribir")
    * archivo.writelines(["Línea1\n", "Línea2\n"])
'''

def crear_archivo():
    nombre=input ("Nombre del archivo: ")
    with open(nombre,"w") as archivo: 
     '''
     with para que mande llamar el archivo y cuando
     abro el archivo y dejo de usarlo lo cierra
     '''
    print("Archivo creado correctamente")

crear_archivo()

def Escribir_archivos():
    nombre=input("Nombre del archivo: ")
    texto=input("Escribe el texto a guardar: ")
    
    with open(nombre, "w") as arvhivo:
        archivo.write(texto)
        
    print("Texto guardado correctamente")
    
Escribir_archivos