# Clase que representa un producto del restaurante

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int, disponible: bool):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.disponible = disponible

    def __str__(self):
        return (
            f"Producto: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Cantidad: {self.cantidad} | "
            f"Disponible: {self.disponible}"
        )