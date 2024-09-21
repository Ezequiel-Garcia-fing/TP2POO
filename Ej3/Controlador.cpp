#include "Controlador.h"
#include "SensorA.h"  // Incluir la cabecera de SensorA
#include "SensorB.h"  // Incluir la cabecera de SensorB
#include "SensorC.h"  // Incluir la cabecera de SensorC
#include <fstream>
#include <sstream>
#include <iostream>

void Controlador::agregarSensor(Sensor* sensor) {
    sensores.push_back(sensor);
}

void Controlador::leerDatosSensores() {
    for (auto& sensor : sensores) {
        sensor->leerDatos();
    }
}

Controlador::~Controlador() {
    for (auto& sensor : sensores) {
        delete sensor;
    }
}

void Controlador::cargarSensoresDesdeArchivo(const std::string& nombreArchivo) {
    std::ifstream archivo(nombreArchivo);
    if (!archivo.is_open()) {
        std::cerr << "No se pudo abrir el archivo de configuración." << std::endl;
        return;
    }

    std::string linea;
    while (std::getline(archivo, linea)) {
        std::istringstream iss(linea);
        std::string tipo, ip;
        if (!(iss >> tipo >> ip)) {
            std::cerr << "Error al leer la línea: " << linea << std::endl;
            continue;
        }

        if (tipo == "A") {
            agregarSensor(new SensorA(ip));
        } else if (tipo == "B") {
            agregarSensor(new SensorB(ip));
        } else if (tipo == "C") {
            agregarSensor(new SensorC(ip));
        } else {
            std::cerr << "Tipo de sensor desconocido: " << tipo << std::endl;
        }
    }
}
