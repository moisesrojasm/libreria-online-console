from utilidades.utilidades_json import cargar_json, guardar_json
import os

RUTA_USUARIOS = os.path.join("datos", "usuarios.json")

def cargar_usuarios():
    return cargar_json(RUTA_USUARIOS)

def guardar_usuarios(usuarios):
    guardar_json(RUTA_USUARIOS, usuarios)

def obtener_siguiente_id_usuario(usuarios):
    if not usuarios:
        return 1
    ids = [u.get("id", 0) for u in usuarios]
    return max(ids) + 1

def registrar_usuario():
    print("\n=== REGISTRO DE USUARIO ===")
    nombre = input("Nombre completo: ")
    correo = input("Correo electrónico: ")
    password = input("Contraseña: ")
    direccion = input("Dirección: ")

    usuarios = cargar_usuarios()

    # Validar que el correo no exista ya
    for usuario in usuarios:
        if usuario["correo"] == correo:
            print("Ya existe un usuario registrado con ese correo.")
            return

    nuevo_id = obtener_siguiente_id_usuario(usuarios)

    # Si no hay usuarios, el primero es admin
    es_admin = False
    if not usuarios:
        print("Primer usuario registrado. Lo marcaré como administrador.")
        es_admin = True

    nuevo_usuario = {
        "id": nuevo_id,
        "nombre": nombre,
        "correo": correo,
        "password": password,
        "direccion": direccion,
        "es_admin": es_admin
    }

    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)

    print("Usuario registrado con éxito.")

def iniciar_sesion():
    print("\n=== INICIAR SESIÓN ===")
    correo = input("Correo: ")
    password = input("Contraseña: ")

    usuarios = cargar_usuarios()

    for usuario in usuarios:
        if usuario["correo"] == correo and usuario["password"] == password:
            print(f"\nBienvenido, {usuario['nombre']}.")
            return usuario

    print("Correo o contraseña incorrectos.")
    return None

# Solo para administradores (mostrar y modificar roles)
def administrar_usuarios():
    usuarios = cargar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print("\n=== USUARIOS REGISTRADOS ===")
    for u in usuarios:
        rol = "ADMIN" if u.get("es_admin", False) else "CLIENTE"
        print(f"ID: {u['id']} | {u['nombre']} | {u['correo']} | Rol: {rol}")

    opcion = input("\n¿Desea cambiar los privilegios de algún usuario? (s/n): ").lower()
    if opcion != "s":
        return

    id_texto = input("Ingrese el ID del usuario: ")
    try:
        id_usuario = int(id_texto)
    except ValueError:
        print("ID inválido.")
        return

    usuario_objetivo = None
    for u in usuarios:
        if u["id"] == id_usuario:
            usuario_objetivo = u
            break

    if usuario_objetivo is None:
        print("No se encontró un usuario con ese ID.")
        return

    print(f"\nUsuario: {usuario_objetivo['nombre']} ({usuario_objetivo['correo']})")
    rol_actual = "ADMIN" if usuario_objetivo.get("es_admin", False) else "CLIENTE"
    print(f"Rol actual: {rol_actual}")

    respuesta = input("¿Debe ser administrador? (s/n): ").lower()
    if respuesta == "s":
        usuario_objetivo["es_admin"] = True
    else:
        usuario_objetivo["es_admin"] = False

    guardar_usuarios(usuarios)
    print("Privilegios actualizados con éxito.")

# Para clientes y administradores
def editar_mis_datos(usuario):
    print("\n=== EDITAR MIS DATOS ===")
    print("Deja en blanco cualquier campo que no quieras cambiar.\n")

    print(f"Nombre actual: {usuario['nombre']}")
    nuevo_nombre = input("Nuevo nombre: ")

    print(f"Correo actual: {usuario['correo']}")
    nuevo_correo = input("Nuevo correo: ")

    print(f"Dirección actual: {usuario['direccion']}")
    nueva_direccion = input("Nueva dirección: ")

    cambiar_password = input("¿Deseas cambiar la contraseña? (s/n): ").lower()
    nuevo_password = ""
    if cambiar_password == "s":
        nuevo_password = input("Nueva contraseña: ")

    usuarios = cargar_usuarios()

    if nuevo_correo:
        for u in usuarios:
            if u["correo"] == nuevo_correo and u["id"] != usuario["id"]:
                print("Ese correo ya está siendo usado por otro usuario. No se cambia el correo.")
                nuevo_correo = ""  # cancelar cambio
                break

    if nuevo_nombre:
        usuario["nombre"] = nuevo_nombre
    if nuevo_correo:
        usuario["correo"] = nuevo_correo
    if nueva_direccion:
        usuario["direccion"] = nueva_direccion
    if nuevo_password:
        usuario["password"] = nuevo_password

    for u in usuarios:
        if u["id"] == usuario["id"]:
            u["nombre"] = usuario["nombre"]
            u["correo"] = usuario["correo"]
            u["direccion"] = usuario["direccion"]
            u["password"] = usuario["password"]
            break

    guardar_usuarios(usuarios)
    print("Datos actualizados con éxito.")

    return usuario
