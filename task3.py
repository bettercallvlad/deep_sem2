# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно

num = int(input('Число: '))

DIV_BIN = 2
DIV_OCT = 8
LIMIT = 0

for divider in DIV_BIN, DIV_OCT:
    num_to_system: int = num
    result: str = ''
    while num_to_system > LIMIT:
        result += str(num_to_system % divider)
        num_to_system //= divider
    result = result[::-1]
    for_check: str = bin(num) if divider == DIV_BIN else oct(num)
    print(f"Результат: {result}, Встроенная: {for_check}")
