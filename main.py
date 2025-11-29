from servicios.servicio_autenticacion import iniciar_sesion, registrar_usuario
from servicios import servicio_libros
from servicios.servicio_carrito import crear_carrito, agregar_al_carrito, quitar_del_carrito, mostrar_carrito
from servicios.servicio_pedidos import generar_pedido, obtener_pedidos, obtener_pedidos_usuario

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
                if usuario.get("es_admin"):
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

        if opcion == "1":
            libros = servicio_libros.obtener_libros(solo_activos=False)
            servicio_libros.mostrar_catalogo(libros)
        elif opcion == "2":
            servicio_libros.agregar_libro()
        elif opcion == "3":
            servicio_libros.editar_libro()
        elif opcion == "4":
            servicio_libros.eliminar_libro()
        elif opcion == "5":
            palabra = input("Ingrese palabra a buscar: ")
            resultados = servicio_libros.buscar_libros(palabra)
            servicio_libros.mostrar_catalogo(resultados)
        elif opcion == "6":
            pedidos = obtener_pedidos()
            if not pedidos:
                print("No hay pedidos registrados.")
            else:
                print("\n=== LISTA DE PEDIDOS ===")
                for pedido in pedidos:
                    print(
                        f"ID Pedido: {pedido.get('id')} | Usuario ID: {pedido.get('usuario_id')} "
                        f"| Total: ${pedido.get('total')} | Fecha: {pedido.get('fecha')}"
                    )
        elif opcion == "7":
            print("Cerrando sesión de administrador...")
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
        print("6. Confirmar pedido")
        print("7. Ver mis pedidos")
        print("8. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            libros = servicio_libros.obtener_libros()
            servicio_libros.mostrar_catalogo(libros)
        elif opcion == "2":
            palabra = input("Ingrese palabra a buscar: ")
            resultados = servicio_libros.buscar_libros(palabra)
            servicio_libros.mostrar_catalogo(resultados)
        elif opcion == "3":
            categoria = input("Ingrese categoría: ")
            resultados = servicio_libros.filtrar_por_categoria(categoria)
            servicio_libros.mostrar_catalogo(resultados)
        elif opcion == "4":
            try:
                id_libro = int(input("ID del libro a agregar al carrito: ").strip())
                cantidad = int(input("Cantidad: ").strip())
            except ValueError:
                print("Datos inválidos.")
                continue
            libro = servicio_libros.buscar_libro_por_id(id_libro)
            if libro is None or not libro.get("activo", True):
                print("No se encontró un libro activo con ese ID.")
            else:
                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")
                elif cantidad > libro.get("stock", 0):
                    print("No hay suficiente stock.")
                else:
                    agregar_al_carrito(carrito, id_libro, cantidad)
        elif opcion == "5":
            libros = servicio_libros.obtener_libros(solo_activos=False)
            mostrar_carrito(carrito, libros)
        elif opcion == "6":
            libros = servicio_libros.obtener_libros(solo_activos=False)
            if not carrito["items"]:
                print("El carrito está vacío, no se puede generar un pedido.")
            else:
                pedido = generar_pedido(carrito, libros)
                if pedido:
                    carrito["items"] = []
        elif opcion == "7":
            pedidos = obtener_pedidos_usuario(usuario["id"])
            if not pedidos:
                print("No tienes pedidos registrados.")
            else:
                print("\n=== MIS PEDIDOS ===")
                for pedido in pedidos:
                    print(
                        f"ID Pedido: {pedido.get('id')} | Total: ${pedido.get('total')} | "
                        f"Fecha: {pedido.get('fecha')}"
                    )
        elif opcion == "8":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()
