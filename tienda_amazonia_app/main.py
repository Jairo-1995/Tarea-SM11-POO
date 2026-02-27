# main.py
from servicios.inventario import Inventario


def mostrar_menu():
    """Muestra el menú principal del sistema."""

    print("""
==============================================================
🛒  SISTEMA DE GESTIÓN DE INVENTARIOS🗃️ - 🍌PRODUCTOS AMAZÓNICOS📋
==============================================================
    1. ➕ Añadir nuevo producto 🍇
    2. ❌ Eliminar producto por ID 🗑️
    3. 🔄 Actualizar cantidad o precio de producto🧾
    4. 🔍 Buscar y mostrar producto por nombre📜
    5. 📦 Mostrar todos los productos en el inventario🗃️
    6. 💰 Consultar valor total del inventario💵
    7. 🚪 Salir del sistema🚶‍➡️
============================================================
    """)

def obtener_numero_positivo(mensaje, es_entero=False):
    """Valida que el usuario ingrese un número positivo."""
    while True:
        try:
            valor = input(mensaje).strip()
            if not valor:
                print("❗ Error: El valor no puede estar vacío.")
                continue
            if es_entero:
                numero = int(valor)
            else:
                numero = float(valor)
            if numero < 0:
                print("Error: El número debe ser no negativo.")
                continue
            return numero
        except ValueError:
            tipo = "entero" if es_entero else "número decimal"
            print(f"❗ Error: Ingresa un {tipo} válido.")


def obtener_texto_requerido(mensaje):
    """Valida que el usuario ingrese un texto no vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("❗ Error: Este campo no puede estar vacío.")


def obtener_id():
    """Obtiene un ID válido del usuario."""
    return obtener_texto_requerido("Ingresa ID único del producto: ")


def agregar_producto(inventario):
    """Permite agregar un nuevo producto al inventario."""
    print("\n--- AÑADIR NUEVO PRODUCTO ---")
    try:
        id_producto = obtener_id()
        nombre = obtener_texto_requerido("Nombre del producto (ej. Aguaje, Cacao): ")
        categoria = obtener_texto_requerido("Categoría (ej. Frutas, Semillas, Especias): ")
        cantidad = int(obtener_numero_positivo("Cantidad en stock: ", es_entero=True))
        precio = obtener_numero_positivo("Precio por unidad ($): ")
        
        inventario.añadir_producto(id_producto, nombre, categoria, cantidad, precio)
    except KeyboardInterrupt:
        print("\n🚫 Operación cancelada.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def eliminar_producto(inventario):
    """Permite eliminar un producto del inventario."""
    print("\n--- ELIMINAR PRODUCTO ---")
    try:
        id_producto = obtener_id()
        inventario.eliminar_producto(id_producto)
    except KeyboardInterrupt:
        print("\n🚫 Operación cancelada.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def actualizar_producto(inventario):
    """Permite actualizar un producto existente."""
    print("\n--- ACTUALIZAR PRODUCTO ---")
    try:
        id_producto = obtener_id()
        print("(Deja vacío si no quieres cambiar algún campo)")
        
        categoria_str = input("Nueva categoría: ").strip()
        cantidad_str = input("Nueva cantidad: ").strip()
        precio_str = input("Nuevo precio: ").strip()
        
        nueva_categoria = categoria_str if categoria_str else None
        nueva_cantidad = None
        nuevo_precio = None
        
        if cantidad_str:
            try:
                nueva_cantidad = int(cantidad_str)
                if nueva_cantidad < 0:
                    print("❌ Error: La cantidad debe ser no negativa.")
                    return
            except ValueError:
                print("❌ Error: La cantidad debe ser un número entero.")
                return
        
        if precio_str:
            try:
                nuevo_precio = float(precio_str)
                if nuevo_precio < 0:
                    print("❌ Error: El precio debe ser no negativo.")
                    return
            except ValueError:
                print("❌ Error: El precio debe ser un número válido.")
                return
        
        inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio, nueva_categoria)
    except KeyboardInterrupt:
        print("\n⚠ Operación cancelada.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def buscar_producto(inventario):
    """Permite buscar productos por nombre."""
    print("\n--- BUSCAR PRODUCTO ---")
    try:
        nombre_parcial = obtener_texto_requerido("Ingresa el nombre (o parte de él) a buscar: ")
        inventario.buscar_productos(nombre_parcial)
    except KeyboardInterrupt:
        print("\n⚠ Operación cancelada.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def mostrar_inventario_completo(inventario):
    """Muestra todos los productos del inventario."""
    print("\n--- INVENTARIO COMPLETO ---")
    try:
        inventario.mostrar_inventario()
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def consultar_valor_total(inventario):
    """Muestra el valor total del inventario."""
    print("\n--- VALOR TOTAL DEL INVENTARIO ---")
    try:
        inventario.calcular_valor_total()
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def main():
    """Función principal del programa."""
    inventario = Inventario()
    print("\n✅ Sistema iniciado. Inventario cargado correctamente.")
    
    while True:
        try:
            mostrar_menu()
            opcion = input("\nSelecciona una opción (1-7): ").strip()
            
            if opcion == "1":
                agregar_producto(inventario)
            elif opcion == "2":
                eliminar_producto(inventario)
            elif opcion == "3":
                actualizar_producto(inventario)
            elif opcion == "4":
                buscar_producto(inventario)
            elif opcion == "5":
                mostrar_inventario_completo(inventario)
            elif opcion == "6":
                consultar_valor_total(inventario)
            elif opcion == "7":
                print("\n" + "=" * 60)
                print("🙏 Gracias por usar el Sistema de Gestión de Inventarios.")
                print("👋 ¡Hasta luego!")
                print("=" * 60)
                break
            else:
                print("❌ Opción inválida. Por favor, selecciona una opción entre 1 y 7.")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"❌ Error inesperado en el programa principal: {e}")


if __name__ == "__main__":
    main()