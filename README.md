# deep_sem2
## Решение задач со второго семинара курса "Погружение в Python"

### Задачи:
#### Задача №2

Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
* порядковый номер начиная с единицы
* значение
* адрес в памяти
* размер в памяти
* хэш объекта
* результат проверки на целое число только если он положительный
* результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.

#### Задача №3

Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своегорезультата, а не для решения.
Дополнительно:
Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления.
Избегайте магических чисел. Добавьте аннотацию типов где это возможно


#### Задача №4

Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
Диаметр не превышает 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.

#### Задача №5

Напишите программу, которая решает квадратные уравнения даже если
дискриминант отрицательный.
Используйте комплексные числа
для извлечения квадратного корня.

#### Задача №6

Напишите программу банкомат.
* Начальная сумма равна нулю
* Допустимые действия: пополнить, снять, выйти
* Сумма пополнения и снятия кратны 50 у.е.
* Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
* После каждой третей операции пополнения или снятия начисляются проценты - 3%
* Нельзя снять больше, чем на счёте
* При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
* Любое действие выводит сумму денег
