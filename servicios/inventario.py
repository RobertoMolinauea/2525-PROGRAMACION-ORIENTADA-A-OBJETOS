from modelos.producto import Producto


class Inventario:
    """
    Inventario con archivo:
    - Carga desde inventario.txt al iniciar
    - Guarda en inventario.txt al agregar/actualizar/eliminar
    - Maneja: FileNotFoundError, PermissionError, ValueError
    """

    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # -----------------------------
    # ARCHIVOS: CARGAR
    # -----------------------------
    def cargar_desde_archivo(self):
        """
        Lee inventario.txt (formato: id,nombre,cantidad,precio)
        """
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                self.productos = []
                for num_linea, linea in enumerate(f, start=1):
                    linea = linea.strip()
                    if not linea:
                        continue

                    partes = linea.split(",")
                    if len(partes) != 4:
                        print(f"⚠ Línea corrupta (formato inválido) en {num_linea}: {linea}")
                        continue

                    try:
                        pid = int(partes[0])
                        nombre = partes[1]
                        cantidad = int(partes[2])
                        precio = float(partes[3])
                        self.productos.append(Producto(pid, nombre, cantidad, precio))
                    except ValueError:
                        print(f"⚠ Línea corrupta (datos inválidos) en {num_linea}: {linea}")
                        continue

        except FileNotFoundError:
            # si no existe, lo crea vacío
            try:
                with open(self.archivo, "w", encoding="utf-8") as _:
                    pass
                print("ℹ inventario.txt no existía. Se creó automáticamente.")
            except PermissionError:
                print("❌ No tienes permisos para crear inventario.txt.")

        except PermissionError:
            print("❌ No tienes permisos para leer inventario.txt.")

    # -----------------------------
    # ARCHIVOS: GUARDAR
    # -----------------------------
    def guardar_en_archivo(self):
        """
        Sobrescribe inventario.txt con el inventario actual.
        Retorna True si guardó, False si falló.
        """
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
            return True
        except PermissionError:
            print("❌ No tienes permisos para escribir en inventario.txt.")
            return False
        except OSError as e:
            print(f"❌ Error del sistema al guardar el archivo: {e}")
            return False

    # -----------------------------
    # OPERACIONES
    # -----------------------------
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Ya existe un producto con ese ID.")
                return False

        self.productos.append(producto)

        if self.guardar_en_archivo():
            print("✅ Producto agregado y guardado en inventario.txt")
        else:
            print("⚠ Producto agregado en memoria, pero NO se pudo guardar en el archivo")

        return True

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)

                if self.guardar_en_archivo():
                    print("✅ Producto eliminado y cambios guardados en inventario.txt")
                else:
                    print("⚠ Producto eliminado en memoria, pero NO se pudo guardar en el archivo")

                return True

        print("❌ No se encontró un producto con ese ID.")
        return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                if self.guardar_en_archivo():
                    print("✅ Producto actualizado y guardado en inventario.txt")
                else:
                    print("⚠ Producto actualizado en memoria, pero NO se pudo guardar en el archivo")

                return True

        print("❌ No se encontró un producto con ese ID.")
        return False

    def buscar_por_nombre(self, nombre):
        """
        Retorna lista de productos cuyo nombre contenga el texto (no distingue mayúsculas).
        """
        nombre = nombre.strip().lower()
        return [p for p in self.productos if nombre in p.get_nombre().lower()]

    def listar_productos(self):
        if not self.productos:
            print("📦 Inventario vacío.")
            return

        print("\n--- INVENTARIO ---")
        for p in self.productos:
            print(
                f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | "
                f"Cantidad: {p.get_cantidad()} | Precio: {p.get_precio()}"
            )
        print("------------------\n")