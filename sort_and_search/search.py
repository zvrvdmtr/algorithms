# Simple sequential search for ordered/unordered list
def sequential_search(alist, number):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == number:
            found = True
        else:
            pos = pos + 1

    return found


# testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(sequential_search(testlist, 3))
# print(sequential_search(testlist, 13))


def binary_search(alist, number):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == number:
            found = True

        else:
            if number < alist[midpoint]:
                last = midpoint - 1

            else:
                first = midpoint + 1

    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 2))