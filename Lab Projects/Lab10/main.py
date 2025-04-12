from RationalList import RationalList
from Rational import Rational


def parse_line_to_rationals(line):
    tokens = line.strip().split()
    result = RationalList()
    for token in tokens:
        if '/' in token:
            result.append(Rational(token))
        else:
            result.append(int(token))
    return result


def process_file(filename):
    try:
        output = f"===== Обробка файлу {filename} =====\n"
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                rlist = parse_line_to_rationals(line)
                result = rlist.sum()
                output += f"Рядок {line_num}: {line.strip()}\n"
                output += f"Відсортовано: {' '.join(str(r) for r in rlist)}\n"
                output += f"Сума = {result} ≈ {result():.6f}\n\n"
        return output
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return None



def main():
    input_files = ["input02.txt"]
    output_file = "output.txt"

    with open(output_file, "w", encoding="utf-8") as outfile:
        for fname in input_files:
            result = process_file(fname)
            if result:
                outfile.write(result)


if __name__ == "__main__":
    main()
