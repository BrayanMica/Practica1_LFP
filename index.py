import subprocess
import sys
from tqdm import tqdm
import time

from carga import leerArchivoEntrada
ListaPelicualas = []    


def menu():
    condicion = True
    gestion = True
    print("Lenguajes Formales y de Programación")
    print("Seccion B-")
    print("Carne: 201907343")
    print("Brayan Estiben Micá Pérez")
    input()
    subprocess.call('clear', shell=True)
    while condicion:
        print("________________Menu______________\n"+
              "1. Cargar archivo de entrada\n"+
              "2. Gestionar películas\n"+
              "3. Filtrado\n"+
              "4. Gráfica\n"+
              "5. Salir")
        respuesta = input("Escribe un numero de la lista del menu para continuar ")
        if respuesta == "1":
            subprocess.call('clear', shell=True)
            for i in tqdm(range(3)):
                time.sleep(1)
            # CARGA DE ARCHIVOS
            leerArchivoEntrada(ListaPelicualas)
            if ListaPelicualas is not None:
                print("_________HA TERMINADO LA CARGA DEL ARCHIVO_________")
                #for i in ListaPelicualas:
                #    i.mostarinfo()
                #input()
            else:
                print("---------- ERROR NO SE CARGO EL ARCHIVO CORRECTAMENTE ----------")
            pass
        elif respuesta == "2":
            subprocess.call('clear', shell=True)
            print("------- Gestionar peliculas -------\n"
                  +"1. Mostrar peliculas\n"
                  +"2. Mostrar Actores\n")
            while gestion:
                mpelis = input("Ingrese un numero del menu para continuar")
                if mpelis == '1':
                    subprocess.call('clear', shell=True)
                    if len(ListaPelicualas) > 0 :
                        print("_________DATOS CARGADOS EN MEMORIA_________")
                        for i in ListaPelicualas:
                            i.mostarinfo()
                        input()
                    else:
                        print("---------- NO TIENES CARGADOS DATOS EN MEMORIA ----------")
                    gestion = False
                elif mpelis == '2':
                    subprocess.call('clear', shell=True)
                    print("Escribe un nombre de pelicula para mostrar los actores")
                    gestion = False
                else:
                    subprocess.call('clear', shell=True)
                    print("------- Gestionar peliculas -------\n"
                    +"1. Mostrar peliculas\n"
                    +"2. Mostrar Actores\n")
                    print("El numero que ingresaste no es parte del menu vuelve a intentarlo")
            
        elif respuesta == "3":
            pass
        elif respuesta == "4":
            pass
        elif respuesta == "5":
            subprocess.call('clear', shell=True)
            print("..........HAZ SALIDO DEL PROGRAMA.....")
            sys.exit()
        else:
            subprocess.call('clear', shell=True)
            print(".......INGRESA UN CARACTER VALIDO.........")
        
    
if __name__ == '__main__':
    menu()
  
    


    