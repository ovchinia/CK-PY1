from random import randint

def get_unique_list_numbers(start_ = -10, stop_ = 10, range_ = 15) -> list[int]:
    while True:
        r_un = [randint(start_, stop_) for _ in range(range_)]
        if len(r_un) == len(set(r_un)):
            return r_un
        else:
            continue


#def get_unique_list_numbers(start_ = -10, stop_ = 10) -> list[int]:
#    from random import randint
#    list_ = []
#   while True:
#       r_un = [randint(start_, stop_)]
#      if len(list_) == 15:
#          return list_
#       else:
#           if str(r_un) in list_:
#                continue
#           else:
#               list_.append(str(r_un))

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
