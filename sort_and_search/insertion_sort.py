def insertion_sort(data: list):
    if len(data) < 2:
        return data

    for i in range(1, len(data)):
        current_value = data[i]
        position = i

        while position > 0 and data[position-1] > current_value:
            data[position] = data[position-1]
            position = position-1

        data[position] = current_value


unsorted_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(unsorted_list)
print(unsorted_list)
