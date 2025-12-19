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

using namespace libcellml;

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

void printAst(AnalyserEquationAstPtr &ast, std::string prepend)
{
    if (ast == nullptr)
    {
        return;
    }

    std::cout << "- " << prepend;
    std::cout << "Type - " << ast->typeAsString(ast->type());
    auto var = ast->variable();
    if (var != nullptr)
    {
        std::cout << ", Variable - " << var->name();
    }
    auto value = ast->value();
    if (!value.empty())
    {
        std::cout << ", Value - " << value;
    }
    std::cout << std::endl;

    printAst(ast->leftChild(), prepend + "  ");
    printAst(ast->rightChild(), prepend + "  ");
}

int main()
{

    std::string libcellmlPath = "../../../cellml/libcellml";
    // std::string inputFile = "libcellml/model.not.ordered.cellml";
    std::string inputFile = "/sine_approximations_import.xml";
    // std::string cellmlPath = "../../../output/";
    // std::string inputFile = "unarranged_algebraic_equation.cellml";
    std::string outputPath = "../../../output/";
    std::string outputFile = "rlycoolpython.py";

    std::string fullInputPath = libcellmlPath + inputFile;
    std::string fullOutputPath = outputPath + outputFile;

    std::cout << "Opening CellML file..." << std::endl;
    std::ifstream inFile(fullInputPath);
    std::stringstream inFileContents;
    inFileContents << inFile.rdbuf();

    std::cout << "Parsing CellML file..." << std::endl;
    ParserPtr parser = Parser::create(false);
    ModelPtr model = parser->parseModel(inFileContents.str());
    logIssues(parser);

    if (model == nullptr)
    {
        std::cout << "Unable to parse model";
        return 1;
    }

    auto importer = libcellml::Importer::create();
    importer->resolveImports(model, libcellmlPath);
    model = importer->flattenModel(model);

    logIssues(importer);

    std::cout << "Validating model..." << std::endl;
    ValidatorPtr validator = Validator::create();
    validator->validateModel(model);
    logIssues(validator);

    std::cout << "Analysing model..." << std::endl;
    AnalyserPtr analyser = Analyser::create();
    analyser->analyseModel(model);
    AnalyserModelPtr analysedModel = analyser->analyserModel();

    logIssues(analyser);
    std::string modelType = AnalyserModel::typeAsString(analysedModel->type());
    std::cout << "Model Type: " << modelType << std::endl;
    std::cout << "Algebraic Variables " << analysedModel->algebraicVariableCount() << std::endl;
    for (size_t i = 0; i < analysedModel->algebraicVariableCount(); ++i)
    {
        AnalyserVariablePtr var = analysedModel->algebraicVariable(i);
        std::cout << " - " << var->variable()->name() << std::endl;
    }
    std::cout << "States " << analysedModel->stateCount() << std::endl;
    for (size_t i = 0; i < analysedModel->stateCount(); ++i)
    {
        AnalyserVariablePtr var = analysedModel->state(i);
        std::cout << " - " << var->variable()->name() << std::endl;
    }
    std::cout << "Computed Constants " << analysedModel->computedConstantCount() << std::endl;
    for (size_t i = 0; i < analysedModel->computedConstantCount(); ++i)
    {
        AnalyserVariablePtr var = analysedModel->computedConstant(i);
        std::cout << " - " << var->variable()->name() << std::endl;
    }
    std::cout << "Constants " << analysedModel->constantCount() << std::endl;
    for (size_t i = 0; i < analysedModel->constantCount(); ++i)
    {
        AnalyserVariablePtr var = analysedModel->constant(i);
        std::cout << " - " << var->variable()->name() << std::endl;
    }
    std::cout << "External vars " << analysedModel->externalVariableCount() << std::endl;

    std::cout << "Equations " << analysedModel->analyserEquationCount() << std::endl;
    for (size_t i = 0; i < analysedModel->analyserEquationCount(); ++i)
    {
        AnalyserEquationPtr eq = analysedModel->analyserEquation(i);
        std::cout << "EQUATION - " << eq->typeAsString(eq->type()) << std::endl;
        printAst(eq->ast(), "");
    }

    // std::cout << "Outputing CellML file..." << std::endl;
    // libcellml::PrinterPtr printer = libcellml::Printer::create();
    // std::string serialisedModel = printer->printModel(model);
    // std::ofstream outFile(fullOutputPath);
    // outFile << serialisedModel;
    // outFile.close();
    // std::cout << inputFile << " has been written to: " << fullOutputPath << std::endl;

    std::cout << "Generating Python code..." << std::endl;
    GeneratorPtr generator = Generator::create();
    if (generator == nullptr)
    {
        return 1;
    }
    auto generatorProfile = GeneratorProfile::create(GeneratorProfile::Profile::PYTHON);
    if (generatorProfile == nullptr)
    {
        std::cout << "bricks" << std::endl;
    }

    auto code = generator->implementationCode(analysedModel, generatorProfile);
    std::ofstream outFile(fullOutputPath);
    outFile << code;
    outFile.close();
    std::cout << "Code has been written to: " << fullOutputPath << std::endl;

    return 0;
}
