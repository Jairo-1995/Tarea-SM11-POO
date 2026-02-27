# 🛒 Sistema de Gestión de Inventarios

## 📖 Descripción Breve

Sistema de gestión de inventario en **Python con POO**. Permite administrar productos amazónicos con almacenamiento persistente en archivos CSV e interfaz interactiva.

**Características:**
- ✅ Operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
- ✅ Almacenamiento en archivos (Serialización/Deserialización)
- ✅ Colección con Listas (append, pop, enumerate)
- ✅ Validación de datos y manejo de errores
- ✅ Menú interactivo con validación de entrada

---

## 🚀 Ejecución Rápida

```bash
cd tienda_amazonia_app
python main.py
```

**Requisitos:** Python 3.7+ (sin librerías externas)

---

## 📁 Estructura del Proyecto

```
tienda_amazonia_app/
├── main.py                    # Interfaz de usuario (menú)
├── modelos/producto.py        # Clase Producto
├── servicios/inventario.py    # Clase Inventario + persistencia
├── servicios/data/
│   └── inventario.txt         # Base de datos (CSV)
└── DOCUMENTACION.md           # Guía técnica completa
```

---

## 🏛️ Arquitectura

**Clase Producto** (`modelos/producto.py`)
- Atributos: `_id`, `_nombre`, `_cantidad`, `_precio`, `_categoria`
- Métodos: `__init__()`, `__del__()`, getters/setters, `__str__()`

**Clase Inventario** (`servicios/inventario.py`)
- Colección: `self._productos = []` (LISTA de Productos)
- Métodos: `añadir()`, `eliminar()`, `actualizar()`, `buscar()`, `mostrar()`, `calcular_total()`
- Persistencia: `_cargar_inventario()`, `_guardar_inventario()`

---

## 💾 Colecciones (Listas)

### Operaciones Clave

| Operación | Método | Complejidad |
|-----------|--------|-------------|
| Agregar | `append()` | O(1) |
| Eliminar | `pop(índice)` | O(n) |
| Buscar | `enumerate() + for` | O(n) |
| Iterar | `for producto in lista` | O(n) |
| Suma | `sum(generator)` | O(n) |

### Ejemplos de Uso

```python
# AGREGAR PRODUCTO
self._productos.append(producto)

# BUSCAR POR ID
for indice, producto in enumerate(self._productos):
    if producto.get_id() == id_buscado:
        return indice

# ELIMINAR PRODUCTO
self._productos.pop(indice)

# MOSTRAR TODOS
for producto in self._productos:
    print(producto)

# CALCULAR VALOR TOTAL
total = sum(p.get_cantidad() * p.get_precio() for p in self._productos)
```

---

## 📊 Almacenamiento en Archivos

### Formato CSV

**Archivo:** `servicios/data/inventario.txt`

```
P001,Aguaje,Frutas Amazónicas,50,12.50
P002,Cacao,Semillas,100,8.75
P003,Açaí,Frutas Amazónicas,30,15.00
```

**Estructura:** `ID,Nombre,Categoría,Cantidad,Precio`

### Ciclo de Persistencia

```
INICIO
  ↓
_cargar_inventario()  ← Lee CSV → Deserializa → Crea Productos → Agrega a lista
  ↓
LISTA EN MEMORIA (self._productos)
  ↓
[Usuario realiza operación]
  ↓
_guardar_inventario() ← Itera lista → Serializa → Escribe en CSV
  ↓
FIN
```

### Deserialización (Cargando datos)

```python
def _cargar_inventario(self):
    with open(self.FILE_NAME, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            id, nombre, categoria, cantidad, precio = parts
            cantidad = int(cantidad)          # Conversión de tipo
            precio = float(precio)            # Conversión de tipo
            producto = Producto(id, nombre, cantidad, precio, categoria)
            self._productos.append(producto)  # Agregando a lista
```

### Serialización (Guardando datos)

```python
def _guardar_inventario(self):
    with open(self.FILE_NAME, 'w', encoding='utf-8') as f:
        for producto in self._productos:     # Iterando lista
            f.write(f"{producto.get_id()},"
                   f"{producto.get_nombre()},"
                   f"{producto.get_categoria()},"
                   f"{producto.get_cantidad()},"
                   f"{producto.get_precio()}\n")
```

---

## 📋 Menú Interactivo (7 Opciones)

```
🛒 SISTEMA DE GESTIÓN DE INVENTARIOS
  1. ➕ Añadir nuevo producto
  2. ❌ Eliminar producto por ID
  3. 🔄 Actualizar cantidad o precio
  4. 🔍 Buscar por nombre
  5. 📦 Mostrar inventario completo
  6. 💰 Consultar valor total
  7. 🚪 Salir del sistema
```

### Ejemplo: Añadir Producto

```
Selecciona una opción (1-7): 1

Ingresa ID único: P001
Nombre del producto: Aguaje
Categoría: Frutas Amazónicas
Cantidad: 50
Precio: 12.50

✅ Producto 'Aguaje' añadido y guardado en archivo.
```

---

## 🔍 Métodos Principales

**`_buscar_indice_por_id(id)`** - Búsqueda lineal O(n)
```python
for indice, producto in enumerate(self._productos):
    if producto.get_id() == id:
        return indice
return -1
```

**`eliminar_producto(id)`** - Elimina de lista y persiste
```python
indice = self._buscar_indice_por_id(id)
if indice != -1:
    self._productos.pop(indice)
    self._guardar_inventario()
```

**`buscar_productos(nombre_parcial)`** - Búsqueda por contenido
```python
resultados = [p for p in self._productos 
              if nombre_parcial.lower() in p.get_nombre().lower()]
```

**`calcular_valor_total()`** - Suma con generador
```python
total = sum(p.get_cantidad() * p.get_precio() for p in self._productos)
```

---

## ✅ Validaciones

| Campo | Validación |
|-------|-----------|
| **ID** | Único (no duplicados) |
| **Nombre** | No vacío |
| **Cantidad** | Entero ≥ 0 |
| **Precio** | Número ≥ 0 |
| **Categoría** | No vacía |

---

## 🎓 Conceptos POO Implementados

- **Encapsulación:** Atributos privados (`_nombre`) con getters/setters
- **Constructor:** `__init__()` inicializa objetos Producto
- **Destructor:** `__del__()` limpia recursos
- **Abstracción:** Interfaz simple en el menú
- **Método especial:** `__str__()` para representación legible

---

## 📚 Documentación Completa

- [DOCUMENTACION.md](DOCUMENTACION.md) - Conceptos y flujos detallados
- [GUIA_TECNICA.md](GUIA_TECNICA.md) - Referencia de métodos con complejidad
- [DIAGRAMA_DATOS.md](DIAGRAMA_DATOS.md) - Transformaciones y CSV mapping
- [INDICE_DOCUMENTACION.md](INDICE_DOCUMENTACION.md) - Navegación de docs

---

## ❓ Preguntas Frecuentes

**¿Dónde se guardan los datos?**
En `servicios/data/inventario.txt` (CSV, se carga al inicio y se guarda con cada cambio)

**¿Se pierden al cerrar?**
No, se guardan automáticamente en cada operación

**¿Puedo editar el archivo manualmente?**
Sí, formato: `ID,Nombre,Categoría,Cantidad,Precio` (respeta el orden)

**¿Qué pasa si no existe el archivo?**
Se crea al primera ejecución si la carpeta `servicios/data/` existe

---

**¡Gracias por usar nuestro Sistema de Gestión de Inventarios! 🙏**
