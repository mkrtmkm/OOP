import math

def taylor_terms(x):
    term = x
    k = 0
    yield 2 * term

    while True:
        k += 1
        term *= (x ** 2) * (2 * k - 1) / (2 * k + 1)
        yield 2 * term

def taylor_sum_counter(x, n):
    if abs(x) >= 1:
        raise ValueError("|x| має бути менше 1")

    gen = taylor_terms(x)
    total = 0.0
    for _ in range(n):
        total += next(gen)
    return total

def taylor_sum_epsilon(x, epsilon=1e-6, max_iter=1000):
    if abs(x) >= 1:
        raise ValueError("|x| має бути менше 1")

    gen = taylor_terms(x)
    total = 0.0
    for k in range(max_iter):
        term = next(gen)
        total += term
        if abs(term) < epsilon:
            return total, k + 1
    return total, max_iter

def write_to_file(x_values, n=10, filename="res_e.txt"):
    with open(filename, 'w', encoding='utf-8') as f:

        f.write("Цикл з лічильником:\n")
        f.write("x\tНаближене\tMath\t\tРізниця\n")
        for x in x_values:
            try:
                approx = taylor_sum_counter(x, n)
                exact = math.log((1 + x) / (1 - x))
                f.write(f"{x:.3f}\t{approx:.8f}\t{exact:.8f}\t{abs(approx - exact):.2e}\n")
            except ValueError:
                continue

        f.write("\nЦикл з умовою :\n")
        f.write("x\tНаближене\tMath\t\tРізниця\n")
        for x in x_values:
            try:
                approx, iterations = taylor_sum_epsilon(x)
                exact = math.log((1 + x) / (1 - x))
                f.write(f"{x:.3f}\t{approx:.8f}\t{exact:.8f}\t{abs(approx - exact):.2e}\n")
            except ValueError:
                continue

if __name__ == "__main__":
    test_values = [0.1, 0.3, 0.5, 0.7, 0.9]
    write_to_file(test_values)
