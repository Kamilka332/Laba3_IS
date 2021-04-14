import re
import numpy as np

values = [
    ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з'],
    ['и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р'],
    ['с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'],
    ['ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В'],
    ['Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К'],
    ['Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У'],
    ['Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
    ['Э', 'Ю', 'Я', ' ', '.', ':', '!', '?', ',']
]
P, Y = [], []

pattern = r'[А-я,.:;?! ]+'
phrase = input('Введите фразу с клавиатуры: ')
while re.fullmatch(pattern, phrase) is None:
    phrase = input('Введенная строка некоректна, повторите ввод: ')

key = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 15, 29]
])

# проверка
if not np.linalg.det(key):
    raise Exception('Матрица вырожденная')

if len(phrase) % len(key) == 1:
    phrase += '  '
elif len(phrase) % len(key) == 2:
    phrase += ' '

# array_length = 2
# if not len(phrase) % 3 and len(phrase) % 2:
#     array_length = 3
# elif not len(phrase) % 5 and len(phrase) % 2:
#     array_length = 5
# elif not len(phrase) % 7 and len(phrase) % 2:
#     array_length = 7
# # и так далее
#
# print('Введите ключ:')
# key = np.array([[int(input()) for j in range(array_length)] for i in range(array_length)])
# while not np.linalg.det(key):
#     print('Вы ввели вырожденную матрицу, повторите ввод:')
#     key = np.array([[input() for j in range(array_length)] for i in range(array_length)])

for p in phrase:
    for i in range(len(values)):
        for j in range(len(values[i])):
            if p in values[i][j]:
                P.append(i * len(values[i]) + j + 1)
print(f'Фраза, представленная с помощью таблицы 2: ', end='')
print(*P)

P = np.split(np.array(P), len(P) / key.shape[0])

print('Шифр: ', end='')
for i in range(len(P)):
    Y.append(key.dot(P[i].T))
    print(*key.dot(P[i].T), end=' ')
print()

###########################################
#########Обратная операция#################
###########################################

P.clear()
for i in range(len(Y)):
    P.append(np.linalg.inv(key).dot(np.array(Y[i])))
P = np.array(P).flatten()
P = list(map(int, map(round, P)))
phrase = ''
for p in P:
    for i in range(len(values)):
        for j in range(len(values[i])):
            if p == i * len(values[i]) + j + 1:
                phrase += values[i][j]
print('Расшифрованная фраза: ' + phrase)

# while True:
    # print('Введите ключ:')
    # key = [[int(input()) for j in range(array_length)] for i in range(array_length)]
    #
    # while not np.linalg.det(key):
    #     print('Вы ввели вырожденную матрицу, повторите ввод:')
    #     key = np.array([[input() for j in range(array_length)] for i in range(array_length)])

#     P.clear()
#     for i in range(len(Y)):
#         P.append(np.linalg.inv(key).dot(np.array(Y[i])))
#     P = np.array(P).flatten()
#     P = list(map(int, map(round, P)))
#     phrase = ''
#     for p in P:
#         for i in range(len(values)):
#             for j in range(len(values[i])):
#                 if p == i * len(values[i]) + j + 1:
#                     phrase += values[i][j]
#     print('Расшифрованная фраза: ' + phrase)
