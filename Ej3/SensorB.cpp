#include "SensorB.h"
#include <iostream>

SensorB::SensorB(const std::string& ip) : Sensor("B", ip) {}

void SensorB::leerDatos() {
    std::cout << "Leyendo datos de iluminacion del sensor B en IP: " << ip << std::endl;
}
