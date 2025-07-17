import unittest
from sweet import Sweet
from sweetshop import SweetShop, InsufficientStockError, SweetNotFoundError

class TestSweet(unittest.TestCase):
    def test_create_valid_sweet(self):
        sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20)
        self.assertEqual(sweet.name, "Kaju Katli")
        self.assertEqual(sweet.price, 50.0)
        self.assertEqual(sweet.quantity, 20)

    def test_negative_price_raises_error(self):
        with self.assertRaises(ValueError):
            Sweet(1002, "Barfi", "Milk-Based", -10.0, 10)

    def test_negative_quantity_raises_error(self):
        with self.assertRaises(ValueError):
            Sweet(1003, "Jalebi", "Sugar-Based", 10.0, -5)

class TestSweetShop(unittest.TestCase):
    def setUp(self):
        self.shop = SweetShop()

    def test_add_sweet(self):
        sweet = self.shop.add_sweet("Ladoo", "Nut-Based", 20.0, 30)
        self.assertEqual(sweet.name, "Ladoo")
        self.assertEqual(sweet.id, 1001)

    def test_delete_sweet(self):
        sweet = self.shop.add_sweet("Barfi", "Milk-Based", 25.0, 10)
        self.shop.delete_sweet(sweet.id)
        self.assertEqual(self.shop.get_total_sweets_count(), 0)

    def test_delete_invalid_id(self):
        with self.assertRaises(SweetNotFoundError):
            self.shop.delete_sweet(9999)

    def test_get_sweet(self):
        sweet = self.shop.add_sweet("Jalebi", "Sugar-Based", 15.0, 50)
        found = self.shop.get_sweet(sweet.id)
        self.assertEqual(found, sweet)

    def test_search_by_name(self):
        self.shop.add_sweet("Kaju Katli", "Nut-Based", 50.0, 20)
        results = self.shop.search_by_name("Kaju")
        self.assertEqual(len(results), 1)

    def test_search_by_category(self):
        self.shop.add_sweet("Rasgulla", "Milk-Based", 25.0, 40)
        results = self.shop.search_by_category("Milk-Based")
        self.assertEqual(len(results), 1)

    def test_search_by_price_range(self):
        self.shop.add_sweet("Sweet1", "Cat1", 10.0, 5)
        self.shop.add_sweet("Sweet2", "Cat2", 30.0, 5)
        self.shop.add_sweet("Sweet3", "Cat3", 60.0, 5)
        results = self.shop.search_by_price_range(20.0, 50.0)
        self.assertEqual(len(results), 1)

    def test_purchase_sweet(self):
        sweet = self.shop.add_sweet("Kaju", "Nut", 50.0, 10)
        self.shop.purchase_sweet(sweet.id, 3)
        self.assertEqual(sweet.quantity, 7)

    def test_purchase_insufficient_stock(self):
        sweet = self.shop.add_sweet("Gulab Jamun", "Milk", 40.0, 2)
        with self.assertRaises(InsufficientStockError):
            self.shop.purchase_sweet(sweet.id, 5)

    def test_restock_sweet(self):
        sweet = self.shop.add_sweet("Ladoo", "Festive", 20.0, 10)
        self.shop.restock_sweet(sweet.id, 5)
        self.assertEqual(sweet.quantity, 15)

    def test_restock_negative_quantity(self):
        sweet = self.shop.add_sweet("Ladoo", "Festive", 20.0, 10)
        with self.assertRaises(ValueError):
            self.shop.restock_sweet(sweet.id, -3)

if __name__ == '__main__':
    unittest.main()
