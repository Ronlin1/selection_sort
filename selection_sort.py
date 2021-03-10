# Selection Sort
def selection_sort(any_list):
    # we assume that i is sorted -> the first element
    """
    For More about how this algorithm works, kindly read the README file! Thanks!
    :param any_list:
    :return: sorted-list
    """
    for i in range(len(any_list)):
        smallest_num = i
        # now starting from i, we iterate over the next elements
        for j in range(i + 1, len(any_list)):
            # if we find a smaller value than i, we swap
            if any_list[j] < any_list[smallest_num]:
                smallest_num = j
        any_list[i], any_list[smallest_num] = any_list[smallest_num], any_list[i]
    return any_list


# Testing and calling out the function
call_list = [123, 4, 67, 8, 9, 234, 67, 2, 40, 78, 5, 17]
print(f'My Unsorted List --> {call_list}')
call_1 = selection_sort(call_list)
print(f'My Selection Sorted list --> {call_1}')
