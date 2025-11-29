# libreria-online-console
Sistema de librería online en consola con carrito de compras y gestión de libros.

´´´´plain text

libreria_online/
│
├── main.py          # Punto de entrada: muestra menús y orquesta todo
│
├── datos/                          # Archivos JSON persistentes
│   ├── libros.json
│   ├── usuarios.json
│   └── pedidos.json               # Opcional pero muy elegante
│
├── funciones/                     # Lógica de negocio (no interfaz)
│   ├── auth_service.py            # Registro / login / gestión de usuarios
│   ├── book_service.py            # Gestión de libros (CRUD + búsquedas)
│   ├── cart_service.py            # Manejo del carrito en memoria
│   └── order_service.py           # Finalizar compra y registrar pedidos
│
└── utils/
    └── json_utils.py              # Cargar/guardar JSON de forma genérica


´´´