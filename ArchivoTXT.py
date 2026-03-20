def crear_archivo():
    nombre = input("Nombre del archivo: ")
    
    with open(nombre, "w") as archivo:
        print("Archivo creado correctamente")


def escribir_archivo():
    nombre = input("Nombre del archivo: ")
    texto = input("Escribe el texto a guardar: ")
    
    with open(nombre, "w") as archivo:
        archivo.write(texto)
        
    print("Texto guardado correctamente")


def agregar_texto():
    nombre = input("Nombre del archivo: ")
    texto = input("Texto a agregar: ")
    
    with open(nombre, "a") as archivo:
        archivo.write("\n" + texto)
        
    print("Texto agregado correctamente")


def leer_archivo():
    nombre = input("Nombre del archivo: ")
    
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
            print("\nContenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo no existe")


def buscar_palabra():
    nombre = input("Nombre del archivo: ")
    palabra = input("Palabra a buscar: ")
    
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
            
            if palabra in contenido:
                print("La palabra fue encontrada")
            else:
                print("La palabra no se encuentra en el archivo")
                
    except FileNotFoundError:
        print("El archivo no existe")


def menu():
    while True:
        print("\n--- GESTOR DE ARCHIVOS ---")
        print("1. Crear archivo")
        print("2. Escribir en archivo")
        print("3. Agregar texto")
        print("4. Leer archivo")
        print("5. Buscar palabra")
        print("6. Salir")
        
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            escribir_archivo()
        elif opcion == "3":
            agregar_texto()
        elif opcion == "4":
            leer_archivo()
        elif opcion == "5":
            buscar_palabra()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")


menu()
