#include "CSVFile.h"
#include <fstream>
#include <sstream>
#include <stdexcept>

CSVFile::CSVFile(const std::string& fileName) : fileName(fileName) {}

std::vector<std::vector<std::string>> CSVFile::readCSV() {
    std::ifstream file(fileName);
    if (!file.is_open()) {
        throw std::runtime_error("Error: No se pudo abrir el archivo CSV: " + fileName);
    }

    std::vector<std::vector<std::string>> data;
    std::string line, cell;

    while (std::getline(file, line)) {
        std::vector<std::string> row;
        std::stringstream lineStream(line);
        while (std::getline(lineStream, cell, ',')) {
            row.push_back(cell);
        }
        data.push_back(row);
    }

    if (data.empty()) {
        throw std::runtime_error("Error: El archivo CSV está vacío o tiene un formato incorrecto.");
    }

    file.close();
    return data;
}
