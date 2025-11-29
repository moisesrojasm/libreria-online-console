from servicios.servicio_autenticacion import iniciar_sesion, registrar_usuario, administrar_usuarios, editar_mis_datos
from servicios.servicio_carrito import crear_carrito, agregar_al_carrito, quitar_del_carrito, mostrar_carrito
from servicios.servicio_libros import mostrar_catalogo, agregar_libro, editar_libro, eliminar_libro, buscar_libros, filtrar_por_categoria, obtener_libros
from servicios.servicio_pedidos import generar_pedido, mostrar_pedidos, mostrar_pedidos_usuario

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
        print("6. Filtrar por categoría")
        print("7. Ver historial de pedidos")
        print("8. Ver / modificar usuarios")
        print("9. Editar mis datos")
        print("10. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_catalogo()
        elif opcion == "2":
            agregar_libro()
        elif opcion == "3":
            editar_libro()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "5":
            buscar_libros()
        elif opcion == "6":
            filtrar_por_categoria()
        elif opcion == "7":
            mostrar_pedidos()
        elif opcion == "8":
            administrar_usuarios()
        elif opcion == "9":
            usuario = editar_mis_datos(usuario)
        elif opcion == "10":
            break
        else:
            print("Opción no válida.")

def menu_cliente(usuario):
    carrito = crear_carrito(usuario["id"])

    while True:
        print("\n=== MENÚ CLIENTE ===")
        print("1. Ver catálogo")
        print("2. Buscar libros")
        print("3. Filtrar por categoría")
        print("4. Agregar al carrito")
        print("5. Ver carrito")
        print("6. Quitar del carrito")
        print("7. Confirmar pedido")
        print("8. Ver mis pedidos")
        print("9. Editar mis datos")
        print("10. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_catalogo()
        elif opcion == "2":
            buscar_libros()
        elif opcion == "3":
            filtrar_por_categoria()
        elif opcion == "4":
            libros = obtener_libros()
            agregar_al_carrito(carrito, libros)
        elif opcion == "5":
            libros = obtener_libros()
            mostrar_carrito(carrito, libros)
        elif opcion == "6":
            quitar_del_carrito(carrito)
        elif opcion == "7":
            generar_pedido(carrito)
        elif opcion == "8":
            mostrar_pedidos_usuario(usuario["id"])
        elif opcion == "9":
            usuario = editar_mis_datos(usuario)
        elif opcion == "10":
            break
        else:
            print("No es una opción válida.")

if __name__ == "__main__":
    menu_principal()
