#Defino la clase consulta.
class Consultas:
    
    #Defino "Consultar", con este puede consultar todos los datos.
    def consultar():
        registros= open("Registros.txt", "r", encoding="utf8")
        registros1= registros.read()
        print(registros1)

    #Defino "Consultar por id", con este puede consultar los datos del trabajador deseado.
    def consultarporid(id_empleado):
        registros= open("Registros.txt", "r+", encoding="utf8")
        id_empleado= str(input("Introduzca el id que desea consultar: "))
        for line in registros:
            lines= line.strip().split()
            if id_empleado in lines:
                print(lines)
        registros.close
    
    #Defino "Consultar por fecha", con este puede consultar los datos de una fecha especifica.
    def consultarporfecha(fecha):
        registros= open("Registros.txt", "r+", encoding="utf8")
        fecha= str(input("Porfavor, introduzca la fecha que desea consultar (dd/mm/aaaa): "))
        for line in registros:
            lines=line.strip().split()
            if fecha in lines:
                print(lines)
        registros.close