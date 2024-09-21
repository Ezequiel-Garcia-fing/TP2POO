#ifndef XMLCONVERTER_H
#define XMLCONVERTER_H

#include <vector>
#include <string>

class XMLConverter {
public:
    std::string convertToXML(const std::vector<std::vector<std::string>>& data);
};

#endif
