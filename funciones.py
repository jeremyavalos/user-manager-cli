import json

#funciones

def guardar_datos(nombre, edad):
    try:
        with open("datos.json", "r") as archivo:
            usuarios = json.load(archivo)
            print("ANTES:", usuarios)
    except FileNotFoundError:
        usuarios = []
    except json.JSONDecodeError:
        usuarios = []

    # verificar si ya existe
    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre.lower():
            print("Usuario ya existe.")
            return

    # agregar nuevo usuario
    nuevo_usuario = {
        "nombre": nombre,
        "edad": int(edad)
    }

    usuarios.append(nuevo_usuario)

    with open("datos.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

    print("Usuario guardado correctamente.")

def ver_usuarios():
    import json

    try:
        with open("datos.json", "r") as archivo:
            usuarios = json.load(archivo)
    except:
        print("No hay usuarios guardados.")
        return

    if not usuarios:
        print("No hay usuarios guardados.")
        return

    print("\n--- USUARIOS ---")
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']} | Edad: {usuario['edad']}")
    
def buscar_usuario():
    import json

    nombre_buscar = input("Ingresa el nombre a buscar: ")

    try:
        with open("datos.json", "r") as archivo:
            usuarios = json.load(archivo)
    except:
        print("No hay usuarios guardados.")
        return

    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre_buscar.lower():
            print(f"Usuario encontrado: {usuario['nombre']} | Edad: {usuario['edad']}")
            return

    print("Usuario no encontrado.")

def eliminar_usuario():
    import json

    nombre_eliminar = input("Ingresa el nombre a eliminar: ")

    try:
        with open("datos.json", "r") as archivo:
            usuarios = json.load(archivo)
    except:
        print("No hay usuarios guardados.")
        return

    nuevos_usuarios = []
    eliminado = False

    for usuario in usuarios:
        if usuario["nombre"].lower() != nombre_eliminar.lower():
            nuevos_usuarios.append(usuario)
        else:
            eliminado = True

    with open("datos.json", "w") as archivo:
        json.dump(nuevos_usuarios, archivo, indent=4)

    if eliminado:
        print("Usuario eliminado correctamente.")
    else:
        print("Usuario no encontrado.")

def editar_usuario():
    import json

    nombre_editar = input("Ingresa el nombre del usuario a editar: ")

    try:
        with open("datos.json", "r") as archivo:
            usuarios = json.load(archivo)
    except:
        print("No hay usuarios guardados.")
        return

    encontrado = False

    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre_editar.lower():

            while True:
                nueva_edad = input("Ingresa la nueva edad: ")

                if nueva_edad.isdigit():
                    usuario["edad"] = int(nueva_edad)
                    break
                else:
                    print("Ingresa un número válido.")

            encontrado = True

    with open("datos.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

    if encontrado:
        print("Usuario actualizado correctamente.")
    else:
        print("Usuario no encontrado.")
        