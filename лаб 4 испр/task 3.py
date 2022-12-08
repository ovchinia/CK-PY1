def delete(list_, index=None):
    if isinstance(index, int) and index != -1:
        if not index:
            index = 0
            ans = list_[1:]
        elif index > 0:
            ans = list_[0:index] + list_[index + 1:]
        else:
            length = len(list_)
            index1 = length + index
            ans = list_[0:index1] + list_[index1 + 1:]
    else:
        ans = list_[:-1]
    return ans


print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
