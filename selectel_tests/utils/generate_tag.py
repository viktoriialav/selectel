from random import randint


def random_tag():
    random_len = randint(5, 64)
    tag = ''
    for i in range(random_len):
        num = randint(0, 25)
        tag += chr(ord('a') + num)
    return tag
