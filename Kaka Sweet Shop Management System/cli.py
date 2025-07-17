from sweetshop import SweetShop, InsufficientStockError, SweetNotFoundError

class SweetShopCLI:
    def __init__(self):
        self.shop = SweetShop()
        self._initialize_sample_data()

    def _initialize_sample_data(self):
        self.shop.add_sweet("Kaju Katli", "Nut-Based", 50.0, 20)
        self.shop.add_sweet("Gajar Halwa", "Vegetable-Based", 30.0, 15)
        self.shop.add_sweet("Gulab Jamun", "Milk-Based", 10.0, 50)

    def display_menu(self):
        print("\n=== Sweet Shop Management System ===")
        print("1. Add Sweet")
        print("2. Delete Sweet")
        print("3. View All Sweets")
        print("4. Search by Name")
        print("5. Search by Category")
        print("6. Search by Price Range")
        print("7. Purchase Sweet")
        print("8. Restock Sweet")
        print("9. Exit")
        print("====================================")

    def display_sweets(self, sweets):
        if not sweets:
            print("No sweets found.")
            return
        print("\n{:<6} {:<20} {:<20} {:<10} {:<10}".format(
            "ID", "Name", "Category", "Price", "Quantity"
        ))
        print("-" * 70)
        for sweet in sweets:
            print("{:<6} {:<20} {:<20} {:<10.2f} {:<10}".format(
                sweet.id, sweet.name, sweet.category, sweet.price, sweet.quantity
            ))

    def run(self):
        print("Welcome to Sweet Shop Management System!")
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-9): ").strip()
            try:
                if choice == '1':
                    self.add_sweet()
                elif choice == '2':
                    self.delete_sweet()
                elif choice == '3':
                    self.view_all_sweets()
                elif choice == '4':
                    self.search_by_name()
                elif choice == '5':
                    self.search_by_category()
                elif choice == '6':
                    self.search_by_price_range()
                elif choice == '7':
                    self.purchase_sweet()
                elif choice == '8':
                    self.restock_sweet()
                elif choice == '9':
                    print("Thank you for using the system!")
                    break
                else:
                    print("Invalid choice.")
            except Exception as e:
                print(f"Error: {e}")

    # Implement other methods (add_sweet, delete_sweet, etc.) from your code

if __name__ == '__main__':
    SweetShopCLI().run()
