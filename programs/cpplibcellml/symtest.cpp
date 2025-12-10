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

#include <symengine/parser.h>
#include <symengine/solve.h>

int main()
{
    std::string  s = "-1^2";
    auto res = SymEngine::parse(s);
    std::cout << SymEngine::eq(*res, *SymEngine::integer(-1)) << std::endl;
    std::cout << SymEngine::eq(*res, *SymEngine::parse(res->__str__())) << std::endl;

    SymEngine::RCP<const SymEngine::Symbol> x = SymEngine::symbol("x");
    SymEngine::RCP<const SymEngine::Symbol> y = SymEngine::symbol("y");

    SymEngine::RCP<const SymEngine::Boolean> poly = SymEngine::Eq(x, y);
    SymEngine::RCP<const SymEngine::Set> slns = SymEngine::solve(poly, x);

    SymEngine::vec_basic container = slns->get_args();
    std::cout << container.size() << std::endl;
    for (SymEngine::RCP<const SymEngine::Basic> element : container) {
        std::cout << *element.get() << std::endl;
    }

    return 0;
}
