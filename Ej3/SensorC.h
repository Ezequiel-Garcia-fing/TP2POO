#ifndef SENSORC_H
#define SENSORC_H

#include "Sensor.h"

class SensorC : public Sensor {
public:
    SensorC(const std::string& ip);
    void leerDatos() override;
};

#endif // SENSORC_H
