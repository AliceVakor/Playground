__author__ = 'korol'

import time
import unittest

from SortingStudy import Sortings


class MyTestCase(unittest.TestCase):
    def test__find_maximum__if_none__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with None
        3. Call find_maximum()

        Expected result: Exception is thrown
        """

        sortings = Sortings()
        sortings.list = None

        with self.assertRaises(Exception) as actual:
            sortings.find_maximum()

        self.assertEqual("Can not find maximum in a list 'None'", actual.exception.message)

    def test__find_maximum__if_empty_list__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with an empty list
        3. Call find_maximum()

        Expected result: Exception is thrown
        """

        sortings = Sortings()
        sortings.list = []

        with self.assertRaises(Exception) as exc:
            sortings.find_maximum()

        self.assertEqual('Can not find maximum in an empty list', exc.exception.message)

    def test_find_maximum__if_list_of_lists__exception_thrown(self):
        """
        Scenario:
        1. Create object of class Sortings
        2. Initialize list by list of two lists
        3. Call find_maximum()

        Expected result: Exception thrown
        """
        sorting = Sortings()
        sorting.list = [[1, 3, 4, 5, 0], [1, 2, 4, 6, 0, 9]]

        with self.assertRaises(Exception) as actual:
            sorting.find_maximum()

        self.assertEqual("An input list should contain only numeric values", actual.exception.message)

    def test_find_maximum__if_non_list_value__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with float value
        3. Call find_maximum()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = 20.12

        with self.assertRaises(Exception) as actual:
            sortings.find_maximum()

        self.assertEqual("Can not find maximum for object of type not 'list'", actual.exception.message)

    def test__find_maximum__if_one_value__returns_this_value(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with single value
        3. Call find_maximum()

        Expected result: This value is returned
        """
        sortings = Sortings()
        sortings.list = [0]

        actual_result = sortings.find_maximum()

        self.assertEqual(0, actual_result)

    def test__find_maximum__if_all_values_are_identical__returns_one_value(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with equal values
        3. Call find_maximum()

        Expected result: Single initialized value returned
        """
        sortings = Sortings()
        sortings.list = [2, 2, 2, 2, 2, 2]

        actual_result = sortings.find_maximum()

        self.assertEqual(2, actual_result)

    def test__find_maximum__if_negative_values__returns_maximum(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with negative values
        3. Call find_maximum()

        Expected result: Maximum value returned
        """
        sortings = Sortings()
        sortings.list = [-2, 2, -1, 0]

        actual_result = sortings.find_maximum()

        self.assertEqual(2, actual_result)

    def test__find_maximum__if_float_values__returns_maximum(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with float values
        3. Call find_minimum()

        Expected result: The minimal value returned
        """
        sortings = Sortings()
        sortings.list = [0.333, 0, 1 / 3, 1.0 / 3.0]

        actual_result = sortings.find_maximum()

        self.assertEqual(1.0 / 3.0, actual_result)

    def test_find_minimum__returns_minimal(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with positive integers
        3. Call find_minimum()

        Expected result: A correct minimum value returned
        """

        sortings = Sortings()
        sortings.list = [5, 1, 2, 3]

        actual_result = sortings.find_minimum()

        self.assertEqual(1, actual_result)

    def test_find_minimum__two_times__returns_minimal(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with positive integers
        3. Call find_minimum() method
        4. Initialize list with other positive integers
        5. Call find_minimum() method

        Expected result: A correct minimum value returned both times.
        """

        sortings = Sortings()
        sortings.list = [5, 1, 2, 3]

        actual_result = sortings.find_minimum()

        self.assertEqual(1, actual_result)

        sortings.list = [3456, 123, 12, 35]

        actual_result = sortings.find_minimum()

        self.assertEqual(12, actual_result)

    def test_find_minimum__if_empty_list__exception_thrown(self):
        """
        Scenario:
        1. Create object of class Sortings
        2. Initialize list with an empty list
        3. Call find_minimum()

        Expected result: Exception thrown
        """

        sorting = Sortings()
        sorting.list = []

        with self.assertRaises(Exception) as actual:
            sorting.find_minimum()

        self.assertEqual("Can not find min_val in an empty list", actual.exception.message)

    def test_find_minimum__if_None__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with None
        3. Call find_minimum()

        Expected result: Exception is thrown
        """

        sortings = Sortings()
        sortings.list = None

        with self.assertRaises(Exception) as actual:
            sortings.find_minimum()

        self.assertEqual("Can not find min_val in a list 'None'", actual.exception.message)

    def test_find_minimum__if_list_of_lists__exception_thrown(self):
        """
        Scenario:
        1. Create object of class Sortings
        2. Initialize list by list of two lists
        3. Call find_minimum()

        Expected result: Exception thrown
        """
        sorting = Sortings()
        sorting.list = [[1, 3, 4, 5, 0], [1, 2, 4, 6, 0, 9]]

        with self.assertRaises(Exception) as actual:
            sorting.find_minimum()

        self.assertEqual("An input list should contain only numeric values", actual.exception.message)

    def test_find_minimum__if_non_list_value__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with int value
        3. Call find_minimum()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = -20303

        with self.assertRaises(Exception) as actual:
            sortings.find_minimum()

        self.assertEqual("Can not find min_val for object of type not 'list'", actual.exception.message)

    def test_find_minimum__if_one_value__returns_this_value(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with single value
        3. Call find_minimum()

        Expected result: This value is returned
        """

        sortings = Sortings()
        sortings.list = [34566]

        actual_result = sortings.find_minimum()
        self.assertEqual(34566, actual_result)

    def test_find_minimum__if_equal_values__returns_one_value(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with equal values
        3. Call find_minimum()

        Expected result: Single initialized value returned
        """
        sortings = Sortings()
        sortings.list = [2, 2, 2, 2, 2, 2]

        actual_result = sortings.find_minimum()

        self.assertEqual(2, actual_result)

    def test__find_minimum__if_negative_values__returns_minimum(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with negative values
        3. Call find_minimum()

        Expected result: The minimal negative value returned
        """
        sortings = Sortings()
        sortings.list = [-2, 2, -1, 0]

        actual_result = sortings.find_minimum()

        self.assertEqual(-2, actual_result)

    def test__find_minimum__if_float_values__returns_minimum(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with float values
        3. Call find_minimum()

        Expected result: The minimal value returned
        """
        sortings = Sortings()
        sortings.list = [0.333, 0, 1 / 3, 1.0 / 3.0]

        actual_result = sortings.find_minimum()

        self.assertEqual(0, actual_result)

    def test_calculate_total__total_is_calculated(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with int values
        3. Call calculate_total()

        Expected result: Total of int values returned
        """
        sortings = Sortings()
        sortings.list = [20202, 1, 2, 3]

        actual_result = sortings.calculate_total()

        self.assertEqual(20208, actual_result)

    def test_calculate_total__if_None__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with None
        3. Call calculate_total()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = None

        with self.assertRaises(Exception) as actual:
            sortings.calculate_total()

        self.assertEqual("Can not calculate total of a list 'None'", actual.exception.message)

    def test_calculate_total__if_empty_list__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list by empty list
        3. Call calculate_total()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = []

        with self.assertRaises(Exception) as actual:
            sortings.calculate_total()

        self.assertEqual('Can not calculate total of an empty list', actual.exception.message)

    def test_calculate_total__if_list_of_lists_values__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with list of lists
        3. Call calculate_total()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = [[0, 2, 10, 3]]

        with self.assertRaises(Exception) as actual:
            sortings.calculate_total()

        self.assertEqual("An input list should contain only numeric values", actual.exception.message)

    def test_calculate_total__if_non_list_value__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with int value
        3. Call calculate_total()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = -20303

        with self.assertRaises(Exception) as actual:
            sortings.calculate_total()

        self.assertEqual("Can not calculate total for object of type not 'list'", actual.exception.message)

    def test_calculate_total__if_string_values__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with string
        3. Call calculate_total()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = ["Test"]

        with self.assertRaises(Exception) as actual:
            sortings.calculate_total()

        self.assertEqual("An input list should contain only numeric values", actual.exception.message)

    def test_calculate_total__if_one_positive_value__returns_this_value(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with one positive value
        3. Call calculate_total()

        Expected result: This value returned
        """
        sortings = Sortings()
        sortings.list = [10101012]
        actual_result = sortings.calculate_total()
        self.assertEqual(10101012, actual_result)

    def test_calculate_total__if_one_negative_value__returns_this_value(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with one negative value
        3. Call calculate_total()

        Expected result: This value returned
        """
        sortings = Sortings()
        sortings.list = [-33012]
        actual_result = sortings.calculate_total()
        self.assertEqual(-33012, actual_result)

    def test_calculate_total__if_negative_values__returns_total(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with mix of negative and positive values
        3. Call calculate_total()

        Expected result: Correct total returned
        """
        sortings = Sortings()
        sortings.list = [100, -2, -10, -3, 2]

        actual_result = sortings.calculate_total()

        self.assertEqual(87, actual_result)

    def test__calculate_total__if_float_values__returns_total(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with float values and float resulting expressions
        3. Call calculate_total()

        Expected result: Correct total returned
        """
        sortings = Sortings()
        sortings.list = [0.333, 0, 1 / 3, 1.0 / 3.0]

        actual_result = sortings.calculate_total()

        self.assertEqual(0.6663333333333333, actual_result)

    def test_calculate_total_product__returns_total_product(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with int values
        3. Call calculate_total_product()

        Expected result: Correct value of total product returned
        """
        sortings = Sortings()
        sortings.list = [444, 1, 2, 3]

        actual_result = sortings.calculate_total_product()

        self.assertEqual(2664, actual_result)

    def test_calculate_total_product__if_None__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list as None
        3. Call calculate_total_product()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = None

        with self.assertRaises(Exception) as actual:
            sortings.calculate_total_product()

        self.assertEqual("Can not calculate total product of a list 'None'", actual.exception.message)

    def test_calculate_total_product__if_empty_list__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list by empty list
        3. Call calculate_total_product()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = []

        with self.assertRaises(Exception) as actual:
            sortings.calculate_total_product()

        self.assertEqual('Can not calculate total product of an empty list', actual.exception.message)

    def test_calculate_total_product__if_list_of_lists_values__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with list of lists
        3. Call calculate_total_product()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = [[-100, -2, 10, -3, 2]]

        with self.assertRaises(Exception) as actual:
            sortings.calculate_total_product()

        self.assertEqual("An input list should contain only numeric values", actual.exception.message)

    def test_calculate_total_product__if_non_list_value__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with int value
        3. Call calculate_total_product()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = 165

        with self.assertRaises(Exception) as actual:
            sortings.calculate_total_product()

        self.assertEqual("Can not calculate total product for object of type not 'list'", actual.exception.message)

    def test_calculate_total_product__if_one_positive_value__returns_this_value(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with one positive value
        3. Call calculate_total_product()

        Expected result: This value returned
        """
        sortings = Sortings()
        sortings.list = [11]
        actual_result = sortings.calculate_total_product()
        self.assertEqual(11, actual_result)

    def test_calculate_total_product__if_negative_and_positive_values__returns_product(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with mix of negative and positive values
        3. Call calculate_total_product()

        Expected result: Correct total returned
        """
        sortings = Sortings()
        sortings.list = [100, -2, -10, -3, 2]

        actual_result = sortings.calculate_total_product()

        self.assertEqual(-12000, actual_result)

    def test_calculate_total_product__if_3_negative_values__returns_negative_product(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with mix of negative and positive values
        3. Call calculate_total_product()

        Expected result: Correct total returned
        """
        sortings = Sortings()
        sortings.list = [-2, -10, -3]

        actual_result = sortings.calculate_total_product()

        self.assertEqual(-60, actual_result)

    def test_calculate_total_product__if_0_among_values__returns_0(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with positive values and 0
        3. Call calculate_total_product()

        Expected result: 0 returned
        """
        sortings = Sortings()
        sortings.list = [2, 10, 3, 0]

        actual_result = sortings.calculate_total_product()

        self.assertEqual(0, actual_result)

    def test_sort_asc_selection_sort__if_None__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list as None
        3. Call sort_asc_selection_sort()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = None

        with self.assertRaises(Exception) as actual:
            sortings.sort_asc_selection_sort()

        self.assertEqual("Can not perform sort asc of a list 'None'", actual.exception.message)

    def test_sort_asc_selection_sort__if_empty_list__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list by empty list
        3. Call sort_asc_selection_sort()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = []

        with self.assertRaises(Exception) as actual:
            sortings.sort_asc_selection_sort()

        self.assertEqual("Can not perform sort asc of an empty list", actual.exception.message)

    def test_sort_asc_selection_sort__if_list_of_lists_values__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with list of lists
        3. Call sort_asc_selection_sort()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = [[2]]

        with self.assertRaises(Exception) as actual:
            sortings.sort_asc_selection_sort()

        self.assertEqual("An input list should contain only numeric values", actual.exception.message)

    def test_sort_asc_selection_sort__if_non_list_value__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with int value
        3. Call sort_asc_selection_sort()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = 165

        with self.assertRaises(Exception) as actual:
            sortings.sort_asc_selection_sort()

        self.assertEqual("Can not perform sort asc for object of type not 'list'", actual.exception.message)

    def test_sort_asc_selection_sort__if_non_negative_values__returns_list_sorted_asc(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with non_negative int values
        3. Call sort_asc_selection_sort()

        Expected result: This list sorted asc returned
        """
        sortings = Sortings()
        sortings.list = [5098, 6000, 564, 324, 0, 13, 28, 45, 1]

        actual_result = sortings.sort_asc_selection_sort()

        self.assertEqual([0, 1, 13, 28, 45, 324, 564, 5098, 6000], actual_result)

    def test_sort_asc_selection_sort__if_negative_values__returns_list_sorted_asc(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with negative int values
        3. Call sort_asc_selection_sort()

        Expected result: This list sorted asc returned
        """
        sortings = Sortings()
        sortings.list = [-5098, -6000, -564, -324, -13, -28, -45, -1]

        actual_result = sortings.sort_asc_selection_sort()

        self.assertEqual([-6000, -5098, -564, -324, -45, -28, -13, -1], actual_result)

    def test_sort_asc_selection_sort__if_mixed_int_values__returns_list_sorted_asc(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with mix of negative and non-negative int values
        3. Call sort_asc_selection_sort()

        Expected result: This list sorted asc returned
        """
        sortings = Sortings()
        sortings.list = [-1, -600, 564, -3224, 333, -208, 34, 1, 0]

        actual_result = sortings.sort_asc_selection_sort()

        self.assertEqual([-3224, -600, -208, -1, 0, 1, 34, 333, 564], actual_result)

    def test_sort_asc_selection_sort__if_equal_values__returns_this_list(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with equal values
        3. Call sort_asc_selection_sort()

        Expected result: Same list returned
        """
        sortings = Sortings()
        sortings.list = [2, 2, 2, 2, 2, 2]

        actual_result = sortings.sort_asc_selection_sort()

        self.assertEqual([2, 2, 2, 2, 2, 2], actual_result)

    def test_sort_asc_selection_sort__if_mixed_types_values__returns_list_sorted_asc(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with mix of negative and non-negative int, float, long values
        3. Call sort_asc_selection_sort()

        Expected result: This list sorted asc returned
        """
        sortings = Sortings()
        sortings.list = [-1.0, -600.66, 564, 32.24, 32.3, -208,
                         10002020202020202049485763542514145637473484389, 1, 0]

        actual_result = sortings.sort_asc_selection_sort()

        self.assertEqual([-600.66, -208, -1.0, 0, 1, 32.24, 32.3, 564,
                          10002020202020202049485763542514145637473484389L], actual_result)

    def test_sort_asc_bubble__if_None__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list as None
        3. Call sort_asc_bubble()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = None

        with self.assertRaises(Exception) as actual:
            sortings.sort_asc_bubble()

        self.assertEqual("Can not perform sort asc of a list 'None'", actual.exception.message)

    def test_sort_asc_bubble__if_empty_list__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list by empty list
        3. Call sort_asc_bubble()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = []

        with self.assertRaises(Exception) as actual:
            sortings.sort_asc_bubble()

        self.assertEqual("Can not perform sort asc of an empty list", actual.exception.message)

    def test_sort_asc_bubble__if_list_of_lists_values__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with list of lists
        3. Call sort_asc_bubble()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = [[2]]

        with self.assertRaises(Exception) as actual:
            sortings.sort_asc_bubble()

        self.assertEqual("An input list should contain only numeric values", actual.exception.message)

    def test_sort_asc_bubble__if_non_list_value__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with int value
        3. Call sort_asc_bubble()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = 165

        with self.assertRaises(Exception) as actual:
            sortings.sort_asc_bubble()

        self.assertEqual("Can not perform sort asc for object of type not 'list'", actual.exception.message)

    def test_sort_asc_bubble__if_non_negative_values__returns_list_sorted_asc(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with non_negative int values
        3. Call sort_asc_bubble()

        Expected result: This list sorted asc returned
        """
        sortings = Sortings()
        sortings.list = [5098, 6000, 564, 324, 0, 13, 28, 45, 1]

        actual_result = sortings.sort_asc_bubble()

        self.assertEqual([0, 1, 13, 28, 45, 324, 564, 5098, 6000], actual_result)

    def test_sort_asc_bubble__if_negative_values__returns_list_sorted_asc(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with negative int values
        3. Call sort_asc_bubble()

        Expected result: This list sorted asc returned
        """
        sortings = Sortings()
        sortings.list = [-5098, -6000, -564, -324, -13, -28, -45, -1]

        actual_result = sortings.sort_asc_bubble()

        self.assertEqual([-6000, -5098, -564, -324, -45, -28, -13, -1], actual_result)

    def test_sort_asc_bubble__if_mixed_int_values__returns_list_sorted_asc(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with mix of negative and non-negative int values
        3. Call sort_asc_bubble()

        Expected result: This list sorted asc returned
        """
        sortings = Sortings()
        sortings.list = [-1, -600, 564, -3224, 333, -208, 34, 1, 0]

        actual_result = sortings.sort_asc_bubble()

        self.assertEqual([-3224, -600, -208, -1, 0, 1, 34, 333, 564], actual_result)

    def test_sort_asc_bubble__if_equal_values__returns_this_list(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with equal values
        3. Call sort_asc_v()

        Expected result: Same list returned
        """
        sortings = Sortings()
        sortings.list = [2, 2, 2, 2, 2, 2]

        actual_result = sortings.sort_asc_bubble()

        self.assertEqual([2, 2, 2, 2, 2, 2], actual_result)

    def test_sort_asc_bubble__if_mixed_types_values__returns_list_sorted_asc(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with mix of negative and non-negative int, float, long values
        3. Call sort_asc_bubble()

        Expected result: This list sorted asc returned
        """
        sortings = Sortings()
        sortings.list = [-1.0, -600.66, 564, 32.24, 32.3, -208,
                         10002020202020202049485763542514145637473484389, 1, 0]

        actual_result = sortings.sort_asc_bubble()

        self.assertEqual([-600.66, -208, -1.0, 0, 1, 32.24, 32.3, 564,
                          10002020202020202049485763542514145637473484389L], actual_result)

    def test_sort_desc_bubble__if_None__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list as None
        3. Call sort_desc_bubble()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = None

        with self.assertRaises(Exception) as actual:
            sortings.sort_desc_bubble()

        self.assertEqual("Can not perform sort desc of a list 'None'", actual.exception.message)

    def test_sort_desc_bubble__if_empty_list__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list by empty list
        3. Call sort_desc_bubble()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = []

        with self.assertRaises(Exception) as actual:
            sortings.sort_desc_bubble()

        self.assertEqual("Can not perform sort desc of an empty list", actual.exception.message)

    def test_sort_desc_bubble__if_list_of_lists_values__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with list of lists
        3. Call sort_desc_bubble()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = [[2]]

        with self.assertRaises(Exception) as actual:
            sortings.sort_desc_bubble()

        self.assertEqual("An input list should contain only numeric values", actual.exception.message)

    def test_sort_desc_bubble__if_non_list_value__exception_thrown(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with int value
        3. Call sort_desc_bubble()

        Expected result: Exception thrown
        """
        sortings = Sortings()
        sortings.list = 165

        with self.assertRaises(Exception) as actual:
            sortings.sort_desc_bubble()

        self.assertEqual("Can not perform sort desc for object of type not 'list'", actual.exception.message)

    def test_sort_desc_bubble__if_non_negative_values__returns_list_sorted_desc(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with non_negative int values
        3. Call sort_desc_bubble()

        Expected result: This list sorted desc returned
        """
        sortings = Sortings()
        sortings.list = [5098, 6000, 564, 324, 0, 13, 28, 45, 1]

        actual_result = sortings.sort_desc_bubble()

        self.assertEqual([6000, 5098, 564, 324, 45, 28, 13, 1, 0], actual_result)

    def test_sort_desc_bubble__if_negative_values__returns_list_sorted_desc(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with negative int values
        3. Call sort_desc_bubble()

        Expected result: This list sorted desc returned
        """
        sortings = Sortings()
        sortings.list = [-5098, -6000, -564, -324, -13, -28, -45, -1]

        actual_result = sortings.sort_desc_bubble()

        self.assertEqual([-1, -13, -28, -45, -324, -564, -5098, -6000], actual_result)

    def test_sort_desc_bubble__if_mixed_int_values__returns_list_sorted_desc(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with mix of negative and non-negative int values
        3. Call sort_desc_bubble()

        Expected result: This list sorted desc returned
        """
        sortings = Sortings()
        sortings.list = [-1, -600, 564, -3224, 333, -208, 34, 1, 0]

        actual_result = sortings.sort_desc_bubble()

        self.assertEqual([564, 333, 34, 1, 0, -1, -208, -600, -3224], actual_result)

    def test_sort_desc_bubble__if_equal_values__returns_this_list(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with equal values
        3. Call sort_desc_bubble()

        Expected result: Same list returned
        """
        sortings = Sortings()
        sortings.list = [2, 2, 2, 2, 2, 2]

        actual_result = sortings.sort_desc_bubble()

        self.assertEqual([2, 2, 2, 2, 2, 2], actual_result)

    def test_sort_desc_bubble__if_mixed_types_values__returns_list_sorted_desc(self):
        """
        Scenario:
        1. Create object of Sortings class
        2. Initialize list with mix of negative and non-negative int, float, long values
        3. Call sort_desc_bubble()

        Expected result: This list sorted desc returned
        """
        sortings = Sortings()
        sortings.list = [-1.0, -600.66, 564, 32.24, 32.3, -208,
                         10002020202020202049485763542514145637473484389, 1, 0]

        actual_result = sortings.sort_desc_bubble()

        self.assertEqual([10002020202020202049485763542514145637473484389L,
                          564, 32.3, 32.24, 1, 0, -1.0, -208, -600.66], actual_result)


if __name__ == '__main__':
    unittest.main()
