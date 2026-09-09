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