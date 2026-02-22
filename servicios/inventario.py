from modelos.producto import Producto


class Inventario:

    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # ---------------------------
    # CARGAR DESDE ARCHIVO
    # ---------------------------
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    datos = linea.split(",")

                    if len(datos) == 4:
                        try:
                            producto = Producto(
                                int(datos[0]),
                                datos[1],
                                int(datos[2]),
                                float(datos[3])
                            )
                            self.productos.append(producto)
                        except ValueError:
                            print("Línea corrupta ignorada.")

        except FileNotFoundError:
            with open(self.archivo, "w", encoding="utf-8") as f:
                pass
            print("Archivo inventario.txt creado automáticamente.")

        except PermissionError:
            print("No tienes permisos para leer el archivo.")

    # ---------------------------
    # GUARDAR EN ARCHIVO
    # ---------------------------
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    f.write(linea)
        except PermissionError:
            print("No tienes permisos para escribir en el archivo.")

    # ---------------------------
    # AGREGAR
    # ---------------------------
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado correctamente.")

    # ---------------------------
    # ELIMINAR
    # ---------------------------
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

    # ---------------------------
    # ACTUALIZAR
    # ---------------------------
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    # ---------------------------
    # LISTAR
    # ---------------------------
    def listar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        print("\n--- INVENTARIO ---")
        for p in self.productos:
            print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: {p.get_precio()}")
        print("------------------")