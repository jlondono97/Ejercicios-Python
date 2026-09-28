inventario = {
    "camiseta": {"precio": 35000, "stock": 20, "talla": "M"},
    "pantalon": {"precio": 80000, "stock": 5, "talla": "32"},
    "chaqueta": {"precio": 150000, "stock": 0, "talla": "L"},
    "gorra": {"precio": 25000, "stock": 15, "talla": "Unica"}
}

def mostrar_productos(mi_diccionario):
    for x, obj in mi_diccionario.items():
        print(x)
    
        for y in obj:
            print(f"{y} : {obj[y]}")
    return True

a = mostrar_productos(inventario)
print(a)

def mostrar_stock(mi_diccionaro):
    for x, obj in mi_diccionaro.items():
        for y in obj:
            if obj[y] == 0:
                print(f"Producto agotado: {x}")
                print(f"{y} {obj[y]}")
    return True

b = mostrar_stock(inventario)
print(b)

def valor_inventario(mi_diccionario):
    for x, obj in mi_diccionario.items():
        print(x)
        for y in obj:
            valor = obj['precio'] * obj['stock']
        print(valor)
    return True

c = valor_inventario(inventario)
print(c)


def aumento_inventario(mi_diccionario):
    for x, obj in mi_diccionario.items():
        for y in obj:
            if obj['stock'] <= 10:
                total_descuento = obj['precio'] * 0.10 + obj['precio']
                print(f"Productos con menos de 10 unidades: {x} y su precio aumentado es {total_descuento}")
    return True

d = aumento_inventario(inventario)
print(d)


