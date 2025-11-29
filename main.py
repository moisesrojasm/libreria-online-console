from servicios.servicio_autenticacion import iniciar_sesion, registrar_usuario
from servicios.servicio_carrito import crear_carrito
from servicios.servicio_libros import obtener_libros
from servicios.servicio_pedidos import obtener_pedidos

def menu_principal():
    while True:
        print("\n=== LIBRERÍA ONLINE ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = iniciar_sesion()
            if usuario:
                if usuario["es_admin"]:
                    menu_administrador(usuario)
                else:
                    menu_cliente(usuario)
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

def menu_administrador(usuario):
    while True:
        print("\n=== PANEL ADMINISTRADOR ===")
        print("1. Ver catálogo")
        print("2. Agregar libro")
        print("3. Editar libro")
        print("4. Eliminar libro")
        print("5. Buscar libros")
        print("6. Ver pedidos")
        print("7. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        # Llamadas a funciones del servicio de libros y pedidos

        if opcion == "7":
            break

def menu_cliente(usuario):
    carrito = crear_carrito(usuario["id"])

    while True:
        print("\n=== MENÚ CLIENTE ===")
        print("1. Ver catálogo")
        print("2. Buscar libros")
        print("3. Filtrar por categoría")
        print("4. Agregar al carrito")
        print("5. Ver carrito")
        print("6. Confirmar pedido")
        print("7. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        # Llamadas a funciones de carrito, libros y pedidos

        if opcion == "7":
            break

if __name__ == "__main__":
    menu_principal()
