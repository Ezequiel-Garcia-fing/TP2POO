#include <fstream>
#include <iostream>
#include "CSVFile.h"
#include "XMLConverter.h"

int main() {
    std::string inputFileName;
    std::string outputFileName;

    std::cout << "Ingrese la ruta completa del archivo CSV: ";
    std::getline(std::cin, inputFileName);

    try {
        CSVFile csvFile(inputFileName);
        auto data = csvFile.readCSV();

        XMLConverter xmlConverter;
        std::string xml = xmlConverter.convertToXML(data);

        std::cout << "Ingrese el nombre del archivo XML de salida: ";
        std::cin >> outputFileName;

        std::ofstream file(outputFileName);
        if (!file.is_open()) {
            throw std::runtime_error("Error: No se pudo crear el archivo XML.");
        }
        file << xml;
        file.close();

        std::cout << "Archivo convertido exitosamente a XML.\n";
    } catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
    }

    return 0;
}
