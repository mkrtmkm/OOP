from Audit3_2_1 import *

def read_file(filename):
    try:
        with open(filename, "r") as file:
            equations = []

            for line in file:
                coefficients = list(map(float, line.split()))
                if len(coefficients) == 2:
                    eq = Equation(*coefficients)
                elif len(coefficients) == 3:
                    eq = QuadraticEquation(*coefficients)
                elif len(coefficients) == 5:
                    eq = BiquadraticEquation(*coefficients)
                else:
                    continue
                equations.append(eq)
    except Exception as e:
        print(f"Error: {e}")


        solution_dict = {
            "no solution":[],
            "one solution":[],
            "two solutions":[],
            "three solutions":[],
            "four solutions":[],
            "inf solutions":[],
        }

        one_solution_values = []

        for eq in equations:
            solutions = eq.solve()
            num_solutions = len(solutions) if isinstance(solutions, tuple) else 0

            if "InfSolutions" in solutions:
                solution_dict["inf solutions"].append(eq.show())

            elif "No Solution" in solutions:
                solution_dict["no solution"].append(eq.show())

            else:
                solution_dict[f"{num_solutions} solutions"].append(eq.show())
                if num_solutions == 1:
                    one_solution_values.append((eq.show(), solutions[0]))

        print(f"Results for {filename}:")
        for key, value in solution_dict.items():
            print(f"{key}: {len(value)}")
            