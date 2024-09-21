# objeto_medicion.py
import random

class ObjetoMedicion:
    def __init__(self):
        self.velocidad = random.uniform(0, 100)  # Velocidad en m/s (real)
        self.distancia = random.uniform(0, 1000) # Distancia en m (real)
        self.altitud = random.randint(0, 10000)  # Altitud en m (entero)

    def __str__(self):
        return f"Velocidad: {self.velocidad:.2f} m/s, Distancia: {self.distancia:.2f} m, Altitud: {self.altitud} m"
