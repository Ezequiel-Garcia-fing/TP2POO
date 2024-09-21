# main.py

from serial_communication import SerialCommunication
from data_handler import DataHandler

def main():
    try:
        serial_com = SerialCommunication()
        data_handler = DataHandler()

        while True:
            char = input("Ingresa 'x' para XML, 'j' para JSON, 'c' para CSV, o 'q' para salir: ").lower()
            if char == 'q':
                break

            serial_com.send_data(char)  # Envía el carácter al Arduino
            data = serial_com.receive_data()  # Recibe todas las líneas de datos del Arduino

            if char == 'c':
                parsed_data = data_handler.parse_csv(data)  # Si es CSV, lo parseamos como tal
            elif char == 'j':
                parsed_data = data_handler.parse_json(data)  # Si es JSON, lo parseamos como tal
            elif char == 'x':
                parsed_data = data_handler.parse_xml(data)  # Si es XML, lo parseamos como tal
            else:
                continue

            data_handler.save_to_csv(parsed_data)  # Guardar los datos en CSV

    except Exception as e:
        print(f"Error en el programa: {e}")
    finally:
        serial_com.close()

if __name__ == "__main__":
    main()
