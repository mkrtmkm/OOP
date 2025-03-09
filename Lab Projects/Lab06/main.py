from Figures import Triangle, Rectangle, Trapeze, Parallelogram, Circle


def find_max_area_and_perimeter(figures):
    max_area_figure = max(figures, key=lambda f: f.area(), default=None)
    max_perimeter_figure = max(figures, key=lambda f: f.perimeter(), default=None)
    return max_area_figure, max_perimeter_figure


def read_figures_from_file(filename):
    figures = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            try:
                if parts[0] == "Triangle":
                    figures.append(Triangle(float(parts[1]), float(parts[2]), float(parts[3])))
                elif parts[0] == "Rectangle":
                    figures.append(Rectangle(float(parts[1]), float(parts[2])))
                elif parts[0] == "Trapeze":
                    figures.append(Trapeze(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])))
                elif parts[0] == "Parallelogram":
                    figures.append(Parallelogram(float(parts[1]), float(parts[2]), float(parts[3])))
                elif parts[0] == "Circle":
                    figures.append(Circle(float(parts[1])))
            except (ValueError, IndexError) as e:
                print(f"Помилка обробки рядка '{line.strip()}': {e}")
    return figures


def write_results_to_file(output_filename, max_area_figure, max_perimeter_figure):
    with open(output_filename, "w", encoding="utf-8") as file:
        if max_area_figure:
            file.write(f"Фігура з найбільшою площею:\n{max_area_figure}\n\n")
        else:
            file.write("Фігура з найбільшою площею не знайдена.\n\n")

        if max_perimeter_figure:
            file.write(f"Фігура з найбільшим периметром:\n{max_perimeter_figure}\n")
        else:
            file.write("Фігура з найбільшим периметром не знайдена.\n")


if __name__ == "__main__":
    input_filename = "input01.txt"
    output_filename = "output.txt"

    figures = read_figures_from_file(input_filename)

    if figures:
        max_area_figure, max_perimeter_figure = find_max_area_and_perimeter(figures)
        write_results_to_file(output_filename, max_area_figure, max_perimeter_figure)
        print(f"Результати записані у файл {output_filename}")
    else:
        print("У файлі немає коректних фігур.")