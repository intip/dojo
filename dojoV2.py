#coding: utf-8

# test first and baby steps dojo

"""
    Calculate prices according with the following:
        1 book type: R$ 28
        2 books with different types: discount 5%
        3 books with different types: discount 10%
        4 books with different types: discount 20%
        5 books with different types: discount 25%
"""

PRICE = round(28, 2)
DISCOUNT = [1, 0.95, 0.9, 0.8, 0.75]

def calc_partial(books):
    quantity = len(books)
    return round(DISCOUNT[quantity - 1] * quantity * PRICE, 2)
    
def make_groups(books):
    unique = []

    while books:
        group = []
        for i in books:
            if i not in group:
                if (len(set(group)) < 4 or len(books) < 6)  or (len(set(books)) > len(set(group)) + 1):
                    group.append(i)
        for i in group:
            books.remove(i)
        unique.append(group)

    return unique


def calc_price(books):
    count = 0
    list_empty = []

    groups = make_groups(books)
    
    #for discount in with_discounts:

    total_price = [calc_partial(i) for i in groups]

    return round(sum(total_price), 2)



# test case
from unittest import TestCase
import unittest

class BasketTest(TestCase):
    
    def test_zero_books(self):
        self.assertEqual(calc_price([]), 0)
    def test_one_book(self):
        self.assertEqual(calc_price([1]), 28)
    def test_two_books(self):
        self.assertEqual(calc_price([1,2]), round((28*2)*0.95, 2))
    def test_three_books(self):
        self.assertEqual(calc_price([1,2,3]), round((28*3)*0.9, 2))
    def test_four_books(self):
        self.assertEquals(calc_price([1,2,3,4]), round((28*4)*0.8, 2))
    def test_five_books(self):
        self.assertEquals(calc_price([1,2,3,4,5]), round((28*5)*0.75, 2))
    def test_same_books(self):
        self.assertEquals(calc_price([1,1]), round((28*2), 2))
    def test_two_books_same_one(self):
        self.assertEquals(calc_price([1,1,2]), round(28*2 * 0.95 + 28, 2))
    def test_two_books_same_two(self):
        self.assertEquals(calc_price([1,1,2,2,3]), round((28 * 3 * 0.9) + (28 * 2 * 0.95), 2))
    def test_rape_world(self):
        self.assertEquals(calc_price([1,1,1,1,1,3,3,5,5,5,5,5,5,5]), round((6 * 28 * 0.9) + (6 * 28 * 0.95) + (2 * 28), 2))
    
    def test_mind_fuck(self):
        self.assertEquals(calc_price([1, 2, 3, 4, 1, 2, 3, 5]),
                          round(4 * 28 * 0.8 * 2, 2))


unittest.main()
