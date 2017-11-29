from functionality import NewFormula


class Compiler:
    """
    The compiler class.
    """

    def __init__(self):
        """
        @type self: compiler
        @rtype: None
        """
        self.function_list_ = []

if __name__ == '__main__':
    function_name = input("Enter a name for your formula: ")
    num_variables = input("How many variables required: ")
    nf = NewFormula(function_name, num_variables)
    nf.create_variables()
    print('You have the follow variables: ' + nf.variable_list[0] + nf.variable_list[1] + nf.variable_list[2])
    print('Use the variables, and the commands to implement a formula. ')
    formula = input("Compile your formula: ")
    nf.formula = formula
    run_formula_test = input('Run the formula, enter value as a list in order of variables.')
    nf.compile_formula(run_formula_test)
