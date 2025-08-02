#SISTEMA DE GESTIÓN ACADÉMICA
estudiante={}
def menu_principal():
    print("---MENÚ DE GESTIÓN ACADÉMICA---")
    print("1.Agregar Estudiate.\n2.Agregar curso con nota.\n3.Consultar Estudiante")
    print("4.Calcular promedio de estudiante\n5.Verificar si aprueba\n6.Mostrar todos los estudiantes.\n7.Salir")

def agregar_estudiantes():
    id= input("Ingrese ID del estudiante:")
    nombre=input("Ingrese nombre del estudiante:")
    carrera= input("Ingrese carrera o programa academico:")

    estudiante[id]={
        "id":id,
        "nombre":nombre,
        "carrera":carrera,
        "cursos":{}
    }

    return id,nombre,carrera

def agregar_curso():
    id= input("Ingrese id de estudiante:")
    if id in estudiante:
        nombre_curso=input("Ingrese nombre de curso:")
        try:
            nota= float(input("Ingrese nota final:"))
        except ValueError:
            print("Error: Ingrese numeros validos.")
        else:
            if nota <0 or nota >100:
                print("Nota no valida...")
            else:
                estudiante[id]["cursos"][nombre_curso] = nota
                return nota,nombre_curso
    else:
        print("Estudiante no encontrado...")

menu_principal()
opcion= input("Ingrese una opcion:")

match opcion:
    case "1":
        print("---AGREGAR ESTUDIANTE---")
    case "2":
        print("---AGREGAR CURSO CON NOTA---")
    case "3":
        print("---CONSULTAR ESTUDIANTE---")
    case "4":
        print("---CALCULAR PROMEDIO DE ESTUDIANTE---")
    case "5":
        print("---VERIFICAR SI APRUEBA ESTUDIANTE---")
    case "6":
        print("---MOSTAR TODOS LOS ESTUDIANTES---")
    case "7":
        print("saliendo del sistema...")
