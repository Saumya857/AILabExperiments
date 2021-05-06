
#WEEK 3- ##Constraint Satisfaction Problem

#Title:- Crypto Arithmetic Puzzle





#A cryptarithmetic puzzle is a mathematical exercise where the digits of some numbers are represented by letters (or symbols). Each letter represents a unique digit. The goal is to #find the digits such that a given mathematical equation is verified:

#  CP
# +IS
# +FUN
# = TRUE

####Approach 1
''''
First attempt to solve equation CP + IS + FUN = TRUE
where each letter represents a unique digit.

This problem has 72 different solutions in base 10.
'''
from ortools.sat.python import cp_model
from ortools.sat.python.cp_model import VarArraySolutionPrinter

model = cp_model.CpModel()
base = 10

c = model.NewIntVar(1, base - 1, 'C')
p = model.NewIntVar(0, base - 1, 'P')
i = model.NewIntVar(1, base - 1, 'I')
s = model.NewIntVar(0, base - 1, 'S')
f = model.NewIntVar(1, base - 1, 'F')
u = model.NewIntVar(0, base - 1, 'U')
n = model.NewIntVar(0, base - 1, 'N')
t = model.NewIntVar(1, base - 1, 'T')
r = model.NewIntVar(0, base - 1, 'R')
e = model.NewIntVar(0, base - 1, 'E')

# We need to group variables in a list to use the constraint AllDifferent.
letters = [c, p, i, s, f, u, n, t, r, e]

# Verify that we have enough digits.
assert base >= len(letters)

# Define constraints.
model.AddAllDifferent(letters)

# CP + IS + FUN = TRUE
model.Add(c * base + p + i * base + s + f * base * base + u * base +
          n == t * base * base * base + r * base * base + u * base + e)


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count


    ### Solve model.
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter(letters)
    status = solver.SearchForAllSolutions(model, solution_printer)


''''
Attempt to solve equation TWO + TWO = FOUR
where each letter represents a unique digit.
7 solutions obtained

'''
def solutions():
    # letters = ('t', 'w', 'o', 'f', 'o', 'u', 'r')
    all_solutions = list()
    for t in range(9, 0, -1):
        for w in range(9, -1, -1):
            for o in range(9, -1, -1):
                for f in range(9, 0, -1):
                    for u in range(9, -1, -1):
                        for r in range(9, -1, -1):
                          
                            if len(set([t, w, o, f, u, r])) == 6:
                                two = 100 * t + 10*w + o;
                                
                                four = 1000 * f + 100 * o + 10 * u + r
                                if two + two == four:
                                    print(two, two, four)
    return


#WEEK 3- ##Constraint Satisfaction Problem

#Title:- Crypto Arithmetic Puzzle





#A cryptarithmetic puzzle is a mathematical exercise where the digits of some numbers are represented by letters (or symbols). Each letter represents a unique digit. The goal is to #find the digits such that a given mathematical equation is verified:

#  CP
# +IS
# +FUN
# = TRUE

####Approach 1
''''
First attempt to solve equation CP + IS + FUN = TRUE
where each letter represents a unique digit.

This problem has 72 different solutions in base 10.
'''
from ortools.sat.python import cp_model
from ortools.sat.python.cp_model import VarArraySolutionPrinter

model = cp_model.CpModel()
base = 10

c = model.NewIntVar(1, base - 1, 'C')
p = model.NewIntVar(0, base - 1, 'P')
i = model.NewIntVar(1, base - 1, 'I')
s = model.NewIntVar(0, base - 1, 'S')
f = model.NewIntVar(1, base - 1, 'F')
u = model.NewIntVar(0, base - 1, 'U')
n = model.NewIntVar(0, base - 1, 'N')
t = model.NewIntVar(1, base - 1, 'T')
r = model.NewIntVar(0, base - 1, 'R')
e = model.NewIntVar(0, base - 1, 'E')

# We need to group variables in a list to use the constraint AllDifferent.
letters = [c, p, i, s, f, u, n, t, r, e]

# Verify that we have enough digits.
assert base >= len(letters)

# Define constraints.
model.AddAllDifferent(letters)

# CP + IS + FUN = TRUE
model.Add(c * base + p + i * base + s + f * base * base + u * base +
          n == t * base * base * base + r * base * base + u * base + e)


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count


    ### Solve model.
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter(letters)
    status = solver.SearchForAllSolutions(model, solution_printer)


''''
Attempt to solve equation TWO + TWO = FOUR
where each letter represents a unique digit.
7 solutions obtained

'''
def solutions():
    # letters = ('t', 'w', 'o', 'f', 'o', 'u', 'r')
    all_solutions = list()
    for t in range(9, 0, -1):
        for w in range(9, -1, -1):
            for o in range(9, -1, -1):
                for f in range(9, 0, -1):
                    for u in range(9, -1, -1):
                        for r in range(9, -1, -1):
                          
                            if len(set([t, w, o, f, u, r])) == 6:
                                two = 100 * t + 10*w + o;
                                
                                four = 1000 * f + 100 * o + 10 * u + r
                                if two + two == four:
                                    print(two, two, four)
    return


solutions()