def crear_carrito(usuario_id):
    return {
        "usuario_id": usuario_id,
        "items": []
    }

def agregar_al_carrito(carrito, libros):
    print("\n=== AGREGAR AL CARRITO ===")
    id_texto = input("ID del libro: ")
    cantidad_texto = input("Cantidad: ")

    try:
        id_libro = int(id_texto)
        cantidad = int(cantidad_texto)
    except ValueError:
        print("ID o cantidad inválidos.")
        return

    libro_encontrado = None
    for libro in libros:
        if libro["id"] == id_libro and libro.get("activo", True):
            libro_encontrado = libro
            break

    if libro_encontrado is None:
        print("No se encontró un libro activo con ese ID.")
        return

    if libro_encontrado.get("stock", 0) < cantidad:
        print("No hay stock suficiente.")
        return

    for item in carrito["items"]:
        if item["libro_id"] == id_libro:
            item["cantidad"] += cantidad
            print("Cantidad actualizada en el carrito.")
            return

    carrito["items"].append({
        "libro_id": id_libro,
        "cantidad": cantidad
    })
    print("Libro agregado al carrito.")

def quitar_del_carrito(carrito):
    print("\n=== QUITAR DEL CARRITO ===")
    id_texto = input("ID del libro a quitar: ")

    try:
        id_libro = int(id_texto)
    except ValueError:
        print("ID inválido.")
        return

    for item in carrito["items"]:
        if item["libro_id"] == id_libro:
            carrito["items"].remove(item)
            print("Libro eliminado del carrito.")
            return

    print("El libro no está en el carrito.")

def calcular_total(carrito, libros):
    total = 0.0
    for item in carrito["items"]:
        libro_id = item["libro_id"]
        cantidad = item["cantidad"]
        for libro in libros:
            if libro["id"] == libro_id:
                total += libro["precio"] * cantidad
                break
    return total

def mostrar_carrito(carrito, libros):
    print("\n=== CARRITO DE COMPRAS ===")
    if not carrito["items"]:
        print("El carrito está vacío.")
        return

    for item in carrito["items"]:
        libro_id = item["libro_id"]
        cantidad = item["cantidad"]
        libro = None
        for l in libros:
            if l["id"] == libro_id:
                libro = l
                break
        if libro:
            print(f"ID: {libro_id} | {libro['titulo']} x {cantidad} = ${libro['precio'] * cantidad}")
    total = calcular_total(carrito, libros)
    print(f"\nTotal: ${total}")
