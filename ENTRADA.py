import datetime

#Clase entrada
class Entrada:
    def __init__(self, id_empleado, nombre):
        self.nombre= nombre
        self.id_empleado= id_empleado

    #Defino la entrada con id_empleado y nombre.
    def entrada(id_empleado, nombre):
        #Abro el blog de notas que seria mi base de datos.
        registros= open("Registros.txt", "a+", encoding="utf8")
        id_empleado= input(str("Porfavor, introduzca el id del empleado: "))
        nombre=input(str("Porfavor, introdusca su nombre: "))
        #La fecha y hora se introduce automaticamente.
        date= datetime.datetime.now()
        fecha= date.strftime('%d/%m/%Y | Hora de entrada: %H:%M:%S')
        print("!Gracias, se guardaran los datos registrados!")
        #Guardo los datos en el blog de notas.
        registros.write(f'Fecha: {fecha} | ID: {id_empleado} | Nombre: {nombre} | \n')
        registros.close