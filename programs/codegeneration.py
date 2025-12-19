from libcellml import Parser, Analyser, AnalyserModel, Generator, Validator, GeneratorProfile
from pathlib import Path

cwd = Path.cwd()

model_path = cwd.parent / "cellml/testing"
model_file_name = "simple_rearrangement.cellml"
output_file_path = cwd.parent / "output/"
output_file_name = "output.py"

def log_issues(libcellobj):
    print(f'{libcellobj.issueCount()} issue/s found for {libcellobj.__class__}')
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

    print("Validating model...")
    validator = Validator()
    validator.validateModel(model)
    log_issues(validator)

    print("Analysing model...")
    analyser = Analyser()
    analyser.analyseModel(model)
    analysed_model = analyser.analyserModel()
    log_issues(analyser)
    print(f'Model Type: {AnalyserModel.typeAsString(analysed_model.type())}')

    print("Generating Python code...")
    generator = Generator()
    generator_profile = GeneratorProfile(GeneratorProfile.Profile.PYTHON)
    code = generator.implementationCode(analysed_model, generator_profile)
    write_file = open(output_file_path / output_file_name, "w")
    write_file.write(code)
    print(f'{model_file_name} has been written to {output_file_path / output_file_name}')

if __name__ == "__main__":
    main()
