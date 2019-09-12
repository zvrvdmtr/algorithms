from basic.stack.stack import Stack


# Simple recursion func which count sum of numbers
def list_sum(num):
    if len(num) == 1:
        return num[0]
    else:
        return num[0] + list_sum(num[1:])


print(list_sum([1, 3, 5, 7, 9]))


# Simple number converter to any base
def to_str(n, base):
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base, base) + convert_string[n % base]


print(to_str(1453, 16))


recs = Stack()


def to_str_s(n, base):
    convert_string = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            recs.push(convert_string[n])
        else:
            recs.push(convert_string[n%base])

        n = n // base

    result = ""
    while not recs.isEmpty():
        result = result + str(recs.pop())

    return result

print(to_str_s(1453, 16))
