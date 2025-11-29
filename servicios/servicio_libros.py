from utilidades.utilidades_json import cargar_json, guardar_json
import os

RUTA_LIBROS = os.path.join("datos", "libros.json")

def obtener_libros():
    return cargar_json(RUTA_LIBROS)

def guardar_libros(libros):
    guardar_json(RUTA_LIBROS, libros)

def agregar_libro():
    pass

def actualizar_libro(id_libro, nuevos_datos):
    pass

def eliminar_libro(id_libro):
    pass

def buscar_libros(palabra):
    pass

def filtrar_por_categoria(categoria):
    pass
