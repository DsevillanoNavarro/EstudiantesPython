def agregaEstudiante():
    nombre = input("Dime el nombre del estudiante: ")
    edad = int(input("Dime la edad del estudiante: "))

    with open("registro_estudiantes.txt", "a") as file:
        file.write(f"{nombre},{edad}\n") 


    print(f"Estudiante {nombre} de {edad} años agregado al registro.")
def verEstudiantes():
    
        with open("registro_estudiantes.txt", "r") as file:
            estudiantes = file.readlines()  
            
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                print("Lista de estudiantes:")
                for estudiante in estudiantes:
                    print(estudiante.strip())  
    
def buscarEstudiante():
    nombre_buscar = input("Dime el nombre del estudiante que deseas buscar: ")

    
    with open("registro_estudiantes.txt", "r") as file:
            estudiantes = file.readlines()  
            encontrado = False
            
            for estudiante in estudiantes:
                nombre, edad = estudiante.strip().split(",")  
                if nombre.lower() == nombre_buscar.lower():  
                    print(f"Estudiante encontrado: Nombre: {nombre}, Edad: {edad}")
                    encontrado = True
                    break
            
            if not encontrado:
                print("Estudiante no encontrado.")

    
def borrarEstudiante():
    nombre_borrar = input("Dime el nombre del estudiante que deseas borrar: ")

    with open("registro_estudiantes.txt", "r") as file:
            estudiantes = file.readlines()  

    with open("registro_estudiantes.txt", "w") as file:
            encontrado = False
            
            for estudiante in estudiantes:
                nombre, edad = estudiante.strip().split(",")  
                if nombre.lower() == nombre_borrar.lower():  
                    print(f"Estudiante borrado: Nombre: {nombre}, Edad: {edad}")
                    encontrado = True
                else:
                    file.write(estudiante)  
            
            if not encontrado:
                print("Estudiante no encontrado.")

    

    
def compruebaNum(variableNum):
    if variableNum == 1:
        agregaEstudiante()
        
    elif variableNum == 2:
        verEstudiantes()
        
    elif variableNum == 3:
        buscarEstudiante()
        
    elif variableNum == 4:
        borrarEstudiante()
        
    elif variableNum == 5:
        print("Salir del programa")
        exit()
        
    else:
        print("Número no válido. Por favor, intenta de nuevo.")

def menu():
    print("PULSE UN BOTÓN")
    print("1. Agregar Estudiante")
    print("2. Ver lista de estudiantes")
    print("3. Buscar Estudiante")
    print("4. Eliminar Estudiante")
    print("5. Salir del programa")
    numero = int(input("Dime un número: "))
    compruebaNum(numero)
    while numero > 0 and numero < 5:
        menu()
    else:
    
        exit()
    

menu()

