class Pelicula:
    def __init__(self, nombre, autores, anio, genero):
        self.nombre = nombre
        self.autores = autores
        self.anio = anio
        self.genero = genero

    def mostarinfo(self):
        print("\nNOMBRE PELICULA: ",self.nombre, "\nAUTORES: ", self.autores,"\nAÑO ESTRENO: ", self.anio,"\nGENERO: ", self.genero)

def leerArchivoEntrada(lista):
    ruta = input("Escriba la ruta del archivo a leer: ")
    archivo = open(ruta, 'r')
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

        peli = Pelicula(tmp_nombre, tmp_autores, tmp_anio, tmp_genero)
        lista.append(peli)