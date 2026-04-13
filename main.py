import funciones

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
       while True:
        edad = input("edad: ")
        
        if edad.isdigit():
          break
        else:
          print("Por favor, ingresa un número válido.")
       funciones.guardar_datos(nombre, edad)
    
    elif opcion == "2":
       funciones.ver_usuarios()

    elif opcion == "3":
       funciones.buscar_usuario()
    
    elif opcion == "4":
       funciones.eliminar_usuario()

    elif opcion == "5":
       funciones.editar_usuario()

    elif opcion == "6":
      print("¡Hasta luego!")
      break

    else:
      print("Opción no válida. Por favor, selecciona una opción del menú.")
