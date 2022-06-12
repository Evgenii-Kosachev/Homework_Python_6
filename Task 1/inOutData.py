def WriteData(line):
    with open('Task 1/Data/result_polynomial.txt', 'w') as data:
        data.write(f'{line}\n')


def ReadData(direction):
    result = ''

    path = direction
    data = open(path, 'r')
    for i in data:
        result += i
    data.close()

    return result