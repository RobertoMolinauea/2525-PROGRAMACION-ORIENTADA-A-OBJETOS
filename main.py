from modelos.producto import Producto
from servicios.inventario import Inventario

def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Listar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_p, nombre, cantidad, precio)

            if inventario.agregar_producto(producto):
                print("Producto agregado correctamente.")
            else:
                print("Error: El ID ya existe.")

        elif opcion == "2":
            id_p = input("ID a eliminar: ")
            if inventario.eliminar_producto(id_p):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            id_p = input("ID a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))

            if inventario.actualizar_producto(id_p, cantidad, precio):
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Buscar por nombre: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            productos = inventario.listar_productos()
            if productos:
                for p in productos:
                    print(p)
            else:
                print("Inventario vacío.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
