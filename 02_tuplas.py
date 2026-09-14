ciudades = [
    ("Medellín", 6.25, -75.56),
    ("Bogotá", 4.71, -74.07),
    ("Cali", 3.45, -76.53),
    ("Cartagena", 10.39, -75.51)
]

def latitud_longitud(lista_ciudades):
    for ciudades in lista_ciudades:
        print(ciudades)

def nombre_ciudades(lista_ciudades):
    ciudades_lista = []
    for ciudades in lista_ciudades:
        ciudad, latitud, longitud = ciudades
        ciudades_lista.append(ciudad)
    print(ciudades_lista)

def latitud_maxima(lista_ciudades):
    dict_latitud = dict()
    for ciudades in lista_ciudades:
        ciudad, latitud, longitud = ciudades
        dict_latitud[latitud] = ciudad
        lat = max(dict_latitud.items())
    print(lat)

def nueva_tupla(lista_ciudades):
    nueva_ciudad = ("Nueva Cheems", 20.5, -58.36)
    lista_ciudades.append(nueva_ciudad)
    print(lista_ciudades)
        

latitud_longitud(ciudades)
nombre_ciudades(ciudades)
latitud_maxima(ciudades)
nueva_tupla(ciudades)


