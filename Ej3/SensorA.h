#ifndef SENSORA_H
#define SENSORA_H

#include "Sensor.h"

class SensorA : public Sensor {
public:
    SensorA(const std::string& ip);
    void leerDatos() override;
};

#endif // SENSORA_H
