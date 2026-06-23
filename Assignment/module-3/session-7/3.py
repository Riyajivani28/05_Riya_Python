class ZomatoOrder:
    def add_item(self, item_name, quantity=1):
        print("Item added:", item_name)
        print("Quantity:", quantity)
        print("----------------------")
order = ZomatoOrder()
item = input("Enter food item: ")
qty_input = input("Enter quantity (press Enter for default 1): ")
if qty_input == "":
    order.add_item(item)
else:
    order.add_item(item, int(qty_input))