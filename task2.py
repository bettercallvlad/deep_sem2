# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

data = ['stroka', 10, 5/2, 10, ]

for i in range(len(data)):
    adress = id(data[i])
    size = data[i].__sizeof__()
    hash_obj = hash(data[i])
    res_int = 'INT' if isinstance(data[i], int) else ''
    res_str = 'STR' if isinstance(data[i], str) else ''
    res_float = 'FLOAT' if isinstance(data[i], float) else ''
    print(f"""{i+1} Значение: {data[i]}
Адрес в памяти: {adress}
Размер: {size}
Хэш: {hash_obj}
{res_str} {res_int} {res_float}""", end='\n\n')
