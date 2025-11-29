from utilidades.utilidades_json import cargar_json, guardar_json
from servicios.servicio_libros import obtener_libros, guardar_libros
from servicios.servicio_autenticacion import cargar_usuarios
import os
from datetime import datetime

RUTA_PEDIDOS = os.path.join("datos", "pedidos.json")

def obtener_pedidos():
    return cargar_json(RUTA_PEDIDOS)

def guardar_pedidos(pedidos):
    guardar_json(RUTA_PEDIDOS, pedidos)

def obtener_siguiente_id_pedido(pedidos):
    if not pedidos:
        return 1
    ids = [p.get("id", 0) for p in pedidos]
    return max(ids) + 1

def generar_pedido(carrito):
    libros = obtener_libros()
    if not carrito["items"]:
        print("El carrito está vacío. No se puede generar un pedido.")
        return None

    pedidos = obtener_pedidos()
    nuevo_id = obtener_siguiente_id_pedido(pedidos)

    items_pedido = []
    total = 0.0

    # Verificar stock y calcular total
    for item in carrito["items"]:
        libro_id = item["libro_id"]
        cantidad = item["cantidad"]

        libro_encontrado = None
        for libro in libros:
            if libro["id"] == libro_id:
                libro_encontrado = libro
                break

        if libro_encontrado is None or not libro_encontrado.get("activo", True):
            print(f"Libro con ID {libro_id} no disponible. Pedido cancelado.")
            return None

        if libro_encontrado.get("stock", 0) < cantidad:
            print(f"No hay stock suficiente para el libro '{libro_encontrado['titulo']}'. Pedido cancelado.")
            return None

        subtotal = libro_encontrado["precio"] * cantidad
        total += subtotal

        items_pedido.append({
            "libro_id": libro_id,
            "cantidad": cantidad,
            "precio_unitario": libro_encontrado["precio"]
        })

    # Quitar del stock
    for item in carrito["items"]:
        libro_id = item["libro_id"]
        cantidad = item["cantidad"]
        for libro in libros:
            if libro["id"] == libro_id:
                libro["stock"] -= cantidad
                break

    guardar_libros(libros)

    pedido = {
        "id": nuevo_id,
        "usuario_id": carrito["usuario_id"],
        "items": items_pedido,
        "total": total,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    pedidos.append(pedido)
    guardar_pedidos(pedidos)

    # Vaciar carrito
    carrito["items"].clear()

    print("\nPedido generado con éxito.")
    print(f"ID del pedido: {pedido['id']}")
    print(f"Total: ${pedido['total']}")
    print(f"Fecha: {pedido['fecha']}")
    return pedido

def mostrar_pedidos():
    print("\n=== HISTORIAL DE PEDIDOS ===")
    pedidos = obtener_pedidos()
    usuarios = cargar_usuarios()

    if not pedidos:
        print("No hay pedidos registrados.")
        return

    # Obtener el nombre
    def nombre_usuario(usuario_id):
        for u in usuarios:
            if u["id"] == usuario_id:
                return u["nombre"]
        return "Usuario desconocido"

    for pedido in pedidos:
        nombre = nombre_usuario(pedido["usuario_id"])
        print(f"\nID Pedido: {pedido['id']} | Hecho por: {nombre} | Total: ${pedido['total']} | Fecha: {pedido['fecha']}")
        print("Items:")
        for item in pedido["items"]:
            precio_unitario = item.get("precio_unitario", 0)
            print(f"  Libro ID: {item['libro_id']} x {item['cantidad']} (Precio unitario: ${precio_unitario})")


def mostrar_pedidos_usuario(usuario_id):
    print("\n=== MIS PEDIDOS ===")
    pedidos = obtener_pedidos()
    usuarios = cargar_usuarios()

    nombre_usuario = None
    for u in usuarios:
        if u["id"] == usuario_id:
            nombre_usuario = u["nombre"]
            break

    pedidos_usuario = [p for p in pedidos if p["usuario_id"] == usuario_id]

    if not pedidos_usuario:
        print("No tienes pedidos registrados.")
        return

    print(f"\nPedidos hechos por: {nombre_usuario}\n")

    for pedido in pedidos_usuario:
        print(f"ID Pedido: {pedido['id']} | Total: ${pedido['total']} | Fecha: {pedido['fecha']}")
        print("Items:")
        for item in pedido["items"]:
            precio_unitario = item.get("precio_unitario", 0)
            print(f"  Libro ID: {item['libro_id']} x {item['cantidad']} (Precio unitario: ${precio_unitario})")
        print()

