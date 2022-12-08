import random
import string
str_ = (string.ascii_uppercase + string.ascii_lowercase + string.digits)
def get_random_password() -> str:
    pas_str = random.sample(str_, 8)
    password = "".join(pas_str)
    return password
print(get_random_password())
