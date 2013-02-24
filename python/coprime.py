from sys import argv


def coprime(x):
    lst = [1]
    for i in range(2,x):
        if x%i != 0:
            lst.append(i)
    return lst


if __name__ == "__main__":
    lst = coprime(int(argv[1]))
    print lst
