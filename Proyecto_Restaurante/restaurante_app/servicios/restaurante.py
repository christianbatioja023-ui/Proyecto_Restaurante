# Clase que administra los productos y clientes

class Restaurante:
    def __init__(self):
        # Lista de productos registrados
        self.productos = []

        # Lista de clientes registrados
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\n=== PRODUCTOS REGISTRADOS ===")
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self):
        print("\n=== CLIENTES REGISTRADOS ===")
        for cliente in self.clientes:
            print(cliente)