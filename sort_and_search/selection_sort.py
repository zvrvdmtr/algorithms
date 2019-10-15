# Simple selection sort

def selection_sort(data):
    for i in range(len(data)-1, 0, -1):
        max = 0
        for j in range(i+1):
            if data[j] > data[max]:
                max = j

        x = data[i]
        data[i] = data[max]
        data[max] = x


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(alist)

