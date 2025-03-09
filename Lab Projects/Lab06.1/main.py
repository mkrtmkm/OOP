from Matrix2D import Matrix2D
from Vector2D import Vector2D
from Solver import Solver

def read_systems(coeff_file, rhs_file):
    systems = []
    with open(coeff_file, "r", encoding="utf-8") as f_coeff, open(rhs_file, "r", encoding="utf-8") as f_rhs:
        for coeff_line, rhs_line in zip(f_coeff, f_rhs):
            coeffs = list(map(float, coeff_line.split()))
            rhs = list(map(float, rhs_line.split()))

            if len(coeffs) == 4 and len(rhs) == 2:
                matrix = Matrix2D(*coeffs)
                vector = Vector2D(*rhs)
                systems.append((matrix, vector))
    return systems

def solve_systems(input_matrix_file, input_rhs_file, output_file):
    systems = read_systems(input_matrix_file, input_rhs_file)

    with open(output_file, "w", encoding="utf-8") as file:
        for i, (matrix, vector) in enumerate(systems, 1):
            solver = Solver(matrix, vector)
            solution = solver.solve()

            file.write(f"Система {i}:\n")
            file.write(f"Матриця коефіцієнтів:\n{matrix}\n")
            file.write(f"Вектор правої частини: {vector}\n")

            if solution:
                file.write(f"Розв'язок: {solution}\n\n")
            else:
                file.write("Система не має розв'язку (вироджена матриця)\n\n")

if __name__ == "__main__":
    solve_systems("matrix_coefficients.txt", "rhs_values.txt", "output.txt")
    print("Розв'язки записані у output.txt")