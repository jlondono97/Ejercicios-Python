import json

usuario = {
    "nombre" : "Juan Esteban",
    "edad" : 29,
    "pais" : "Colombia", 
    "lenguaje" : "Python"
}

datos_json = json.dumps(usuario, indent = 4)
print(datos_json)

datos_dict = json.loads(datos_json)
print(datos_dict)

datos = '''
{
    "usuario": "Juan",
    "edad": 29,
    "skills": ["Python", "Git", "SQL"]
}
'''

dict_datos = json.loads(datos)

print(dict_datos['usuario'])
print(dict_datos['edad'])
print(dict_datos['skills'][0])

