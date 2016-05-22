import random

from bson import ObjectId


class CreateId:
    def __init__(self):
        pass

    @staticmethod
    def create_int():
        return str(random.randint(100000000000, 999999999999) * random.randrange(100000, 999999))

    @staticmethod
    def create_int_small():
        return random.randint(100000, 999999)

    @staticmethod
    def create_object_id():
        return str(ObjectId())

    @staticmethod
    def create_password():
        a = ['a', 'b', '9', 'C', '6', 'D', 'e', '5', 'd', 'F', '3', 'm', 'G', 'h', '8', 'p', 'J', '1', 'k',
             '4', 'L', 'M', 'n', 'A', '2', 'P', 'c', 'E', 'z', '7', 'I']
        __pass = ''
        for i in range(0, 11):
            __pass += str(a[random.randint(0, len(a) - 1)])
        return __pass
