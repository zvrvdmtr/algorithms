# Simple implementation for bubble sort


def bubble_sort(data):
    for item in range(len(data)-1):
        for i in range(1, len(data)):
            if data[i-1] > data[i]:
                x = data[i-1]
                data[i-1] = data[i]
                data[i] = x


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(alist)
