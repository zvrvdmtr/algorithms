# Simple merge sort with recursion


def merge_sort(data):
    # Split data list until we get one element list
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        # Compare items from left and right half and add it to the main list
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i = i + 1
            else:
                data[k] = right_half[j]
                j = j + 1

            k = k + 1

        # If right half is empty add all from left half to the list
        while i < len(left_half):
            data[k] = left_half[i]
            i = i + 1
            k = k + 1

        # If left half is empty add all from right half to the list
        while j < len(right_half):
            data[k] = right_half[j]
            j = j + 1
            k = k + 1


unsorted_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(unsorted_list)
