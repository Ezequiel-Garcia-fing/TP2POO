#ifndef SENSORB_H
#define SENSORB_H

#include "Sensor.h"

class SensorB : public Sensor {
public:
    SensorB(const std::string& ip);
    void leerDatos() override;
};

#endif // SENSORB_H
