from random import randint


def create_random_order_id():
    word = "oreder-{}"
    value = randint(1000, 1000000)
    return word.format(value)

