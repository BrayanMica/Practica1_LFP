import os
import subprocess
from pathlib import Path
class Pelicula:
    def __init__(self, nombre, autores, anio, genero):
        self.nombre = nombre
        self.autores = autores
        self.anio = anio
        self.genero = genero
        

    def mostarinfo(self):
        print("\nNOMBRE PELICULA: ",self.nombre, "\nAUTORES: ", self.autores,"\nAÑO ESTRENO: ", self.anio,"\nGENERO: ", self.genero)


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

    
def leerArchivoEntrada(lista):
    absolutepath = os.path.abspath(__file__)
    Directorio = os.path.dirname(absolutepath) 
    #ruta = input("Escriba el nombre del archivo: ")
    ruta_actual = Directorio + "/prueba.lfp"
    try:
        archivo = open(ruta_actual, 'r+', encoding='utf-8')
        lineas = archivo.readlines()
        for i in lineas:
            i = i.split(";")
            count = 1
            tmp_nombre = None
            tmp_autores = None
            tmp_anio = None
            tmp_genero = None
            for j in i:
                if count == 1:
                    tmp_nombre = j
                elif count == 2:
                    j = j.split(",")
                    tmp_autores = j
                elif count == 3:
                    tmp_anio = j
                elif count == 4:
                    tmp_genero = j
                count += 1

            #peli = Pelicula(tmp_nombre, tmp_autores, tmp_anio, tmp_genero)
            
            
            lista.append(Pelicula(tmp_nombre, tmp_autores, tmp_anio, tmp_genero))
            peliculas_sin_duplicados = eliminar_duplicados(lista)
            
            
    except IOError:
        subprocess.call('clear', shell=True)
        print("El archivo no se encuentra en la ruta "+ruta_actual )
    
    for pelicula in peliculas_sin_duplicados:
        print(pelicula.nombre, pelicula.autores, pelicula.anio, pelicula.genero)