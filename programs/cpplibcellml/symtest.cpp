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

void solve(SymEngine::RCP<const SymEngine::Boolean> equation, SymEngine::RCP<const SymEngine::Symbol> var) {
    SymEngine::RCP<const SymEngine::Set> slns = SymEngine::solve(equation, var);

    SymEngine::vec_basic container = slns->get_args();
    std::cout << container.size() << std::endl;
    for (SymEngine::RCP<const SymEngine::Basic> element : container) {
        std::cout << *element.get() << std::endl;
    }
}

void test1() {
    std::string  s = "-1^2";
    auto res = SymEngine::parse(s);
    std::cout << SymEngine::eq(*res, *SymEngine::integer(-1)) << std::endl;
    std::cout << SymEngine::eq(*res, *SymEngine::parse(res->__str__())) << std::endl;
}

void test2() {
    SymEngine::RCP<const SymEngine::Symbol> x = SymEngine::symbol("x");
    SymEngine::RCP<const SymEngine::Symbol> y = SymEngine::symbol("y");

    SymEngine::RCP<const SymEngine::Boolean> poly = SymEngine::Eq(x, y);
    solve(poly, x);
}

int main()
{
    auto a = SymEngine::symbol("a");
    auto b = SymEngine::symbol("b");
    auto c = SymEngine::number(3);

    SymEngine::set_basic statements = { SymEngine::contains(b, SymEngine::reals()) };
    SymEngine::Assumptions assumptions(statements);

    SymEngine::RCP<const SymEngine::Boolean> equality = SymEngine::Eq(SymEngine::tan(a), b);

    solve(equality, a);
    return 0;
}
