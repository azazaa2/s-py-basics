# Строки
name = 'azamat'
multi_line = '''azamat
azamat'''

# Числа
integer = 43
floating = 3.21

# Логические значения (С большой буквы)
is_true = True
is_false = False

# Списки (аналог массивов в JS)
fruits = ['яблоки', 'банан', 'апельсин']

# Кортежи (неизменяемые списки)
coordinates = (10, 20)

# Словари (аналог объектов в JS)
person = {
    'name': 'azamat',
    'age': 20
}

# Множества (уникальные значения)
unique_numbers = {1, 2, 3, 3, 4, 5, 5, 6, 2, 5, 4, 1} # Результат: {1, 2, 3, 4, 5, 6}

# условия
con = 'con'

if con:
    con = 'not-con'

# Функции
def get_cons():
    cons = ['con_1', 'con_2', 'con_3', 'con_4']
    return cons

def set_con(con='def-con'):
    return f'Это {con}'

con = set_con('not-con')
default_con = set_con()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5) # 120

# Циклы
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

count = 1
while count < 5:
    print(count)
    count+=1