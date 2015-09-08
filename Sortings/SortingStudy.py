__author__ = 'korol'

import random
import types
import Heap
from QuickSort import quick_sort
from HoareQuickSort import quick_sort_hoare


class Sortings:

    def __init__(self, list_size=5):
        self.list = []

        i = 0
        while i < list_size:
            self.list.append(random.randint(0, 100))
            i += 1

    def find_minimum(self):

        if not isinstance(self.list, types.ListType) and self.list is not None:
            raise Exception("Can not find min_val for object of type not 'list'")

        if self.list is None:
            raise Exception("Can not find min_val in a list 'None'")

        if len(self.list) == 0:
            raise Exception("Can not find min_val in an empty list")

        for element in self.list:
            if not isinstance(element, (int, long, float)):
                raise Exception("An input list should contain only numeric values")

        min_val = self.list[0]
        i = 1
        while i < len(self.list):
            if min_val > self.list[i]:
                min_val = self.list[i]
            i += 1

        return min_val

    def find_maximum(self):

        if not isinstance(self.list, types.ListType) and self.list is not None:
            raise Exception("Can not find maximum for object of type not 'list'")

        if self.list is None:
            raise Exception("Can not find maximum in a list 'None'")

        if len(self.list) == 0:
            raise Exception("Can not find maximum in an empty list")

        for element in self.list:
            if not isinstance(element, (int, long, float)):
                raise Exception("An input list should contain only numeric values")

        max_val = self.list[0]
        i = 1
        while i < len(self.list):
            if max_val < self.list[i]:
                max_val = self.list[i]
            i += 1
        return max_val

    def calculate_total(self):

        if not isinstance(self.list, types.ListType) and self.list is not None:
            raise Exception("Can not calculate total for object of type not 'list'")

        if self.list is None:
            raise Exception("Can not calculate total of a list 'None'")

        if len(self.list) == 0:
            raise Exception("Can not calculate total of an empty list")

        for element in self.list:
            if not isinstance(element, (int, long, float)):
                raise Exception("An input list should contain only numeric values")

        i = 0
        total = 0
        while i < len(self.list):
            total += self.list[i]
            i += 1
        return total

    def calculate_total_product(self):

        if not isinstance(self.list, types.ListType) and self.list is not None:
            raise Exception("Can not calculate total product for object of type not 'list'")

        if self.list is None:
            raise Exception("Can not calculate total product of a list 'None'")

        if len(self.list) == 0:
            raise Exception("Can not calculate total product of an empty list")

        for element in self.list:
            if not isinstance(element, (int, long, float)):
                raise Exception("An input list should contain only numeric values")

        i = 0
        total_product = 1
        while i < len(self.list):
            total_product *= self.list[i]
            i += 1
        return total_product

    def sort_asc_selection_sort(self):
        """
        https://en.wikipedia.org/wiki/Selection_sort
        :return:
        """
        if not isinstance(self.list, types.ListType) and self.list is not None:
            raise Exception("Can not perform sort asc for object of type not 'list'")

        if self.list is None:
            raise Exception("Can not perform sort asc of a list 'None'")

        if len(self.list) == 0:
            raise Exception("Can not perform sort asc of an empty list")

        for element in self.list:
            if not isinstance(element, (int, long, float)):
                raise Exception("An input list should contain only numeric values")

        i, j, min_val_idx = 0, 0, 0

        while i < len(self.list):
            while j < len(self.list):
                if self.list[min_val_idx] > self.list[j]:
                    min_val_idx = j
                j += 1
            temp = self.list[i]
            self.list[i] = self.list[min_val_idx]
            self.list[min_val_idx] = temp

            i += 1
            j = i
            min_val_idx = j
        return self.list

    def sort_asc_bubble(self):

        if not isinstance(self.list, types.ListType) and self.list is not None:
            raise Exception("Can not perform sort asc for object of type not 'list'")

        if self.list is None:
            raise Exception("Can not perform sort asc of a list 'None'")

        if len(self.list) == 0:
            raise Exception("Can not perform sort asc of an empty list")

        for element in self.list:
            if not isinstance(element, (int, long, float)):
                raise Exception("An input list should contain only numeric values")

        i = 0
        while i < len(self.list):
            j = 0
            while j < len(self.list) - 1 - i:
                if self.list[j] > self.list[j + 1]:
                    temp = self.list[j]
                    self.list[j] = self.list[j + 1]
                    self.list[j + 1] = temp
                j += 1
            i += 1
        return self.list

    def sort_desc_bubble(self):

        if not isinstance(self.list, types.ListType) and self.list is not None:
            raise Exception("Can not perform sort desc for object of type not 'list'")

        if self.list is None:
            raise Exception("Can not perform sort desc of a list 'None'")

        if len(self.list) == 0:
            raise Exception("Can not perform sort desc of an empty list")

        for element in self.list:
            if not isinstance(element, (int, long, float)):
                raise Exception("An input list should contain only numeric values")

        i = 0
        while i < len(self.list):
            j = 0
            while j < len(self.list) - 1:
                if self.list[j] < self.list[j + 1]:
                    temp = self.list[j]
                    self.list[j] = self.list[j + 1]
                    self.list[j + 1] = temp
                j += 1
            i += 1
        return self.list

    def sort_asc_heap_sort(self):
        heap = Heap()
        heap.heap = self.list
        heap.heap_sort()
        return heap.heap

    def sort_asc_quick_sort(self):
        quick_sort(self.list, 0, (len(self.list) - 1))
        return self.list

    def sort_asc_hoare_quick_sort(self):
        quick_sort_hoare(self.list, 0, len(self.list) - 1)
        return self.list