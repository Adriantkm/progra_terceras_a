from ENTRADA import Entrada
from SALIDA import Salida
from CONSULTAS import Consultas

again= True
while again==True:
    print("Bienvenido")
    print("Este es el menu")
    print("1.- Entradas")
    print("2.- Salidas")
    print("3.- Consultar datos")
    print("4.- Salir")
    print("Porfavor seleccione una opcion")
    respuesta= int(input())
    if respuesta <=0:
        print("Porfavor, seleccione una opcion valida.")
    if respuesta >=4:
        print("Porfavor, seleccione una opcion valida.")
    if respuesta ==1: 
        again1=True
        while again1==True:
            print("1.- Registrar entrada.")
            print("2.- Volver.")
            respuesta1= int(input())
            if respuesta1 <=0:
                print("Porfavor, seleccione una opcion valida.")
            if respuesta1 >=5:
                print("Porfavor, seleccione una opcion valida.")
            if respuesta1 ==1:
                registro=Entrada.entrada("","")
            if respuesta1 ==2:
                again1=False

    if respuesta == 2:
        again2= True
        while again2==True:
            print("1.- Registrar salida.")
            print("2.- Volver.")
            respuesta2= int(input())
            if respuesta2 <=0:
                print("Porfavor, seleccione una opcion valida.")
            if respuesta2 >=3:
                print("Porfavor, seleccione una opcion valida.")
            if respuesta2 ==1:
                salida=Salida.salida("","")
            if respuesta2 ==2:
                again2=False

    if respuesta == 3:
        again3= True
        while again3==True:
            print("1.- Consultar todos los datos.")
            print("2.- Consultar por ID.")
            print("3.- Consultar por fecha.")
            print("4.- Volver.")
            respuesta3= int(input())
            if respuesta3 <=0:
                print("Porfavor, seleccione una opcion valida.")
            if respuesta3 >=5:
                print("Porfavor, seleccione una opcion valida.")
            if respuesta3 ==1:
                consultas=Consultas.consultar()
            if respuesta3 ==2:
                consultar=Consultas.consultarporid("")
            if respuesta3 ==3:
                consultaf=Consultas.consultarporfecha("")
            if respuesta3 ==4:
                again=False
    if respuesta ==4:
        print("Gracias por usar el programa!!")
        again= False

        
