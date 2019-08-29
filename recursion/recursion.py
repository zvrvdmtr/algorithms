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