from random import randint

def get_unique_list_numbers(start_ = -10, stop_ = 10, range_ = 15) -> list[int]:
    list_ = []
    while True:
        r_un = randint(start_, stop_)
        if len(list_) == range_:
            return list_
        else:
            if r_un in list_:
                continue
            else:
               list_.append(r_un)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
