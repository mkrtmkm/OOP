def product_generator(n):
    P = 1.0
    yield P  # P_0 = 1 (опціонально)
    for k in range(1, n + 1):
        P *= (1 + 1 / (k ** 2))
        yield P

def compute_product(n):
    P = 1.0
    for k in range(1, n + 1):
        P *= (1 + 1 / (k ** 2))
    return P

def compute_product_epsilon(epsilon=1e-6):
    P = 1.0
    k = 1
    while True:
        term = (1 + 1 / (k ** 2))
        P *= term
        if abs(term - 1) < epsilon:
            break
        k += 1
    return P, k

def write_to_file(n, filename="res_b.txt"):
    with open(filename, 'w', encoding='utf-8') as f:

        f.write("Цикл з лічильником:\n")
        P = 1.0
        for k in range(1, n + 1):
            P *= (1 + 1 / (k ** 2))
            f.write(f"P_{k} = {P}\n")

        f.write("\nГенератор-функція:\n")
        gen = product_generator(n)
        next(gen)
        for k in range(1, n + 1):
            f.write(f"P_{k} = {next(gen)}\n")

        P_final, iterations = compute_product_epsilon()
        f.write(f"\nЦикл з умовою:\n")
        f.write(f"Остаточний P = {P_final}")


if __name__ == "__main__":
    n = 5
    write_to_file(n)