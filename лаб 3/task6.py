list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ = list_numbers[0]
a = 0

for pos, value in enumerate(list_numbers):
    if value >= max_:
        max_ = value
        a = pos
list_numbers[-1], list_numbers[a] = list_numbers[a], list_numbers[-1]
max_, list_numbers[-1] = list_numbers[-1], max_
# TODO Оформить решение
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
