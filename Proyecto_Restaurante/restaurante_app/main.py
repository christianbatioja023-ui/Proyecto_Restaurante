# Importar las clases necesarias

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Crear el restaurante
restaurante = Restaurante()

# Crear productos
producto1 = Producto(
    "Hamburguesa Especial",
    5.99,
    20,
    True
)

producto2 = Producto(
    "Jugo Natural",
    2.50,
    15,
    True
)

# Crear clientes
cliente1 = Cliente(
    "Carlos Perez",
    25,
    "carlos@email.com",
    True
)

cliente2 = Cliente(
    "Maria Lopez",
    30,
    "maria@email.com",
    True
)

# Agregar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
restaurante.mostrar_productos()
restaurante.mostrar_clientes()