#include "SensorA.h"
#include "SensorB.h"
#include "SensorC.h"
#include "Controlador.h"
#include "Vista.h"

int main() {
    Controlador controlador;
    Vista vista;

    // Cargar sensores desde el archivo de configuración
    controlador.cargarSensoresDesdeArchivo("sensores.cfg");

    // Leer datos de los sensores
    controlador.leerDatosSensores();

    // Mostrar datos (simulación)
    vista.mostrarDatos("Datos de ejemplo");

    return 0;
}
