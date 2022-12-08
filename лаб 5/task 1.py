import pprint
list_ = []
for i in range(16):
    str_hex = str(hex(i)) # TODO решить с помощью list comprehension и распечатать его
    str_bin = str(bin(i))
    str_oct = str(oct(i))
    list_.append({"bin": str_bin, "dec": i, "hex": str_hex, "oct": str_oct})
pprint.pp(list_)