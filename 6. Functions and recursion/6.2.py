# Функция для возведения числа n в степень k (по умолчанию k = 2)
def power(n, k=2):
    return n ** k

n = float(input("Введите число n: "))

# Вызываем функцию power с одним или двумя аргументами
result = power(n)  # Если не указан k, будет использовано значение по умолчанию (k = 2)

print(f"{n} в степени 2 = {result}")

