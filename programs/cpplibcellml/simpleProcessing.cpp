/**
 *  TUTORIAL 1: READING AND WRITING A CELLML FILE
 *
 *  By the time you have worked through Tutorial 1 you will be able to:
 *    - Read the contents of a CellML file;
 *    - Deserialise its contents using the Parser to create a Model structure;
 *    - Investigate the hierarchical contents of the Model, including the
 *      Components, Variables, and maths; and
 *    - Serialise the model and write to another file.
 */

#include <fstream>
#include <iostream>
#include <sstream>
#include <typeinfo>

#include <libcellml>

void logIssues(std::shared_ptr<libcellml::Logger> logger)
{
    int errorCount = logger->errorCount();

    std::cout << errorCount << " issue/s found" << std::endl;

    for (int i = 0; i < errorCount; i++)
    {
        libcellml::IssuePtr issue = logger->issue(i);
        if (issue == nullptr)
        {
            std::cout << "Null pointer issue?!" << std::endl;
        }
        else
        {
            std::cout << issue->description() << std::endl;
        }
    }
}

int main()
{
    std::string cellmlPath = "../../../cellml/";
    std::string inputFile = "simple_capillary/simple_capillary.cellml";
    std::string outputPath = "../../../output/";
    std::string outputFile = "output.cellml";

    std::string fullInputPath = cellmlPath + inputFile;
    std::string fullOutputPath = outputPath + outputFile;

    std::cout << "Opening CellML file..." << std::endl;
    std::ifstream inFile(fullInputPath);
    std::stringstream inFileContents;
    inFileContents << inFile.rdbuf();

    std::cout << "Parsing CellML file..." << std::endl;
    libcellml::ParserPtr parser = libcellml::Parser::create(false);
    libcellml::ModelPtr model = parser->parseModel(inFileContents.str());
    logIssues(parser);

    if (model == nullptr)
    {
        std::cout << "Unable to parse model";
        return 1;
    }

    std::cout << "Validating model..." << std::endl;
    libcellml::ValidatorPtr validator = libcellml::Validator::create();
    validator->validateModel(model);
    logIssues(validator);

    std::cout << "Analysing model..." << std::endl;
    libcellml::AnalyserPtr analyser = libcellml::Analyser::create();
    analyser->analyseModel(model);
    libcellml::AnalyserModelPtr analysedModel = analyser->analyserModel();
    logIssues(analyser);
    std::string modelType = libcellml::AnalyserModel::typeAsString(analysedModel->type());
    std::cout << "Model Type: " << modelType << std::endl;

    std::cout << "Outputing CellML file..." << std::endl;
    libcellml::PrinterPtr printer = libcellml::Printer::create();
    std::string serialisedModel = printer->printModel(model);
    std::ofstream outFile(fullOutputPath);
    outFile << serialisedModel;
    outFile.close();
    std::cout << inputFile << " has been written to: " << fullOutputPath << std::endl;

    return 0;
}
