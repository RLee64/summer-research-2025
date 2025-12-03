from libcellml import Parser, Analyser, AnalyserModel, Printer
from pathlib import Path

cwd = Path.cwd()

model_path = cwd.parent / "cellml/simple_capillary"
model_file_name = "simple_capillary.cellml"
output_file_path = cwd.parent / "output/"
output_file_name = "output.cellml"

def log_issues(libcellobj):
    if libcellobj.issueCount() > 0:
        print(f'Errors picked up from {libcellobj.__class__}')
        for i in range(0, libcellobj.issueCount()):
            print(libcellobj.issue(i).description())

def main():
    print("Opening CellML file...")
    with open(model_path / model_file_name) as f:
        content = f.read()

    print("Parsing CellML file...")
    parser = Parser(False)
    model = parser.parseModel(content)
    log_issues(parser)

    print("Analysing CellML file...")
    analyser = Analyser()
    analyser.analyseModel(model)
    analysed_model = analyser.model()
    log_issues(analyser)
    print(f'Model Type: {AnalyserModel.typeAsString(analysed_model.type())}')

    print("Outputing CellML file...")
    printer = Printer()
    serialised_model = printer.printModel(model)
    write_file = open(output_file_path / output_file_name, "w")
    write_file.write(serialised_model)
    print(f'{model_file_name} has been written to {output_file_path / output_file_name}')

if __name__ == "__main__":
    main()
