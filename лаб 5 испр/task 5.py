from random import sample
from string import ascii_lowercase, ascii_uppercase, digits

def get_random_password(i) -> str:
    str_ = (ascii_uppercase + ascii_lowercase + digits)
    pas_str = sample(str_, i)
    password = "".join(pas_str)
    return password

print(get_random_password(8))
print(get_random_password(9))
