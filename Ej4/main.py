# main.py
from objeto_medicion import ObjetoMedicion
from operaciones import persistir_objetos, visualizar_objetos, calcular_velocidad_promedio, buscar_mayor_altitud_archivo

def menu():
    objetos = []
    archivo_guardado = None
    while True:
        print("\nOpciones:")
        print("1. Generar N objetos")
        print("2. Visualizar objetos")
        print("3. Guardar objetos en archivo")
        print("4. Calcular velocidad promedio")
        print("5. Buscar objeto con mayor altitud en archivo")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            N = int(input("Ingrese la cantidad de objetos a generar: "))
            objetos = [ObjetoMedicion() for _ in range(N)]
            print(f"Se generaron {N} objetos.")
        
        elif opcion == "2":
            if objetos:
                visualizar_objetos(objetos)
            else:
                print("No hay objetos generados aún.")
        
        elif opcion == "3":
            if objetos:
                archivo_guardado = input("Ingrese el nombre del archivo (con extensión .csv): ")
                persistir_objetos(objetos, archivo_guardado)
            else:
                print("No hay objetos para guardar.")
        
        elif opcion == "4":
            if objetos:
                calcular_velocidad_promedio(objetos)
            else:
                print("No hay objetos generados aún.")
        
        elif opcion == "5":
            if archivo_guardado:
                buscar_mayor_altitud_archivo(archivo_guardado)
            else:
                print("Debe guardar los objetos en un archivo antes de buscar.")
        
        elif opcion == "6":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
