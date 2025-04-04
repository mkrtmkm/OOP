from Rational import Rational

def parse_term(token):
    if '/' in token:
        return Rational(token)
    else:
        return Rational(int(token), 1)

def compute_expression(expr):
    tokens = expr.strip().split()
    if not tokens:
        return None

    result = parse_term(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        next_term = parse_term(tokens[i + 1])
        if op == '+':
            result = result + next_term
        elif op == '-':
            result = result - next_term
        elif op == '*':
            result = result * next_term
        elif op == '/':
            result = result / next_term
        else:
            raise ValueError(f"Невідомий оператор: {op}")
        i += 2
    return result

def main():
    input_file = "input01.txt"
    output_file = "output.txt"

    try:
        with open(input_file, "r") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue
                try:
                    result = compute_expression(line)
                    output_line = f"{line} = {result} ≈ {result():.6f}"
                    print(output_line)
                    outfile.write(output_line + "\n")
                except Exception as e:
                    error_line = f"Помилка у виразі '{line}': {e}"
                    print(error_line)
                    outfile.write(error_line + "\n")
    except FileNotFoundError:
        print(f"Файл '{input_file}' не знайдено.")

if __name__ == "__main__":
    main()
