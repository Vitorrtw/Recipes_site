from unittest import TestCase
from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), num_pages=4, current_page=2
        )["pagination"]
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), num_pages=4, current_page=2
        )["pagination"]
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), num_pages=4, current_page=10
        )["pagination"]
        self.assertEqual([9, 10, 11, 12], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), num_pages=4, current_page=18
        )["pagination"]
        self.assertEqual([17, 18, 19, 20], pagination)
