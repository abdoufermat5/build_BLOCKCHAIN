def unlimited_args(*args):
    print(args)
    for i in args:
        print(i)


def another_unpack(args):
    print('{} ha {} ha {}'.format(*args))

if __name__ == '__main__':
    unlimited_args(1, 2, 3, 4, 5)
    # unpack list
    unlimited_args(*[1, 2, 3, 4])
    another_unpack([1, 2, 3, 6])