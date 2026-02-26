# servicios/inventario.py
import os
from modelos.producto import Producto

class Inventario:
    FILE_NAME = os.path.join(os.path.dirname(__file__), 'data', 'inventario.txt')
    
    # ==================== CONSTRUCTOR ====================
    # Se ejecuta automáticamente cuando se crea una instancia de la clase
    # Inicializa la lista de productos y carga datos del archivo
    def __init__(self):
        """Inicializa el inventario y carga los productos desde el archivo."""
        self._productos = []  # Lista para almacenar productos
        self._cargar_inventario()

    def _cargar_inventario(self):
        """
        Carga los productos desde el archivo de inventario.
        Maneja excepciones como archivo no encontrado, permisos, o datos corruptos.
        """
        try:
            with open(self.FILE_NAME, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split(',')
                        if len(parts) == 5:
                            id, nombre, categoria, cantidad, precio = parts
                        elif len(parts) == 4:
                            id, nombre, cantidad, precio = parts
                            categoria = "Sin categoría"
                        else:
                            print(f"Advertencia: Línea corrupta en archivo de inventario ignorada: {line}")
                            continue
                        try:
                            cantidad = int(cantidad)
                            precio = float(precio)
                            producto = Producto(id, nombre, cantidad, precio, categoria)
                            self._productos.append(producto)
                        except ValueError:
                            print(f"Advertencia: Línea corrupta en archivo de inventario ignorada: {line}")
            print("Inventario cargado exitosamente desde archivo.✅")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo al añadir productos.")
        except PermissionError:
            print("Error de permisos al leer el archivo de inventario.❌")
        except Exception as e:
            print(f"Error inesperado al cargar inventario: {e}")

    def _guardar_inventario(self):
        """
        Guarda todos los productos en el archivo de inventario.
        Retorna True si exitoso, False si hay error.
        """
        try:
            with open(self.FILE_NAME, 'w', encoding='utf-8') as f:
                for producto in self._productos:
                    f.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_categoria()},{producto.get_cantidad()},{producto.get_precio()}\n")
            return True
        except PermissionError:
            print("Error de permisos al guardar el inventario.❌")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar inventario: {e}")
            return False

    def _buscar_indice_por_id(self, id):
        """
        Busca el índice de un producto por su ID en la lista.
        Retorna el índice si lo encuentra, -1 si no existe.
        """
        for indice, producto in enumerate(self._productos):
            if producto.get_id() == id:
                return indice
        return -1

    def añadir_producto(self, id, nombre, categoria, cantidad, precio):
        # Validaciones
        if not isinstance(cantidad, int) or cantidad < 0:
            print("Error❌: Cantidad debe ser un entero no negativo.")
            return False
        if not isinstance(precio, (int, float)) or precio < 0:
            print("Error❌: Precio debe ser un número no negativo.")
            return False
        if self._buscar_indice_por_id(id) != -1:
            print("Este número ya existe.")
            return False
        
        nuevo_producto = Producto(id, nombre, cantidad, precio, categoria)
        self._productos.append(nuevo_producto)
        
        if self._guardar_inventario():
            print(f"Producto '{nombre}' añadido exitosamente y guardado en archivo.")
        else:
            print(f"Producto '{nombre}' añadido, pero error al guardar en archivo.")
        return True

    def eliminar_producto(self, id):
        indice = self._buscar_indice_por_id(id)
        if indice != -1:
            self._productos.pop(indice)
            
            if self._guardar_inventario():
                print(f"Producto con ID {id} eliminado y cambios guardados en archivo.")
            else:
                print(f"Producto con ID {id} eliminado, pero error al guardar en archivo.")
            return True
        print(f"Error: No se encontró un producto con ID {id}.")
        return False

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None, nueva_categoria=None):
        indice = self._buscar_indice_por_id(id)
        if indice == -1:
            print(f"Error: No se encontró un producto con ID {id}.")
            return False
        
        producto = self._productos[indice]
        cambios_realizados = False
        
        if nueva_cantidad is not None:
            if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
                print("Error: Nueva cantidad debe ser un entero no negativo.")
                return False
            producto.set_cantidad(nueva_cantidad)
            cambios_realizados = True
        
        if nuevo_precio is not None:
            if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
                print("Error: Nuevo precio debe ser un número no negativo.")
                return False
            producto.set_precio(nuevo_precio)
            cambios_realizados = True
        
        if nueva_categoria is not None:
            producto.set_categoria(nueva_categoria)
            cambios_realizados = True
        
        if not cambios_realizados:
            print(f"Advertencia: No se realizaron cambios en el producto con ID {id}.")
            return False
        
        if self._guardar_inventario():
            print(f"Producto con ID {id} actualizado y cambios guardados en archivo.")
        else:
            print(f"Producto con ID {id} actualizado, pero error al guardar en archivo.")
        return True

    def buscar_productos(self, nombre_parcial):
        resultados = []
        for producto in self._productos:
            if nombre_parcial.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        if resultados:
            print("Producto encontrado:")
            for prod in resultados:
                print(prod)
        else:
            print(f"No se encontraron productos con '{nombre_parcial}' en el nombre.")
        return resultados

    def mostrar_inventario(self):
        if not self._productos:
            print("===El inventario está vacío.===")
        else:
            print("===Inventario completo de productos Amazónicos===")
            for producto in self._productos:
                print(producto)

    def get_product_by_id(self, id):
        indice = self._buscar_indice_por_id(id)
        if indice != -1:
            return self._productos[indice]
        return None

    def calcular_valor_total(self):
        total = sum(producto.get_cantidad() * producto.get_precio() for producto in self._productos)
        print(f"Valor total del inventario: ${total:.2f}")
        return total

    # ==================== DESTRUCTOR ====================
    # Se ejecuta automáticamente cuando la instancia es eliminada
    # Realiza limpieza de recursos y guarda el estado final
    def __del__(self):
        """Destructor: se ejecuta cuando el objeto es eliminado de la memoria.
        
        Guarda la última versión del inventario en el archivo antes de finalizar.
        """
        try:
            self._guardar_inventario()
        except Exception:
            pass  # Evitar excepciones en el destructor

