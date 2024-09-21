#include "SensorC.h"
#include <iostream>

SensorC::SensorC(const std::string& ip) : Sensor("C", ip) {}

void SensorC::leerDatos() {
    std::cout << "Leyendo datos de velocidad del viento del sensor C en IP: " << ip << std::endl;
}
