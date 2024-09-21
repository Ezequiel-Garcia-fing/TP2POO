#include "SensorA.h"
#include <iostream>

SensorA::SensorA(const std::string& ip) : Sensor("A", ip) {}

void SensorA::leerDatos() {
    std::cout << "Leyendo datos de temperatura, humedad y presion del sensor A en IP: " << ip << std::endl;
}
