from typing import List, Dict
from sweet import Sweet

class InsufficientStockError(Exception): pass
class SweetNotFoundError(Exception): pass

class SweetShop:
    def __init__(self):
        self._sweets: Dict[int, Sweet] = {}
        self._next_id = 1001
    
    def add_sweet(self, name: str, category: str, price: float, quantity: int) -> Sweet:
        sweet = Sweet(self._next_id, name, category, price, quantity)
        self._sweets[self._next_id] = sweet
        self._next_id += 1
        return sweet

    def delete_sweet(self, sweet_id: int) -> None:
        if sweet_id not in self._sweets:
            raise SweetNotFoundError(f"Sweet with ID {sweet_id} not found")
        del self._sweets[sweet_id]
    
    def get_sweet(self, sweet_id: int) -> Sweet:
        if sweet_id not in self._sweets:
            raise SweetNotFoundError(f"Sweet with ID {sweet_id} not found")
        return self._sweets[sweet_id]
    
    def view_all_sweets(self) -> List[Sweet]:
        return list(self._sweets.values())
    
    def search_by_name(self, name: str) -> List[Sweet]:
        return [s for s in self._sweets.values() if name.lower() in s.name.lower()]
    
    def search_by_category(self, category: str) -> List[Sweet]:
        return [s for s in self._sweets.values() if category.lower() == s.category.lower()]
    
    def search_by_price_range(self, min_price: float, max_price: float) -> List[Sweet]:
        return [s for s in self._sweets.values() if min_price <= s.price <= max_price]
    
    def purchase_sweet(self, sweet_id: int, quantity: int) -> None:
        if sweet_id not in self._sweets:
            raise SweetNotFoundError(f"Sweet with ID {sweet_id} not found")
        sweet = self._sweets[sweet_id]
        if sweet.quantity < quantity:
            raise InsufficientStockError(f"Only {sweet.quantity} in stock.")
        sweet.quantity -= quantity
    
    def restock_sweet(self, sweet_id: int, quantity: int) -> None:
        if sweet_id not in self._sweets:
            raise SweetNotFoundError(f"Sweet with ID {sweet_id} not found")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._sweets[sweet_id].quantity += quantity
    
    def get_total_sweets_count(self) -> int:
        return len(self._sweets)
