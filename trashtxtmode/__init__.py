columns = 80
rows = 25


def cls():
    print("\n"*rows)


def hline(thickness):
    if thickness == 0:
        print(" "*columns)
    elif thickness == 1:
        print("-"*columns)
    elif thickness == 2:
        print("="*columns)
    elif thickness == 3:
        print(":"*columns)
    elif thickness == 4:
        print("#"*columns)
    else:
        return Exception


def title(txt):
    print(txt.upper())
    print("~"*len(txt))