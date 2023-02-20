import subprocess
import sys
from carga import leerArchivoEntrada
    
def menu():
    condicion = True
    ListaPelicualas = []
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
            # CARGA DE ARCHIVOS
            print("___________CARGA DE ARCHIVOS_________")
            leerArchivoEntrada(ListaPelicualas)
            print("CARGO EXITOSAMENTE\n")
            for i in ListaPelicualas:
                i.mostarinfo()
            input()
            pass
        elif respuesta == "2":
            from pathlib import Path
            ruta_actual = Path.cwd()
            print(ruta_actual)
            pass
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
  
    


    