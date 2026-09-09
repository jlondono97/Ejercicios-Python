def promediolista(lista_promedios):
    contador = 0
    resultado = 0
    for numeros in lista_promedios:
        resultado += numeros
        contador += 1
    promedio = resultado/contador
    return promedio

def promedio_lista(lista_pro):
    promedio = sum(lista_pro)/len(lista_pro)
    return promedio

lista = [1,2,3,4,5,7]

pro = promedio_lista(lista)
print(pro)
promedios = promediolista(lista)
print(promedios)

precios = [15000, 8500, 22000, 5000, 15000, 30000, 8500, 12000]

def mostrar_precios(lista_precios):
    maximo = max(lista_precios)
    minimo = min(lista_precios)
    return maximo, minimo

p = mostrar_precios(precios)
print(p)