from ventas import *
from productos import *
from inventario_ventas import *


def top_3_libros_mas_vendidos(ventas):
    """Return the top 3 books with the highest quantities sold."""
    ventas_por_libro = {}

    for v in ventas:
        producto = v["producto"]
        cantidad = v["cantidad"]

        ventas_por_libro[producto] = ventas_por_libro.get(producto, 0) + cantidad

    # Ordenar por cantidad (de mayor a menor)
    top_3 = sorted(ventas_por_libro.items(), key=lambda x: x[1], reverse=True)[:3]

    return top_3



def total_ventas_bruto_y_neto(ventas):
    """Return total gross sales and net sales."""
    total_bruto = sum(v["totalBruto"] for v in ventas)
    total_neto  = sum(v["totalNeto"] for v in ventas)

    return total_bruto, total_neto



def ventas_por_autor(ventas, inventario_prod):
    """Return a dictionary with total net sales per author."""
    ventas_autores = {}

    for v in ventas:
        titulo = v["producto"]

        # Buscar autor en el inventario
        for p in inventario_prod:
            if p["titulo"] == titulo:
                autor = p["autor"]
                break

        ventas_autores[autor] = ventas_autores.get(autor, 0) + v["totalNeto"]

    return ventas_autores




