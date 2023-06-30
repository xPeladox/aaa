from random import randint
alumno = []
asignatura = []
matricula = randint(1000,5000)
def grabar():
    try:
        while True:
                print("****************************")
                rut = input("Ingrese rut en formato 12345678-k: ")
                if len(rut) == 10 and rut[:7].isdigit() and rut[8] == "-" and rut[9:].isalnum:
                    print("**RUT ingresado correctamente**")
                    break
                else:
                    print("### RUT ingresado incorrectamente ###")
        while True:
                nombre = input("ingrese nombre: ")
                if len(nombre) > 2 and len(nombre)<12:
                    print("**Nombre ingresado correctamente**")
                    break
                else:
                    print("### Su nombre debe contener de 2 a 12 caracteres ###")
        apellido = input("Ingrese su apellido: ")
        fechanac = input("Ingrese fecha de nacimiento: ")
        carrera = input ("Ingrese su carrera: ")
        numerolista = int(input("Ingrese su numero de lista: "))
        alumno.append([rut,nombre,apellido,fechanac,carrera,numerolista])
        asignaturaprom(rut)
    except ValueError:
        print("## INGRESE CARACTER CORRESPONDIENTE ##")
    
def asignaturaprom(rut):
    try:
        asig = input("INGRESE ASIGNATURA: ")
        while True:
            prom = float(input("INGRESE SU PROMEDIO: "))
            if prom >=1 and prom <=7:
                break
            else:
                print("## PROMEDIO DEBE SER ENTRE 1.0 hasta 7.0 ##")
        for i in range(len(alumno)):
            if alumno[i][0] == rut:
                asignatura.insert(i,[asig,prom])
                break
            elif alumno[i][0] != rut:
                print("### RUT NO ENCONTRADO ###")  
    except ValueError:
        print("## INGRESE SOLO NUMEROS ##")
def buscar():
    if not alumno:
        print("### NINGÚN RUT REGISTRADO###")
        return
    for i in range(len(alumno)):
        if alumno[i][0] == rut:
            print("****************************")
            print(f"Rut: {alumno[i][0]}")
            print(f"Nombre: {alumno[i][1]}")
            print(f"Apellido: {alumno[i][2]}")
            print(f"Fecha nacimiento: {alumno[i][3]}")
            print(f"Carrera: {alumno[i][4]}")
            print(f"Numero lista: {alumno[i][5]}")
            print(f"Asignatura: {asignatura[i][0]}")
            print(f"Promedio: {asignatura[i][1]}")
            print("****************************")
            break
        elif alumno[i][0] != rut:
            print("### RUT NO ENCONTRADO ###")    

def certificados():
    if not alumno:
        print("### NINGÚN RUT REGISTRADO ###")
        return
    try:
        print("1) Certificado alumno regular\n2) Certificado de notas\n3) Certificado de matricula")
        opc2= int(input("ELIJA UNA OPCION: "))
        if opc2 == 1:
            print("CERTIFICADO ALUMNO REGULAR")
            for i in range(len(alumno)):
                if alumno[i][0] == rut:
                    print("****************************")
                    print(f"Rut: {alumno[i][0]}")
                    print(f"Nombre: {alumno[i][1]}")
                    print(f"Carrera: {alumno[i][4]}")
                    print("Usted es Alumno de Duoc")
                    break
                elif alumno[i][0] != rut:
                    print("### RUT NO ENCONTRADO ###") 
        elif opc2 == 2:
            print("CERTIFICADO DE NOTAS")
            for i in range(len(alumno)):
                if alumno[i][0] == rut:
                    print("****************************")
                    print(f"Rut: {alumno[i][0]}")
                    print(f"Nombre: {alumno[i][1]}")
                    print(f"Carrera: {alumno[i][4]}")
                    for i in range(len(alumno)):
                        if alumno[i][0] == rut:
                            print(f"Asignatura: {asignatura[i][0]}")
                            print(f"Promedio: {asignatura[i][1]}")
                            break  
                        elif alumno[i][0] != rut:
                                print("### RUT NO ENCONTRADA ###") 
        elif opc2 == 3:
            print("**CERTIFICADO DE MATRICULA**")
            for i in range(len(alumno)):
                if alumno[i][0] == rut:
                    print("****************************")
                    print(f"Rut: {alumno[i][0]}")
                    print(f"Nombre: {alumno[i][1]}")
                    print(f"Carrera: {alumno[i][4]}")
                    print(f"Matricula ${matricula}") 
                    break 
                elif alumno[i][0] != rut:
                    print("### RUT NO ENCONTRADA ###")   
        else:
            print("## INGRESE UNA OPCION VALIDA ##")
    except ValueError:
        print("## INGRESE SOLO NUMEROS ##")

while True:
    try:
        print("****BIENVENIDO A DUOC****\n1) Registrar alumno\n2) Buscar alumno por RUT\n3) Buscar certificado\n4) Salir")
        opc = int(input("INGRESE UNA OPCION: "))
        if opc == 1:
                grabar()
        elif opc == 2:
                rut = input("INGRESE RUT A BUSCAR: ")
                buscar()
        elif opc == 3:
                rut = input("INGRESE RUT PARA BUSCAR CERTIFICADO: ")
                certificados()
        elif opc == 4:
            print("***HASTA LUEGO***")
            break
        else:
            print("## INGRESE UNA OPCION VALIDA ##")
    except ValueError:
        print("## INGRESE SOLO NUMEROS ##")