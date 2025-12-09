from libcellml import Parser, Validator
from pathlib import Path

cwd = Path.cwd()

model_path = cwd.parent / "cellml/testing"
model_file_name = "variable_on_rhs.cellml"

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

    for i in range(model.componentCount()):
        component = model.component(i)
        print(component.math())

if __name__ == "__main__":
    main()
