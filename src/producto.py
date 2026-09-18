"""Módulo de modelo de datos para la entidad Producto."""


class Producto:
    """Clase que representa un producto del inventario bajo normas PEP 8."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio_unitario: float,
        cantidad: int,
    ):
        """Inicializa los atributos principales del producto."""
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    def calcular_valor_total_stock(self) -> float:
        """Calcula el valor monetario total del inventario para este producto."""
        return self.precio_unitario * self.cantidad

    def a_diccionario(self) -> dict:
        """Convierte la entidad en un diccionario nativo para la serialización JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio_unitario": self.precio_unitario,
            "cantidad": self.cantidad,
            "valor_total_stock": self.calcular_valor_total_stock(),
        }