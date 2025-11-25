from ventas import *
from productos import *
from inventario_ventas import *


total_ventas = sum(v["totalNeto"] for v in ventas)
productos_ordenados = sorted(ventas, key=lambda v: v["totalNeto"], reverse=True)
print(total_ventas)
top_3 = productos_ordenados[:3]
print(top_3)

def ventas_por_autor(ventas, inventario_prod):
    [print(v) for v in ventas if v["producto"] == inventario_prod[["titulo"]]]



