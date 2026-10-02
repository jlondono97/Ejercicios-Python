def mi_decorador(funcion1):
    def envoltura():
        print("Antes de la jugada")
        funcion1()
        print("Después de la jugada")
    return envoltura

@mi_decorador
def patear():
    print("¡Gol!")

patear()

import time

def medir_tiempo(funcion2):
    def envoltura():
        x = time.time()
        print(x)
        funcion2()
        y = time.time()
        print(y)
    return envoltura

@medir_tiempo
def tarea_lenta():
    time.sleep(2)
    print("Tarea terminada")

tarea_lenta()

def mostrar_mensaje(funcion):
    def envoltura():
        print("🚀 Comenzando...")
        funcion()
        print("✅ Terminamos")
    return envoltura

@mostrar_mensaje
def estudiar():
    print("Estoy estudiando Python")

estudiar()

def registrar(funcion):
    def envoltura(*args):
        print("📌 Ejecutando función...")
        funcion(*args)
        print("📌 Función terminada")
    return envoltura

@registrar
def sumar(a, b):
    print(a + b)

sumar(5 , 3)
