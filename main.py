from modelos.producto import Producto
from servicios.inventario import Inventario


def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Listar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_p = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_p, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            except ValueError:
                print("Error: ID, cantidad y precio deben ser números.")

        elif opcion == "2":
            try:
                id_p = int(input("ID a eliminar: "))
                inventario.eliminar_producto(id_p)
            except ValueError:
                print("Error: El ID debe ser un número.")

        elif opcion == "3":
            try:
                id_p = int(input("ID a actualizar: "))
                cantidad_txt = input("Nueva cantidad (Enter para no cambiar): ")
                precio_txt = input("Nuevo precio (Enter para no cambiar): ")

                nueva_cantidad = int(cantidad_txt) if cantidad_txt else None
                nuevo_precio = float(precio_txt) if precio_txt else None

                inventario.actualizar_producto(id_p, nueva_cantidad, nuevo_precio)

            except ValueError:
                print("Error: valores inválidos.")

        elif opcion == "4":
            texto = input("Buscar nombre: ").lower()

            encontrados = []
            for p in inventario.productos:
                if texto in p.get_nombre().lower():
                    encontrados.append(p)

            if encontrados:
                for p in encontrados:
                    print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: {p.get_precio()}")
            else:
                print("No encontrado.")

        elif opcion == "5":
            inventario.listar_productos()

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
