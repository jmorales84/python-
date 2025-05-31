from datetime import datetime
fecha=datetime.now()
import datetime
año=datetime.datetime.strftime(fecha, "%Y")
print("SELECCIONE EL PERIODO DEL ESTUDIANTE")
print ("1   El estudiante entra durante el primer periodo")
print ("2   El estudiante entra durante el segundo perioso")
simbolo=input("Ingresa la operacion insertando el numero: ")
match simbolo:
    case "1":
        pe=1
    case "2":
        pe=2
    case _:
        
        print("El simbolo ingresado no es el correcto,veulva a intentarlo")
        exit()

print("Elija la carrera a la que pertenezca el estudiante ")
print ("1.- Ing. Industrial")
print ("2.- Ing. TICS")
print ("3.- Ing. Sistemas")
print ("4.- Ing. Quimica")
print ("5.- Ing. Civil")
print ("6.- Ing. Mecatronica")
print ("7.- Ing. Electrica")
print ("8.- Ing. Logistica")
print ("9.- Ing. Administracion")

carrera= input("Seleccione la carrera mediante el numero correspondiente: ")
match carrera:
    case"1":
        ca=1
    case"2":
        ca=2
    case"3":
        ca=3
    case"4":
        ca=4
    case"5":
        ca=5
    case"6":
        ca=6
    case"7":
        ca=7
    case"8":
        ca=8
    case"9":
        ca=9
    case _:
        print("ERROR NUMERO NO DISPONIBLE, vuelva a intentarlo")
        exit()


acum=int(input("Ingresa el numero de ingreso alumno: "))
if acum <= 0:
    print("ERROR NUMERO IMPOSIBLE, vuelva a intentarlo")
    exit()

elif acum <= 9:
    acum= "00"+ str(acum) 
    Con= str(año) + str(pe) + str(ca) + str(acum)
    print ("Tu numero de control es ", Con) 

elif acum<=99:
    acum="0" + str(acum)
    Con= str(año) + str(pe) + str(ca) + str(acum)
    print ("Tu numero de control es ", Con)
elif acum <=999:
    acum=acum
    Con= str(año) + str(pe) + str(ca) + str(acum)
    print ("Tu numero de control es ", Con)

elif acum >= 999:
    print("ERROR NUMERO MUY GRANDE, vuelva a intentarlo")
    exit()