from utilidades.utilidades_json import cargar_json, guardar_json
import os

RUTA_USUARIOS = os.path.join("datos", "usuarios.json")

def cargar_usuarios():
    return cargar_json(RUTA_USUARIOS)

def guardar_usuarios(usuarios):
    guardar_json(RUTA_USUARIOS, usuarios)

def registrar_usuario():
    # Pasos del registro
    pass

def iniciar_sesion():
    # Pasos del login
    pass
