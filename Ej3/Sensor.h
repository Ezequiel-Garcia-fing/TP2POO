#ifndef SENSOR_H
#define SENSOR_H

#include <string>

class Sensor {
protected:
    std::string tipo;
    std::string ip;
public:
    Sensor(const std::string& tipo, const std::string& ip);
    virtual void leerDatos() = 0;
    virtual ~Sensor() = default;
};

#endif // SENSOR_H
