
# modelos/producto.py
# Clase base para productos de la tienda amazónica
class Producto:
    # ==================== CONSTRUCTOR ====================
    # Se ejecuta automáticamente cuando se crea una instancia de la clase
    # Inicializa los atributos del producto
    def __init__(self, id, nombre, cantidad, precio, categoria):
        """Inicializa un nuevo producto con sus atributos."""
        self._id = id  # ID único
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio
        self._categoria = categoria

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def get_categoria(self):
        return self._categoria

    # Setters
    def set_id(self, id):
        self._id = id

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def set_categoria(self, categoria):
        self._categoria = categoria

    # Método para representar el producto como string (útil para imprimir)
    def __str__(self):
        return f"ID: {self._id}  | Nombre: {self._nombre}  | Categoría: {self._categoria}  | Cantidad: {self._cantidad}  | Precio: {self._precio:.2f}"

    # ==================== DESTRUCTOR ====================
    # Se ejecuta automáticamente cuando la instancia es eliminada
    # Limpia recursos y realiza tareas de finalización
    def __del__(self):
        """Destructor: se ejecuta cuando el objeto es eliminado de la memoria."""
        pass  # En Python, rara vez se necesita implementar lógica aqui
             # Python maneja automáticamente la limpieza de memoria