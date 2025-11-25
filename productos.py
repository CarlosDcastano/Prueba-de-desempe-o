


def registrar_producto(inventario_prod, titulo, autor, categoria, precio, cantidadStock):
    """
    Add a product (book) to the products inventory.

    Parameters:

    inventario_prod --> List of dictionaries representing existing products.
    titulo --> Represents the title of the product to be registered
    author, --> The author of the book
    categoria --> Represents the category of the book
    Precio --> The price of the book
    cantidaStock --> The amount of books to be registered.

    Returns: 
    
    message of successfully registered.
    """
    producto = {"titulo": titulo, 
                "autor": autor, 
                "categoria":categoria, 
                "precio": precio, 
                "cantidadStock": cantidadStock
    }
    inventario_prod.append(producto)

    return f"Product successfully registered"




def consultar_productos(inventario_prod):
    if not inventario_prod:
        return []
    
    for p in inventario_prod:
        print(f"TITLE:{p['titulo']} | AUTHOR:{p['autor']} | CATEGORY:{p['categoria']} | PRICE:{p['precio']} | QUANTITY IN STOCK:{p['cantidadStock']} | \n")




def consultar_producto_por_titulo(inventario_prod, titulo):
    if not inventario_prod:
        return []
    
    for p in inventario_prod:
        if titulo == p["titulo"]:
            return f"TITLE:{p['titulo']} | AUTHOR:{p['autor']} | CATEGORY:{p['categoria']} | PRICE:{p['precio']} | QUANTITY IN STOCK:{p['cantidadStock']} | \n"
        
    return f"Product {titulo} not found"
    
    


def actualizar_productos(inventario_prod, titulo, newtitle, newAutor, newCategoria, newPrecio, newCantidadStock):
    if not inventario_prod:
        return []
    
    for p in inventario_prod:
        if titulo == p["titulo"]:
            p["titulo"] = newtitle
            p["autor"] = newAutor
            p["categoria"] = newCategoria
            p["precio"] = newPrecio
            p["cantidadStock"] = newCantidadStock
            return f"Product in stock updated {p}"
    return "Product not found"




def eliminar_productos(inventario_prod, titulo):
    if not inventario_prod:
        return []
    
    for p in inventario_prod:
        if titulo == p["titulo"]:
            print(f"Product found {p}")
            inventario_prod.remove(p)
            return f"Product {p["titulo"]} has been deleted"

