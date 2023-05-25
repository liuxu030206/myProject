# Import the library
import math


# function
def get_round():
    pi = 3.1415926
    print("pi:", pi)
    # Round up
    print("round up:", math.ceil(pi))
    # Round down
    print("round down:", math.floor(pi))
    # Round
    print("round:", round(pi))
    # Take a few digits approximately
    print("round to 3:", round(pi, 3))

    # defined list
    lst = [2, 34, 6, 23, 45, 100]
    print("list:", lst)
    # max
    print("max:", max(lst))
    # min
    print("min:", min(lst))


if __name__ == '__main__':
    get_round()
