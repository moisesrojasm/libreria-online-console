import json
import os

# Cargar los datos de un archivo JSON y regresa una lista o diccionario 
def cargar_json(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []

# Guardar los datos en un archivo JSON
def guardar_json(ruta, datos):
    carpeta = os.path.dirname(ruta)
    if carpeta and not os.path.exists(carpeta):
        os.makedirs(carpeta, exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
