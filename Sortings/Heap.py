# coding=utf-8
import random


def get_left_child_index(parent_index):
    return parent_index * 2 + 1


def get_right_child_index(parent_index):
    return parent_index * 2 + 2


def get_parent_index(child_index):
    if child_index == 0:
        return 0
    return (child_index - 1) / 2


class Heap:
    def __init__(self):
        self.heap = []
        i = 0
        while i < 20:
            self.heap.append(random.randint(0, 100))
            i += 1

        # i = 0
        # while i < 20:
        #     self.add_element(random.randint(0, 100))
        #     i += 1

    def add_element(self, element):
        self.heap.append(element)
        element_index = len(self.heap) - 1

        while True:
            parent_index = get_parent_index(element_index)
            if element > self.heap[parent_index]:
                self.heap[parent_index], self.heap[element_index] \
                    = self.heap[element_index], self.heap[parent_index]

                element_index = parent_index
            else:
                return

    def remove_root(self):
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        p = 0

        while True:
            left = get_left_child_index(p)
            right = get_right_child_index(p)

            if left < len(self.heap):
                child = left
            else:
                return

            if right < len(self.heap) and self.heap[left] < self.heap[right]:
                child = right

            if self.heap[p] < self.heap[child]:
                self.heap[p], self.heap[child] = self.heap[child], self.heap[p]
                p = child

            else:
                return

    def print_heap(self):
        print
        print self.heap

        last_index_in_level = 0
        for index, e in enumerate(self.heap):
            if index < last_index_in_level:
                # stay on the same line
                print e,
            else:
                # print last element of the line and go to next line
                print e

                # calculate last element index in next line
                # this is a right child of the last element in this line
                last_index_in_level = get_right_child_index(last_index_in_level)

    # def validate_if_list_is_heap(self):
    #     for i, item in reversed(list(enumerate(self.heap))):
    #         if item > self.heap[get_parent_index(i)]:
    #             return False
    #         print item
    #     return True

    def validate_that_list_is_heap(self):
        i = len(self.heap) - 1

        while i >= 0:
            if self.heap[i] > self.heap[get_parent_index(i)]:
                return False
                # raise Exception("Child", self.heap[i],
                # "exceeds its parent", self.heap[get_parent_index(i)])
            i -= 1

        return True

    def heap_sort(self):
        """
        while end > 0 do
            (a[0] is the root and largest value. The swap moves it in front of the sorted elements.)
            swap(a[end], a[0])
            (the heap size is reduced by one)
            end ← end - 1
            (the swap ruined the heap property, so restore it)
            siftDown(a, 0, end)
        """

        self.heapify()
        end = len(self.heap)

        while end > 0:
            self.heap[end - 1], self.heap[0] = self.heap[0], self.heap[end - 1]
            end -= 1
            self.sift_down(0, end)

    def heapify(self):
        """
        (start is assigned the index in 'a' of the last parent node)
        (the last element in a 0-based array is at index count-1; find the parent of that element)
        start ← floor ((count - 2) / 2)

    while start ≥ 0 do
        (sift down the node at index 'start' to the proper place such that all nodes below
         the start index are in heap order)
        siftDown(a, start, count - 1)
        (go to the next parent node)
        start ← start - 1
        (after sifting down the root all nodes/elements are in heap order)
        """
        parent_idx = get_parent_index(len(self.heap) - 1)

        while parent_idx >= 0:
            self.sift_down(parent_idx,len(self.heap))
            parent_idx -= 1

    def sift_down(self, start, end):
        """
        siftDown(a, start, end) is
            root ← start

            while root * 2 + 1 ≤ end do    (While the root has at least one child)
                child ← root * 2 + 1       (Left child)
                swap ← root                (Keeps track of child to swap with)

                if a[swap] < a[child]
                    swap ← child
                (If there is a right child and that child is greater)
                if child+1 ≤ end and a[swap] < a[child+1]
                    swap ← child + 1
                if swap = root
                    (The root holds the largest element. Since we assume the heaps rooted at the
                     children are valid, this means that we are done.)
                    return
                else
                    swap(a[root], a[swap])
                    root ← swap            (repeat to continue sifting down the child now)

        """
        parent_idx = start

        while get_left_child_index(parent_idx) < end:
            left_child_idx = get_left_child_index(parent_idx)
            max_value_idx = parent_idx

            if self.heap[max_value_idx] < self.heap[left_child_idx]:
                max_value_idx = left_child_idx

            if left_child_idx + 1 < end and self.heap[max_value_idx] < self.heap[left_child_idx + 1]:
                max_value_idx = left_child_idx + 1

            if max_value_idx == parent_idx:
                return

            else:
                self.heap[parent_idx], self.heap[max_value_idx] = \
                    self.heap[max_value_idx], self.heap[parent_idx]

                parent_idx = max_value_idx


new_heap = Heap()
new_heap.print_heap()
print new_heap.validate_that_list_is_heap()
print
new_heap.heap_sort()
print new_heap.heap
print new_heap.validate_that_list_is_heap()

