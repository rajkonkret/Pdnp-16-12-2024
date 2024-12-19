def connect(**opcje):  # dowolna ilosc argumentów przekazanych po nazwie
    print(opcje)


connect(a=10)  # {'a': 10}
connect(a=10, b=9, name="Radek")  # {'a': 10, 'b': 9, 'name': 'Radek'}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args(1, 2, 3)
all_args(a=8, b=8, c=90, name="Radek")  # () {'a': 8, 'b': 8, 'c': 90, 'name': 'Radek'}
all_args(1, 2, a=10)  # (1, 2) {'a': 10}
all_args()  # () {}
