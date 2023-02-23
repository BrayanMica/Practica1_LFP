# peliculas = []

# def agregar_pelicula(nombre, actores, año, género):
#     for i, pelicula in enumerate(peliculas):
#         if pelicula[0] == nombre:
#             peliculas.pop(i)
#             break
#     peliculas.append([nombre, actores, año, género])


# # Ejemplo de uso
# agregar_pelicula('El padrino', ['Marlon Brando', 'Al Pacino'], 1972, 'Drama')
# agregar_pelicula('La lista de Schindler', ['Liam Neeson', 'Ben Kingsley'], 1993, 'Drama')
# agregar_pelicula('El padrino', ['Marlon Brando', 'Al Pacino', 'Robert Duvall'], 1972, 'Drama')
# print(peliculas)

# # Barra de progreso
# from tqdm import tqdm
# import time

# for i in tqdm(range(3)):
#     time.sleep(1)
    
    
class Pelicula:
    def __init__(self, nombre, autores, anio, genero):
        self.nombre = nombre
        self.autores = autores
        self.anio = anio
        self.genero = genero

def eliminar_duplicados(lista_peliculas):
    peliculas_sin_duplicados = []
    for pelicula in lista_peliculas:
        duplicado = False
        for i, p in enumerate(peliculas_sin_duplicados):
            if pelicula.nombre == p.nombre:
                peliculas_sin_duplicados[i] = pelicula
                duplicado = True
                break
        if not duplicado:
            peliculas_sin_duplicados.append(pelicula)
    return peliculas_sin_duplicados

lista_peliculas = [Pelicula("Titanic", ["James Cameron"], 1997, "Romance"),
                   Pelicula("El Padrino", ["Francis Ford Coppola"], 1972, "Drama"),
                   Pelicula("Star Wars", ["George Lucas"], 1977, "Ciencia ficción"),
                   Pelicula("Titanic", ["Steven Spielberg","Leonardo Dicaprio"], 2016, "Acción")]

peliculas_sin_duplicados = eliminar_duplicados(lista_peliculas)

for pelicula in peliculas_sin_duplicados:
    print(pelicula.nombre, pelicula.autores, pelicula.anio, pelicula.genero)
