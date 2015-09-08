__author__ = 'korol'


def validation(data, parameter, value):
        if value.__contains__(str(parameter)):
            return value


def find(data, parameter):
    """
    For example:
    given list = [1, 3, 2, 4, 5, 67, 8, 8, 68]
    what_to_find = 8
    :return:
    A list of indexes where you meet 8: [7, 8]

    https://en.wikipedia.org/wiki/Search_algorithm
    """
    found_value_indexes = []
    for i, el in enumerate(data):
        element = str(el)
        if validation(data, parameter, element):
            found_value_indexes.append(i)

    return found_value_indexes


a = [1, 3, 2, 4, 5, 67, 8, 8, 68]
print find(a, 8)

# brute_force_search():
#   first(P)
#      while' c is not None:
#         if' valid(P,c) then output(P, c)
#         next(P,c):
#           returns c
#      end while
#returns results set


def eight_queen_puzzle():
    pass
