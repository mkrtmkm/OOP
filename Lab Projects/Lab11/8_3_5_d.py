def a_k_generator():
    a = [1, 1, 1]
    for num in a:
        yield num
    while True:
        next_val = a[-1] + a[-3]
        a.append(next_val)
        yield next_val

def compute_Sn_counter(n):
    if n == 0:
        return 0.0

    gen = a_k_generator()
    S = 0.0
    for k in range(1, n + 1):
        a_k = next(gen)
        S += a_k / (2 ** k)
    return S

def compute_Sn_epsilon(epsilon=1e-6, max_iter=1000):
    gen = a_k_generator()
    S = 0.0
    prev_S = 0.0

    for k in range(1, max_iter + 1):
        a_k = next(gen)
        term = a_k / (2 ** k)
        S += term

        if k > 3 and abs(S - prev_S) < epsilon:
            return S, k

        prev_S = S

    return S, max_iter

def write_to_file(n_values, filename="res_d.txt"):
    with open(filename, 'w', encoding='utf-8') as f:

        f.write("Цикл з лічильником:\n")
        for n in n_values:
            Sn = compute_Sn_counter(n)
            f.write(f"{n}\t{Sn}\n")

        f.write("\nГенератор послідовності a_k:\n")
        gen = a_k_generator()
        for k in range(1, max(n_values) + 1):
            f.write(f"{k}\t{next(gen)}\n")

        final_sum, iterations = compute_Sn_epsilon()
        f.write(f"\nЦикл з умовою:\n")
        f.write(f"Остаточна сума: {final_sum}\n")

if __name__ == "__main__":
    n_values = range(1, 11)
    write_to_file(n_values)