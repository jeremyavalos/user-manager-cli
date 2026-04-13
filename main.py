from funciones import *
#programa
 
while True:
    print("\n--- MENU ---")
    print("1. crear usaurio")
    print("2. ver usuarios")
    print("3. buscar usuario")
    print("4. eliminar usuario")
    print("5. editar usuario")
    print("6. salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("nombre: ") 
        edad = input("edad: ")
        guardar_datos(nombre, edad)

    elif opcion == "2":
        ver_usuarios()

    elif opcion == "3":
        buscar_usuario()
     
    elif opcion == "4":
        eliminar_usuario()

    elif opcion == "5":
        editar_usuario()

    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")
