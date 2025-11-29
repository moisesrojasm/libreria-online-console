from utilidades.utilidades_json import cargar_json, guardar_json
import os

RUTA_LIBROS = os.path.join("datos", "libros.json")

def obtener_libros():
    return cargar_json(RUTA_LIBROS)

def guardar_libros(libros):
    guardar_json(RUTA_LIBROS, libros)

def obtener_siguiente_id_libro(libros):
    if not libros:
        return 1
    ids = [l.get("id", 0) for l in libros]
    return max(ids) + 1

def mostrar_catalogo():
    print("\n=== CATÁLOGO DE LIBROS ===")
    libros = obtener_libros()
    if not libros:
        print("No hay libros registrados.")
        return

    for libro in libros:
        if not libro.get("activo", True):
            continue
        print(f"ID: {libro['id']}")
        print(f"  Título: {libro['titulo']}")
        print(f"  Autor: {libro['autor']}")
        print(f"  Categoría: {libro['categoria']}")
        print(f"  Precio: ${libro['precio']}")
        print(f"  Stock: {libro.get('stock', 0)}")
        print("-" * 30)

def agregar_libro():
    print("\n=== AGREGAR LIBRO ===")
    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoría: ")
    precio_texto = input("Precio: ")
    stock_texto = input("Stock: ")

    try:
        precio = float(precio_texto)
        stock = int(stock_texto)
    except ValueError:
        print("Precio o stock inválidos.")
        return

    libros = obtener_libros()
    nuevo_id = obtener_siguiente_id_libro(libros)

    nuevo_libro = {
        "id": nuevo_id,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "activo": True
    }

    libros.append(nuevo_libro)
    guardar_libros(libros)
    print("Libro agregado con éxito.")

def buscar_libros():
    print("\n=== BÚSQUEDA DE LIBROS ===")
    palabra = input("Ingrese una palabra (título, autor o categoría): ").lower()

    libros = obtener_libros()
    encontrados = []

    for libro in libros:
        if not libro.get("activo", True):
            continue
        texto = f"{libro['titulo']} {libro['autor']} {libro['categoria']}".lower()
        if palabra in texto:
            encontrados.append(libro)

    if not encontrados:
        print("No se encontraron libros que coincidan.")
        return

    print(f"\nSe encontraron {len(encontrados)} libro(s):")
    for libro in encontrados:
        print(f"ID: {libro['id']} | {libro['titulo']} - {libro['autor']} (${libro['precio']})")

def filtrar_por_categoria():
    print("\n=== FILTRAR POR CATEGORÍA ===")
    categoria = input("Categoría: ").lower()

    libros = obtener_libros()
    encontrados = []

    for libro in libros:
        if not libro.get("activo", True):
            continue
        if libro["categoria"].lower() == categoria:
            encontrados.append(libro)

    if not encontrados:
        print("No se encontraron libros de esa categoría.")
        return

    for libro in encontrados:
        print(f"ID: {libro['id']} | {libro['titulo']} - {libro['autor']} (${libro['precio']})")

def editar_libro():
    print("\n=== EDITAR LIBRO ===")
    id_texto = input("ID del libro a editar: ")
    try:
        id_libro = int(id_texto)
    except ValueError:
        print("ID inválido.")
        return

    libros = obtener_libros()
    libro = None
    for l in libros:
        if l["id"] == id_libro:
            libro = l
            break

    if libro is None:
        print("No se encontró un libro con ese ID.")
        return

    print("Deja en blanco si no quieres cambiar el campo.")
    nuevo_titulo = input(f"Título ({libro['titulo']}): ")
    nuevo_autor = input(f"Autor ({libro['autor']}): ")
    nueva_categoria = input(f"Categoría ({libro['categoria']}): ")
    nuevo_precio = input(f"Precio ({libro['precio']}): ")
    nuevo_stock = input(f"Stock ({libro.get('stock', 0)}): ")

    if nuevo_titulo:
        libro["titulo"] = nuevo_titulo
    if nuevo_autor:
        libro["autor"] = nuevo_autor
    if nueva_categoria:
        libro["categoria"] = nueva_categoria
    if nuevo_precio:
        try:
            libro["precio"] = float(nuevo_precio)
        except ValueError:
            print("Precio inválido, se mantiene el anterior.")
    if nuevo_stock:
        try:
            libro["stock"] = int(nuevo_stock)
        except ValueError:
            print("Stock inválido, se mantiene el anterior.")

    guardar_libros(libros)
    print("Libro actualizado con éxito.")

def eliminar_libro():
    print("\n=== ELIMINAR (DESACTIVAR) LIBRO ===")
    id_texto = input("ID del libro a eliminar: ")
    try:
        id_libro = int(id_texto)
    except ValueError:
        print("ID inválido.")
        return

    libros = obtener_libros()
    for libro in libros:
        if libro["id"] == id_libro:
            libro["activo"] = False
            guardar_libros(libros)
            print("Libro desactivado con éxito.")
            return

    print("No se encontró un libro con ese ID.")
