# data_handler.py

import csv
import json
import xml.etree.ElementTree as ET

class DataHandler:
    def __init__(self, filename='datos.csv'):
        self.filename = filename
        self.init_csv_file()

    def init_csv_file(self):
        """Crea archivo CSV con encabezados si no existe"""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['dispositivo_id', 'porcentaje_valvula', 'estado_nivel', 'caudal'])

    def save_to_csv(self, data_dict):
        """Guarda los datos en un archivo CSV"""
        try:
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([data_dict['dispositivo_id'], 
                                 data_dict['porcentaje_valvula'], 
                                 data_dict['estado_nivel'], 
                                 data_dict['caudal']])
            print(f"Datos guardados en {self.filename}")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
            raise

    def parse_csv(self, data):
        """Parsea una cadena CSV y la convierte en un diccionario"""
        parts = data.split(',')
        return {
            'dispositivo_id': parts[0],
            'porcentaje_valvula': parts[1],
            'estado_nivel': parts[2],
            'caudal': parts[3]
        }

    def parse_json(self, data):
        """Parsea una cadena JSON y la convierte en un diccionario"""
        try:
            data_dict = json.loads(data)
            return {
                'dispositivo_id': data_dict.get('dispositivo_id'),
                'porcentaje_valvula': data_dict.get('porcentaje_valvula'),
                'estado_nivel': data_dict.get('estado_nivel'),
                'caudal': data_dict.get('caudal')
            }
        except json.JSONDecodeError as e:
            print(f"Error al parsear JSON: {e}")
            raise

    def parse_xml(self, data):
        """Parsea una cadena XML y la convierte en un diccionario"""
        try:
            root = ET.fromstring(data)
            return {
                'dispositivo_id': root.find('dispositivo_id').text,
                'porcentaje_valvula': root.find('porcentaje_valvula').text,
                'estado_nivel': root.find('estado_nivel').text,
                'caudal': root.find('caudal').text
            }
        except ET.ParseError as e:
            print(f"Error al parsear XML: {e}")
            raise
