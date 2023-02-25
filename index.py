import subprocess
import sys
from tqdm import tqdm
import time
from colorama import Fore, Back, Style

from carga import leerArchivoEntrada,eliminar_duplicados
ListaPeliculas = []    


def menu():
    condicion = True
    gestion = True
    subprocess.call('clear', shell=True)
    print(Fore.BLUE+"Lenguajes Formales y de Programación\n"
          +"Seccion B-\n"
          +"Carne: 201907343\n"
          +"Brayan Estiben Micá Pérez\n")
    input("Presione la tecla enter para continuar")
    
    while condicion:
        subprocess.call('clear', shell=True)
        gestion = True
        filtrado = True
        print(Fore.GREEN+"________________Menu______________\n"+
              "1. Cargar archivo de entrada\n"+
              "2. Gestionar películas\n"+
              "3. Filtrado\n"+
              "4. Gráfica\n"+
              "5. Salir")
        respuesta = input(Fore.YELLOW+"Escribe un numero de la lista del menu para continuar ")
        subprocess.call('clear', shell=True)
        if respuesta == "1":
            subprocess.call('clear', shell=True)
            for i in tqdm(range(1)):
                time.sleep(1)
            # CARGA DE ARCHIVOS
            leerArchivoEntrada(ListaPeliculas)
            
            if ListaPeliculas is not None:
                print("_________HA TERMINADO LA CARGA DEL ARCHIVO_________")
                #for i in ListaPeliculas:
                #    i.mostarinfo()
                #input()
            else:
                print("---------- ERROR NO SE CARGO EL ARCHIVO CORRECTAMENTE ----------")
            input("Presione la tecla enter para continuar")
            pass
        elif respuesta == "2":
            subprocess.call('clear', shell=True)
            if len(ListaPeliculas) > 0 :
                while gestion:
                    subprocess.call('clear', shell=True)
                    activador = False
                    print(Fore.MAGENTA+"------- Gestionar peliculas -------\n"
                    +"1. Mostrar peliculas\n"
                    +"2. Mostrar Actores\n"
                    +"3. Salir")
                    mpelis = input(Fore.YELLOW+"Ingrese un numero del menu para continuar ")
                    
                    if mpelis == '1':
                        subprocess.call('clear', shell=True)
                        print("_________DATOS CARGADOS EN MEMORIA_________")
                        nueva = eliminar_duplicados(ListaPeliculas)
                        for i in nueva:
                            print(i.nombre)
                        input("Presiona la tecla enter para continuar")
                        
                    elif mpelis == '2':
                        subprocess.call('clear', shell=True)
                        print("_________Peliculas disponibles_________")
                        nueva = eliminar_duplicados(ListaPeliculas)
                        for i,peli in enumerate(nueva):
                            print(str(i+1)+" "+ peli.nombre)
                        
                        Sactores = input(Fore.CYAN+"\nEscribe el numero de pelicula segun el listado\n"
                            +"para mostrar sus actores ")
                        for i,peli in enumerate(nueva):
                            if i == (int(Sactores)-1):
                                print(Fore.GREEN+"\n"+str(peli.nombre))
                                print(Fore.BLUE + str(peli.autores))
                                activador = False
                                break
                            else:
                                activador = True
                        if activador == True:
                            print("El numero que ingresaste no es parte del listado")
                            activador = False
                        input("Presione la tecla enter para continuar")

                    elif mpelis == '3':
                        subprocess.call('clear', shell=True)
                        gestion = False
                    else:
                        subprocess.call('clear', shell=True)
                        print("Ingresa un numero de la lista valido")
                        pass
            else:
                            print("---------- NO TIENES PELICULAS CARGADAS EN MEMORIA ----------")
                            input("Presiona la tecla enter para continuar")
        elif respuesta == "3":
            while filtrado:
                subprocess.call('clear', shell=True)
                if len(ListaPeliculas) > 0 :
                    nueva = eliminar_duplicados(ListaPeliculas)
                    print(Fore.LIGHTBLUE_EX+"-------------- Filatrado de peliculas ---------------\n"
                        +"1. Filtrado por nombre\n"
                        +"2. Filtrado por Año\n"
                        +"3. Filtrado por genero\n"
                        +"4. Salir")
                    Fentrada = input("Escribe un numero de la lista continuar")
                    if Fentrada == "1":
                        subprocess.call('clear', shell=True)
                        print("Filtrado por nombre\n")
                        Fnombre = input("Escriba el nombre de un actor\npara ver en que peliculas a colaborado ")
                        contador = 0
                        for i,peli in enumerate(nueva):
                            for j in peli.autores:  
                                if Fnombre == j:
                                    contador=contador+1
                                    print(Fore.YELLOW+str(contador) + ". " + str(peli.nombre))    
                        input(Fore.RED+"Pressiona la tecla enter para continuar")
                    elif Fentrada == "2":
                        subprocess.call('clear', shell=True)
                        print("Filtrado por Año\n")
                        Fanio = input("Escriba el año de las peliculas\nque desea ver ")
                        contador = 0
                        for i,pelicula in enumerate(nueva):
                            if Fanio == pelicula.anio:
                                contador = contador + 1
                                print(Fore.CYAN + str(contador) + ". " + pelicula.nombre)
                        if contador == 0:
                            print(Fore.RED+ "No existe ninguna pelicula con esa coincidencia de añio") 
                        input(Fore.YELLOW+"\nPresione la tecla enter para continuar")
                    elif Fentrada == "3":
                        subprocess.call('clear', shell=True)
                        print("Filtrado por genero\n")
                        Fgenero = input("Escriba el genero de las peliculas\nque desea ver ")
                        contador = 0
                        for i,pelicula in enumerate(nueva):
                            if Fgenero == str(pelicula.genero):
                                contador = contador + 1
                                print(Fore.CYAN + str(contador) + ". " + pelicula.nombre)
                                pass
                        if contador == 0:
                            print(Fore.RED+ "No existe ninguna pelicula con el genero que estas buscando") 
                        input(Fore.RED+"\nPresione la tecla enter para continuar")
                    elif Fentrada == "4":
                        filtrado = False
                        pass
                    else:
                        subprocess.call('clear', shell=True)
                        print("Ingresa un numero de la lista valido")
                        pass

                else:
                    print("---------- NO TIENES PELICULAS CARGADAS EN MEMORIA ----------")
                    filtrado = False
                    input("Presiona la tecla enter para continuar")
                pass
        elif respuesta == "4":
            subprocess.call('clear', shell=True)
            if len(ListaPeliculas) > 0 :
                print("---------- Mostrar imagen -----------")
                input("Presiona la tecla enter para continuar")
            else:
                print("---------- NO TIENES PELICULAS CARGADAS EN MEMORIA ----------")
                filtrado = False
                input("Presiona la tecla enter para continuar")
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