from math import factorial


# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

def fact(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


print('Задача #1')

print('a)')
n = fact(52, 4)
print(f'Всевозможные комбинации = {n}')

m = fact(13, 4)
print(f'Все комбинации с крестями = {m}')

clubs = m / n
clubs = round(clubs, 4)
print(f'Вероятность исхода, где в картах все крести = {clubs * 100}%')

print('b)')
m_Ace = fact(52, 4) - fact(48, 4)
if m_Ace == float(m_Ace):
    m_Ace = round(m_Ace, 4)
print(f'Всевозможные комбинации = {n}')
print(f'Комбинация без тузов  = {m_Ace}')

one_Ace = m_Ace / n
one_Ace = round(one_Ace, 4)
print(f'Вероятность исхода, где в картах хотя бы один туз  = {one_Ace * 100}%')

# ================================================================================================


# ЗАДАЧА 2
# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек,
# не знающий код, откроет дверь с первой попытки?
print()
print('Задача #2')

n1 = fact(10, 3)
print(f'Всевозможные комбинации = {n1}')

code_num = 1 / n1
code_num = round(code_num, 4)
print(f'Вероятность угадывания с первого раза {code_num * 100}%')

# ================================================================================================
# ЗАДАЧА 3
# В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?

print()
print('Задача #3')

n2 = fact(15, 3)
print(f'Всего комбинаций на извлеченные детали = {n2}')
m2 = fact(9, 3)
print(f'Всего комбинаций на окрашенные детали = {m2}')

details = m2 / n2
details = round(details, 4)

print(f'Вероятность извлечения окрашенных деталей {details * 100}%')

# ================================================================================================
# ЗАДАЧА 4
# В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

print()
print('Задача #4')

n3 = fact(100, 2)
print(f'возможные варианты выбора двух билетов из 100 = {n3}')

m3 = fact(2, 2)
print(f'число благоприятных исходов = {m3}')

tickets = m3 / n3
tickets = round(tickets, 4)

print(f'Вероятность что билеты вытгрышные {tickets*100}%')
