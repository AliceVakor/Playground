__author__ = 'korol'
import unittest

from Heap import Heap


class MyTestCase(unittest.TestCase):

    def test__validate_that_list_is_heap(self):
        """
        Scenario:
        1. Create an object of Heap class
        2. Initialize the heap by the list with partially ordered elements according to max heap concept:
            https://en.wikipedia.org/wiki/Binary_heap#Heap_implementation
        3. Call validate_that_list_is_heap()

        Expected result: The list validated as heap
        """
        new_heap = Heap()
        new_heap.heap = [100, 92, 82, 48, 86, 52, 71, 44, 37, 50, 42, 13, 21, 1, 44, 25, 3, 5, 6, 8]

        actual_result = new_heap.validate_that_list_is_heap()

        self.assertEqual(True, actual_result)

    def test__validate_that_list_is_heap__if_child_exceeds_parent__returns_False(self):
        """
        Scenario:
        1. Create an object of Heap class
        2. Initialize the heap by the list with INCORRECT placed first element according to max heap concept:
        https://en.wikipedia.org/wiki/Binary_heap#Heap_implementation
        3. Call validate_that_list_is_heap()

        Expected result: The list validated as NOT heap
        """
        new_heap = Heap()
        new_heap.heap = [91, 92, 82, 48, 86, 52, 71, 44, 37, 50, 42, 13, 21, 1, 44, 25, 3, 5, 6, 8]

        actual_result = new_heap.validate_that_list_is_heap()

        self.assertEqual(False, actual_result)


        # with self.assertRaises(Exception) as actual:
        #     new_heap.validate_that_list_is_heap()
        #
        # self.assertEqual("Child exceeds its parent", actual.exception.message)

if __name__ == '__main__':
    unittest.main()