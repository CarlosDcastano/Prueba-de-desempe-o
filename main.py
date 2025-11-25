
from productos import *
from inventario_ventas import inventario_prod
from ventas import *
from reportes import *

def menu_principal():
    print("*" * 50)
    print(" " * 7, "OPTIONS MENU")
    print(" " * 12, "1. Register book")
    print(" " * 12, "2. Consultar inventario de libros")
    print(" " * 12, "3. Check book inventory")
    print(" " * 12, "4. Update a book")
    print(" " * 12, "5. Delete a book")
    print(" " * 12, "6. Register sale")
    print(" " * 12, "7. Consult sales")
    print(" " * 12, "8. Sales report")
    print(" " * 12, "9. Exit")
    print("*" * 50)

def main():
    while True:
        menu_principal()
        opcion = input("Enter one of the menu options: ")
        if opcion == "1":
            titulo = input("Enter the book title: ").upper()
            autor = input("Enter the book author: ").upper()
            categoria = input("Enter the book category: ").upper()
            while True:
                try:
                    precio = float(input("Enter the book price: "))
                    cantidadStock = int(input("Enter the number of books to be entered: "))
                    if precio < 0 or cantidadStock < 0:
                        print("The value cannot be negative.")
                        continue
                    
                except ValueError:
                    print("Invalid value. Confirm that price is a floating-point value and quantity is an integer.")
                else:
                    registrar_producto(inventario_prod, titulo, autor, categoria, precio, cantidadStock)
                    break
        
        elif opcion == "2":
            consultar_productos(inventario_prod)
        
        
        elif opcion == "3":
            titulo = input("Enter the name of the book you wish to consult: ")
            resultado = consultar_producto_por_titulo(inventario_prod, titulo)
            print(resultado)
        

        elif opcion == "4":
            titulo = input("Enter the name of the book to update: ").upper()
            newtitle = input("Enter the new book title: ").upper()
            newAutor = input("Enter the new book author: ").upper()
            newCategoria= input("Enter the new book category: ").upper()
            while True:
                try:
                    newPrecio= int(input("Enter the new book price: "))
                    newCantidadStock = int(input("Enter the new book quantity: "))
                    if newPrecio < 0 or newCantidadStock < 0:
                        print("The value cannot be negative")
                        continue
                    
                except ValueError:
                    print("VInvalid value. Confirm that the new price is a floating-point value and the quantity is an integer.")

                else: 
                    actualizado = actualizar_productos(inventario_prod, titulo, newtitle, newAutor, newCategoria, newPrecio, newCantidadStock)
                    print(actualizado)
                    break

        elif opcion == "5":
            titulo = input("Enter the name of the book to delete: ").upper()
            eliminado = eliminar_productos(inventario_prod, titulo)
            print(eliminado)

        elif opcion == "6":
            cliente = input("Enter the customer's name: ").upper()
            producto = input("Enter the name of the book you wish to purchase: ").upper()
            while True:
                try:
                    cantidad = int(input("Enter the number of books to buy"))
                    if cantidad < 0:
                        print("The amount cannot be negative.")
                        continue
                except ValueError:
                    print("The amount must be an integer number.")
                else:
                    venta_agregada = registrar_venta(inventario_prod,ventas, cliente, producto, cantidad, fecha= datetime.date.today(), descuento=0.90)
                    print(venta_agregada)
                    break
        elif opcion == "7":
            mostrar= mostrar_ventas(ventas)
            print(mostrar)

        elif opcion == "8":
            print(top_3)
            ventas_por_autor(ventas, inventario_prod)

        elif opcion == "9":
            print("Bye")
            break



main()