"""
Created by James Park
"""

VARIABLES = 'abcdefghijklmnopqrstuvwxyz'
FUNCTIONS = {'add': '+', 'subtract': '-'}


class NewFormula:
    """
    Creates a new formula according to the user's design.
    """

    def __init__(self, name, num_variables, description=''):
        """
        Creates a new formula designed by the user.

        @type name: str
        @type num_variables: int
        @type description: str
        """
        self.name = name
        self.num_variables = int(num_variables)
        self.description = description
        self.variable_list = []
        self.formula = ''

    def create_variables(self):
        """
        Creates variables according to how many variables the
        user inputed

        @type self: NewFormula
        @rtype: None
        """
        for i in range(self.num_variables):
            self.variable_list.append(VARIABLES[i])

    def compile_formula(self, formula):
        """
        Compiles the formula according the user's design.

        @type self: NewFormula
        @type formula: str
        @rtype: None
        """
        item_list = list(formula.strip())
        formula_list = list(self.formula.strip())
        i, j = 0, 0
        while i < len(item_list):
            sum = int(item_list[i])
