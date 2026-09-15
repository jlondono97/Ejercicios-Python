receta_pasta = ["tomate", "ajo", "pasta", "aceite", "sal"]
receta_ensalada = ["lechuga", "tomate", "cebolla", "aceite", "limon"]
receta_sopa = ["papa", "zanahoria", "cebolla", "sal", "agua"]

def ingredientes_repetidos(set_1, set_2):
    set_pasta = set(set_1)
    set_ensalada = set(set_2)
    set_ingredientes_repetidos = set_pasta.intersection(set_ensalada)
    return set_ingredientes_repetidos

set_repetidos = ingredientes_repetidos(receta_pasta, receta_ensalada)
print(set_repetidos)

def ingredientes_compras(set_1, set_2, set_3):
    set_pasta = set(set_1)
    set_ensalada = set(set_2)
    set_sopa = set(set_3)
    set_ingredientes_distintos = set_pasta | set_ensalada | set_sopa
    return set_ingredientes_distintos

set_compras = ingredientes_compras(receta_pasta, receta_ensalada, receta_sopa)
print(set_compras)

def ingredientes_diferencia(set_1, set_2, set_3):
    set_pasta = set(set_1)
    set_ensalada = set(set_2)
    set_sopa = set(set_3)
    set_ingredientes_diferencia = set_sopa - set_ensalada - set_pasta
    return set_ingredientes_diferencia

set_diferentes = ingredientes_diferencia(receta_pasta, receta_ensalada, receta_sopa)
print(set_diferentes)

def aceite(set_1, set_2, set_3):
    set_pasta = set(set_1)
    set_ensalada = set(set_2)
    set_sopa = set(set_3)
    if "aceite" in set_pasta and "aceite" in set_ensalada and "aceite" in set_sopa:
        print("aceite está en los tres sets")
        return True
    else:
        print("aceite no está en los tres sets")
        return False

set_cebolla = aceite(receta_pasta, receta_ensalada, receta_sopa)
print(set_cebolla)


