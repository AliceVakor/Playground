__author__ = 'Varvara'


import time
import unittest

from SortingStudy import Sortings


class SortingsLoadTests(unittest.TestCase):

    def test_sort_asc_bubble__load_test(self):
        """
        Expected result: Timing is not exceeding following numbers
        # 0 2.14576721191e-06
        # 1000 0.306516885757
        # 2000 1.18236112595
        # 3000 2.68166708946
        # 4000 4.75515794754
        # 5000 7.46735286713
        # 6000 10.7233338356
        # 7000 14.4423561096
        # 8000 18.9818980694
        # 9000 23.9862349033
        """
        i = 1
        while i < 10000:
            sortings = Sortings(i)

            start = time.time()
            sortings.sort_asc_bubble()
            end = time.time()
            print i, end - start

            i += 1000

    def test_sort_desc_bubble_load_test(self):
        """

        Expected result: The timing should not exceed following numbers:
        1 4.05311584473e-06
        1001 0.4536049366
        2001 1.79013895988
        3001 3.99529099464
        4001 7.08103489876
        5001 11.0427498817
        6001 15.9283699989
        7001 21.6802170277
        8001 28.3089148998
        9001 35.8479449749
        """
        i = 1
        while i < 10000:
            sortings = Sortings(i)

            start = time.time()
            sortings.sort_desc_bubble()
            end = time.time()
            print i, end - start

            i += 1000

    def test_sort_asc_heap_sort_load_test(self):

        i = 1
        while i < 10000:
            sortings = Sortings(i)

            start = time.time()
            sortings.sort_asc_heap_sort()
            end = time.time()
            print i, end - start

            i += 1000

    def test_sort_asc_quick_sort_load_test(self):
        """
        1 3.09944152832e-06
        1001 0.00337600708008
        2001 0.00739789009094
        3001 0.012197971344
        4001 0.0165600776672
        5001 0.0213091373444
        6001 0.0295732021332
        7001 0.0387279987335
        8001 0.0396621227264
        9001 0.0489349365234
        """
        i = 1
        while i < 100000:
            sortings = Sortings(i)

            start = time.time()
            sortings.sort_asc_quick_sort()
            end = time.time()
            print i, end - start

            i += 10000

    def test_sort_asc_quick_sort_hoare(self):
        sortings = Sortings(100)
        # sortings.list = [5, 4, 7, 2, 3, 10, 8, 6, 0, 1, 9, 2, 10, 3]
        print sortings.sort_asc_hoare_quick_sort()

    def test_sort_asc_quick_sort_hoare_load_test(self):
        """
        1 3.09944152832e-06
        1001 0.00337600708008
        2001 0.00739789009094
        3001 0.012197971344
        4001 0.0165600776672
        5001 0.0213091373444
        6001 0.0295732021332
        7001 0.0387279987335
        8001 0.0396621227264
        9001 0.0489349365234
        """
        i = 1
        while i < 10000000:
            sortings = Sortings(i)

            start = time.time()
            sortings.sort_asc_hoare_quick_sort()
            end = time.time()
            print i, end - start

            i += 1000000


if __name__ == '__main__':
    unittest.main()