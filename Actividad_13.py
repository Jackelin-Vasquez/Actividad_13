#SISTEMA DE GESTIÓN ACADÉMICA
def menu_principal():
    print("---MENÚ DE GESTIÓN ACADÉMICA---")
    print("1.Agregar Estudiate.\n2.Agregar curso con nota.\n3.Consultar Estudiante")
    print("4.Calcular promedio de estudiante\n5.Verificar si aprueba\n6.Mostrar todos los estudiantes.\n7.Salir")

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
        break