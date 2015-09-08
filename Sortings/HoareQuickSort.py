__author__ = 'korol'

# quicksort(A, lo, hi)
#   if lo < hi
#     p = partition(A, lo, hi)
#     quicksort(A, lo, p)
#     quicksort(A, p + 1, hi)
#
# partition(A, lo, hi)
#     pivot = A[lo]
#     i = lo - 1
#     j = hi + 1
#     while True
#         do
#             j = j - 1
#         while A[j] > pivot
#         do
#             i = i + 1
#         while A[i] < pivot
#         if i < j
#             swap A[i] with A[j]
#         else
#             return j


def quick_sort_hoare(the_list, first_idx, last_idx):

    if first_idx < last_idx:
        p = partitioning(the_list, first_idx, last_idx)
        quick_sort_hoare(the_list, first_idx, p)
        quick_sort_hoare(the_list, p + 1, last_idx)


def partitioning(the_list, first_idx, last_idx):
    pivot = the_list[first_idx]
    i = first_idx - 1
    j = last_idx + 1

    while True:

        j -= 1
        while the_list[j] > pivot:
            j -= 1

        i += 1
        while the_list[i] < pivot:
            i += 1

        if i < j:
            the_list[i], the_list[j] = the_list[j], the_list[i]
        else:
            return j

# a = [5, 4, 7, 2, 3, 10, 8, 6, 0, 1, 9, 2, 10, 3]
#
# quick_sort_hoare(a, 0, len(a) - 1)
# print a