def get_parent_classes(cls):
    if cls.__bases__:
        parents = list(cls.__bases__)
        for base in cls.__bases__:
            parents.extend(get_parent_classes(base))
        return parents
    return []


class A:
    pass

class B(A):
    pass

class C(B):
    pass


# print(get_parent_classes(C))
# print(get_parent_classes(object))

import sys

if sys.maxunicode == 0xffff:
    print("Python is using UTF-16 for internal Unicode representation.")
else:
    print("Python is using UTF-32 for internal Unicode representation.")

class B:
    def __init__(self):
        pass

    def check_something(self, i:int):
        if i > 10:
            raise Exception('exception B')

class A:
    def __init__(self, i1:int, i2: int):
        self.list_i = [i1, i2]

    def get_something(self, b:B):
        for i in  self.list_i:
            b.check_something(i)

        return self.list_i

class Main:
    b: B = B()
    list_a: A = [A(1), A(2)]
    for a in list_a:
        print(a.get_something(b))

I need to get list of error masseges from "raise Exception('exception B')" in class Main to add the message to log.
Please list all possible options to implement it.  "raise Exception('exception B')" can be changed to "return error" if it is required