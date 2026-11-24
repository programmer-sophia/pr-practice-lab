def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Потрібно вводити числа!")
    return a + b


print("Result:", add(2, 3))