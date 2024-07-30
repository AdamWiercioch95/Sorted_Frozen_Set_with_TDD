# def gen():
#     print(1)
#     yield 10
#     print(2)
#     yield 20
#     print(3)
#
#
# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))


# uuid - universal unique id
def uuid(id_=1):
    while True:
        yield id_
        id_ += 1
        if id_ > 5:
            return 42


u = uuid()
print(next(u))
print(next(u))
print(next(u))
print(next(u))
print(next(u))
print(next(u))
