#ifndef CSVFILE_H
#define CSVFILE_H

#include <vector>
#include <string>

class CSVFile {
public:
    CSVFile(const std::string& fileName);
    std::vector<std::vector<std::string>> readCSV();

private:
    std::string fileName;
};

#endif
