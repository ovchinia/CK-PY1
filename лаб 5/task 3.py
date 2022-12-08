def get_unique_list_numbers() -> list[int]:
    import random
    while True:
        r_un = [random.randint(-10, 10) for _ in range(15)]
        if len(r_un) == len(set(r_un)):
            return r_un
        else:
            continue


#def get_unique_list_numbers() -> list[int]:
#    import random
#    list_ = []
#   while True:
#       r_un = [random.randint(-10, 10)]
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
