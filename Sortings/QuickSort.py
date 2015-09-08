__author__ = 'korol'

# quicksort(A, lo, hi)
#   if lo < hi
#     p = partition(A, lo, hi)
#     quicksort(A, lo, p - 1)
#     quicksort(A, p + 1, hi)
#
# partition(A, lo, hi)
#     pivot = A[hi]
#     i = lo //place for swapping
#     for j = lo to hi - 1
#         if A[j] <= pivot
#             swap A[i] with A[j]
#             i = i + 1
#     swap A[i] with A[hi]
#     return i


def quick_sort(my_list, first_el_idx, last_el_idx):

    if first_el_idx < last_el_idx:

        p = partition(my_list, first_el_idx, last_el_idx)
        quick_sort(my_list, first_el_idx, p - 1)
        quick_sort(my_list, p + 1, last_el_idx)


def partition(my_list, first_idx, last_idx):
    pivot = my_list[last_idx]

    i, j = first_idx, first_idx

    while j < last_idx:
        if my_list[j] <= pivot:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            i += 1
        j += 1

    my_list[i], my_list[last_idx] = my_list[last_idx], my_list[i]
    return i