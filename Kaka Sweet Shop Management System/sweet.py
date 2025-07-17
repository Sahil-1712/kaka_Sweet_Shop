from dataclasses import dataclass

@dataclass
class Sweet:
    """Represents a sweet item in the shop."""
    id: int
    name: str
    category: str
    price: float
    quantity: int
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")