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
    nueva_lista = [precio for precio in lista_precios if precio > 10000]
    precios_oredenados = sorted(lista_precios)
    maximo = max(lista_precios)
    minimo = min(lista_precios)
    promedio = sum(lista_precios)/len(lista_precios)
    lista_sin_duplicados = list(set(lista_precios))
    return f"Maximo: {maximo}, Minimo: {minimo}, Promedio: {promedio}, Lista nueva: {nueva_lista}, Precios 8500: {lista_precios.count(8500)}, Precios ordenados: {precios_oredenados}, Lista sin duplicados: {lista_sin_duplicados}" 

p = mostrar_precios(precios)
print(p)

temperaturas = [18, 22, 19, 25, 30, 28, 21]

def temperatura(lista_temperatura):
    contador = 0
    lista_f = [temp * 9/5 + 32 for temp in lista_temperatura]
    for dias in lista_temperatura:
        if dias > 20:
            contador += 1
    tem_maxima = max(lista_temperatura)
    return f"Dias mayores a 20: {contador}, lista Fahrenheit: {lista_f}, Indice temperatura maxima: {lista_temperatura.index(tem_maxima)}"

t = temperatura(temperaturas)
print(t)
