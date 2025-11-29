from utilidades.utilidades_json import cargar_json, guardar_json
import os

RUTA_PEDIDOS = os.path.join("datos", "pedidos.json")

def obtener_pedidos():
    return cargar_json(RUTA_PEDIDOS)

def guardar_pedidos(pedidos):
    guardar_json(RUTA_PEDIDOS, pedidos)

def generar_pedido(carrito, lista_libros):
    pass

def obtener_pedidos_usuario(usuario_id):
    pass
