empleados = [
    ("Ana", 2500000),
    ("Luis", 1800000),
    ("Carla", 3200000),
    ("Pedro", 1800000),
    ("Sofia", 4000000)
]

sorted_empleados = sorted(empleados, key=lambda x: x[1])
print(sorted_empleados)

filter_empleados = list(filter(lambda x: x[1] > 2000000, empleados))
print(filter_empleados)

map_empleados = list(map(lambda salario: f"{salario[0]} gana {salario[1]}" , empleados))
print(map_empleados)

es_alto = lambda salario: salario > 3000000

print(es_alto(250))
