def main():
    ''' 1'''
    q = lambda x: x ** 2
    print(q(2))

    ''' 2 '''
    x = [(1, "one"), (4, "four"), (5, "five"), (3, "three")]
    print(sorted (x, key=lambda x: x[1]))

    ''' 3 '''
    x = list(filter(lambda x: x >= 0, [1, 2, 3, -8, -9]))
    print(x)
main()