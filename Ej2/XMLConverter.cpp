#include "XMLConverter.h"
#include <sstream>
#include <stdexcept>

std::string XMLConverter::convertToXML(const std::vector<std::vector<std::string>>& data) {
    if (data.empty()) {
        throw std::runtime_error("Error: No hay datos para convertir a XML.");
    }

    std::stringstream xml;
    xml << "<root>\n";
    for (size_t i = 1; i < data.size(); ++i) {
        xml << "\t<row>\n";
        for (size_t j = 0; j < data[i].size(); ++j) {
            xml << "\t\t<" << data[0][j] << ">" << data[i][j] << "</" << data[0][j] << ">\n";
        }
        xml << "\t</row>\n";
    }
    xml << "</root>\n";

    return xml.str();
}
