# serial_communication.py

import serial #modulo serial para trabajar con comunicacion serial
import time # modulo para usar retrasos en la ejecucion del cogido

class SerialCommunication:
    def __init__(self, port='COM3', baudrate=19200, timeout=1): # timeout:tiempo de espera
        try:
            self.ser = serial.Serial(port, baudrate, timeout=timeout) # serial es la libreria y Serial es una clase dentro de esa libreria, al igualarlo a ser podemos interactuar con los puertos mediante los metodos de la clase Serial (ej readline(), close())
            time.sleep(2)  # Esperar a que la conexión se estabilice  # es decir ser es un objeto que puede realizar acciones especificas como leer o escribir datos por el puerto serie
            self.clear_initial_messages()
            print(f"Conectado al puerto {port}")
        except serial.SerialException as e:
            print(f"Error al abrir el puerto: {e}")
            raise

    def clear_initial_messages(self):
        """Limpia cualquier mensaje inicial enviado por el Arduino."""
        time.sleep(1)
        while self.ser.in_waiting:
            self.ser.readline()  # Ignorar cualquier mensaje inicial
        print("Mensajes iniciales eliminados")

    def send_data(self, char):
        """Envía un carácter al Arduino para recibir datos"""
        if char not in ['x', 'j', 'c']:
            raise ValueError("Carácter inválido. Debe ser 'x', 'j' o 'c'.")
        try:
            self.ser.write(char.encode())  # write es un metodo de la clase Serial que pertenece a la libreria serial
            print(f"Carácter '{char}' enviado al Arduino")
        except Exception as e:
            print(f"Error al enviar el carácter: {e}")
            raise

    def receive_data(self):
        """Recibe todas las líneas de datos enviadas por el Arduino hasta una línea vacía"""
        response_lines = []
        try:
            while True:
                line = self.ser.readline().decode('utf-8').strip()
                if line:  # Si no es una línea vacía, la agregamos a la lista
                    response_lines.append(line)
                else:
                    break  # Si es una línea vacía, terminamos de leer
            response = "\n".join(response_lines)  # Juntamos todas las líneas en un solo string
            print(f"Datos recibidos: {response}")
            return response
        except Exception as e:
            print(f"Error al recibir datos: {e}")
            raise

    def close(self):
        """Cierra la conexión serial"""
        if self.ser.is_open:
            self.ser.close()
            print("Conexión serial cerrada")
