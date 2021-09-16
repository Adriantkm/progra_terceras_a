import datetime

#Clase salida
class Salida:
    def __init__(self, id_empleado, nombre):
        self.nombre= nombre
        self.id_empleado= id_empleado

    #Defino la salida con los mismos datos que la entrada (id_empleado y nombre).
    def salida(id_empleado, nombre):
        registros= open("Registros.txt", "a+", encoding="utf8")
        id_empleado= input(str("Porfavor, introduzca el id del empleado: "))
        nombre=input(str("Porfavor, introdusca su nombre: "))
        #La fecha y hora se introduce automaticamente.
        date= datetime.datetime.now()
        fecha= date.strftime('%d/%m/%Y | Hora de salida: %H:%M:%S')
        print("!Gracias, se guardaran los datos registrados!")
        #Guardo los datos en el blog de notas.
        registros.write(f'Fecha: {fecha} | ID: {id_empleado} | Nombre: {nombre} | \n')
        registros.close
