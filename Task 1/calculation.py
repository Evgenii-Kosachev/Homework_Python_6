# (готово)                            На вход получаем две строки, которые склеиваим не забыв в конец первой добавить знак +.
# (готово)                            Нарезаем объединенную строку на трех элементные кортежи.(1 - число, 2 - буква, 3 - степень) Разделитель + и -.
# Сравниваем между собой кортежи, схожие по 2 и 3 складываем. Кортежи с одним 1 элементом складываем.
# Формируем список из кортежей, первый элемен - кортеж с максимальным значением степени (3й элемен) и по убыванию.

import inOutData


def InterpolationString(firstLine, secondLine):
    result = f'{firstLine}+{secondLine}'
    return result    


def SlicingString(text):
    index1 = 0
    index2 = 0

    list = []
    for i in text:
        if i == '+':
            list.append(text[index1:index2])
            index1 = index2 + 1
        index2 += 1
    list.append(text[index1:index2])

    result = []
    for i in list:
        result.append(SlicingNumber(i))

    return result 


def SlicingNumber(text):
    tuple = ([], [], [])
    temp, temp2 = '', ''
    count = 0

    for i in range(len(text)):
        if text[i].isdigit():
            if count <= 1:
                temp += text[i]
                count = 0

            if count > 1: temp2 += text[i]

        if not text[i].isdigit() and text[i] != '*':
            tuple[1].append(text[i])    
        count += 1

    if temp == '': tuple[0].append(1)
    else: tuple[0].append(int(temp))

    if temp2 == '': None
    else: tuple[2].append(int(temp2))    

    return tuple


list = [([2], ['x'], [2]), ([4], ['x'], []), ([5], [], []), ([1], ['x'], [2]), ([5], [], [])]
list2 = []

for i in range(len(list)):
    for j in range(1, len(list)-1):
        if list[i][1] == list[j][1] and list[i][2] == list[j][2]:
            list2.append((sum(list[i][0] + list[j][0]), list[i][1], list[i][2]))
print(list2)

# Не доделал.