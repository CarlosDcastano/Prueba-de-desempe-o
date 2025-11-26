from inventario_ventas import inventario_prod, ventas
import productos
import datetime



def registrar_venta(inventario_prod, ventas, cliente, producto, cantidad, fecha= datetime.date.today(), descuento=0.90):
    """
    Add a sale to the sales inventory, only if the product exist in the
    products inventory and subtract the quantity of products in stock of that book
    in the products inventory.

    Parameters:

    inventario_prod --> List of dictionaries representing existing products.
    ventas--> List of dictionaries representing each sale
    cliente, --> The customer that is purchasing the book
    producto --> The book that is being sold
    cantidad --> The amount of books to be sold
    fecha= datetime.date.today --> The date of the sale bein complete.

    Returns: 
    
    venta  --> it returns the specific dictionary representing the sale made.
    
    """
    topeDesc = 200000
    desc = 0
    for p in inventario_prod:
        if producto == p["titulo"]:
            if cantidad < p["cantidadStock"]:
                total = p["precio"] * cantidad
                if total > topeDesc:
                    desc = total - (total * descuento)
                    totalNeto = total * descuento
                    

                venta = {"cliente": cliente, 
                        "producto": producto, 
                        "cantidad":cantidad, 
                        "fecha": fecha,
                        "valorUnidad": p["precio"],
                        "totalBruto": total,
                        "descuento": desc,
                        "totalNeto": totalNeto
                }
                ventas.append(venta)
                
                p["cantidaStock"] -= cantidad
                print("Sale successfully completed")
                return venta
            else:
                return f"IT's not possible to sell {cantidad} books of {producto}. Total book: {p["titulo"]} in stock: {p["cantidadStock"]}"
    return f"Product '{producto}' not found"
        

def mostrar_ventas(ventas):
    """
    It shows the list of dictionaries in which the sale was registered

    Parameters: List of dictionaries representing each sale

    returns:

    ventas --< All the sales in the inventory.

    ventas --> 
    """
    if not ventas:
        return f"There is not any completed sale"
    
    for v in ventas:

        print(f"Customer:{v['cliente']} |Product:{v['producto']} |Amount:{v['cantidad']} |Date:{v['fecha']} |Unit Value:{v['valorUnidad']} |Gross total:{v['totalBruto']} |Discount:{v['descuento']} |Net Total:{v['totalNeto']}")
    return ventas


