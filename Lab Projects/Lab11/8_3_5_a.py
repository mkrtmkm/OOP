def compute_recursive(x, k):
    if k == 0:
        return 1.0
    return compute_recursive(x, k - 1) * (x ** 2) / ((2 * k) * (2 * k - 1))

def sequence_generator(x):
    a = 1.0
    yield a
    k = 1
    while True:
        a *= (x ** 2) / ((2 * k) * (2 * k - 1))
        yield a
        k += 1

def compute_with_counter(x, max_k):
    res = []
    a = 1.0
    res.append(a)
    for k in range(1, max_k + 1):
        a *= (x ** 2) / ((2 * k) * (2 * k - 1))
        res.append(a)
    return res

def compute_with_condition(x, epsilon=1e-6):
    res = []
    gen = sequence_generator(x)
    while True:
        a = next(gen)
        res.append(a)
        if abs(a) < epsilon:
            break
    return res

def write_to_file(x, max_k, filename="res_a.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Цикл з лічильником:\n")
        res = compute_with_counter(x, max_k)
        for k, a in enumerate(res):
            f.write(f"a_{k} = {a}\n")

        f.write("\nЦикл з умовою:\n")
        res = compute_with_condition(x)
        for k, a in enumerate(res):
            f.write(f"a_{k} = {a}\n")


if __name__ == "__main__":
    x = 2.0
    max_k = 10
    write_to_file(x, max_k)
