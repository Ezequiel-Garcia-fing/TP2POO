# operaciones.py
import csv

# Persistir objetos en un archivo CSV
def persistir_objetos(objetos, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Velocidad (m/s)", "Distancia (m)", "Altitud (m)"])
        for obj in objetos:
            writer.writerow([obj.velocidad, obj.distancia, obj.altitud])
    print(f"Datos guardados en {filename}.")

# Visualizar los datos en formato tabular
def visualizar_objetos(objetos):
    print(f"{'Velocidad (m/s)':<20}{'Distancia (m)':<20}{'Altitud (m)':<15}")
    print("-" * 55)
    for obj in objetos:
        print(f"{obj.velocidad:<20.2f}{obj.distancia:<20.2f}{obj.altitud:<15}")

# Calcular la velocidad promedio
def calcular_velocidad_promedio(objetos):
    total_velocidad = sum(obj.velocidad for obj in objetos)
    promedio = total_velocidad / len(objetos) if objetos else 0
    print(f"Velocidad promedio: {promedio:.2f} m/s")
    return promedio

# Buscar el objeto con mayor altitud en un archivo CSV
def buscar_mayor_altitud_archivo(filename):
    try:
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            mayor_altitud = -1
            objeto_mayor = None
            for row in reader:
                altitud = int(row['Altitud (m)'])
                if altitud > mayor_altitud:
                    mayor_altitud = altitud
                    objeto_mayor = row
            
            if objeto_mayor:
                print(f"Objeto con mayor altitud: Velocidad: {objeto_mayor['Velocidad (m/s)']} m/s, "
                      f"Distancia: {objeto_mayor['Distancia (m)']} m, Altitud: {objeto_mayor['Altitud (m)']} m")
            else:
                print("No se encontraron datos en el archivo.")
                
    except FileNotFoundError:
        print(f"El archivo {filename} no existe. Por favor, genere y guarde los objetos primero.")
