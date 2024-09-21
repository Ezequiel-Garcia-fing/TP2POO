#ifndef CONTROLADOR_H
#define CONTROLADOR_H

#include "Sensor.h"
#include <vector>
#include <string>

class Controlador {
private:
    std::vector<Sensor*> sensores;
public:
    void agregarSensor(Sensor* sensor);
    void leerDatosSensores();
    void cargarSensoresDesdeArchivo(const std::string& nombreArchivo);
    ~Controlador();
};

#endif // CONTROLADOR_H
