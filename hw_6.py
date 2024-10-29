def  binary_search(list, value):
    n = len(list)
    ResultOk = False
    first = 0
    last = n - 1
    pos = None

    while first < last:
        middle = (first + last) // 2
        if value == list[middle]:
            first = middle
            last = first
            ResultOk = True
            pos = middle
        else:
            if value > list[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if ResultOk == True:
        print('Элемент найден')
        return pos


    else:
        print('Элемент не найден')


index = binary_search([15,24,46,68,85], 68)
print(f'Индекс искаемого элемента {index}!')


b = [23,54,12,65,78,21,3,46,34]

def buble_sort(arb):
    iter = len(arb) - 1
    for i in range(iter):
        for j in range(iter - i):
            if arb[j] > arb[j+1]:
                arb[j], arb[j+1] = arb[j+1], arb[j]

print(b)
buble_sort(b)
print(b)