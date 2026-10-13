class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponibilidad = True

    def __repr__(self):
        return f"{self.titulo}, {self.autor}, Disponibilidad: {self.disponibilidad}"

class Biblioteca:
    def __init__(self):
        self.lista_libros = []

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)
        print(f"{libro} se agregó correctamente a la lista")

    def prestar(self, titulo):
        encontrado = False 
        for prestar_libro in self.lista_libros:
            if prestar_libro.titulo == titulo:
                encontrado = True
                if prestar_libro.disponibilidad:
                    print(f"{titulo} prestado correctamente")
                    prestar_libro.disponibilidad = False
                else:
                    print(f"{titulo} no se encuentra disponible")
        if encontrado == False:   
            print(f"{titulo} No existe ese ese titulo")  

    def devolver(self, titulo):
        encontrado = False 
        for prestar_libro in self.lista_libros:
            if prestar_libro.titulo == titulo:
                encontrado = True
                if prestar_libro.disponibilidad == False:
                    print(f"{titulo} devuelto")
                    prestar_libro.disponibilidad = True
                else:
                    print(f"{titulo} no se encuentra disponible")
        if encontrado == False:   
            print(f"{titulo} No existe ese ese titulo")      

    def mostrar_disponibles(self):
        for prestar_libro in self.lista_libros:
            if prestar_libro.disponibilidad:
                print(f"{prestar_libro} disponibles para prestar")
            else:
                print(f"{prestar_libro} no se encuentra disponible")


lib = Libro("Odisea", "Nueva Cheems")
lib2 = Libro("Coco", "Drilo")
lib3 = Libro("El que no", "Messi")
bib = Biblioteca()
bib.agregar_libro(lib)
bib.agregar_libro(lib2)
bib.agregar_libro(lib3)
bib.prestar("Coco")
bib.prestar("Coco")
bib.devolver("Coco")
bib.mostrar_disponibles()






