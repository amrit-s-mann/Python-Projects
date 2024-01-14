class Inventory:
    def __init__(self, max_capacity):
        self.items = {}
        self.item_count = 0
        self.max_capacity = max_capacity
        pass

    def add_item(self, name, price, quantity):
        if self.item_count + quantity > self.max_capacity:
            return False
        if name not in self.items:
            return False
        
        self.items[name] = {"name": name, "price": price, "quantity": quantity}
        self.item_count += quantity
        return True

    def delete_item(self, name):
        if name not in self.items:
            return False
        
        del self.items[name]
        return True

    def get_items_in_price_range(self, min_price, max_price):
        temp_list = []
        for item in self.items.values():
            if item["price"] >= min_price and item["price"] <= max_price:
                temp_list.append(item["name"])
        return temp_list

    def get_most_stocked_item(self):
        most_stocked_item_name = None
        largest_quantity = 0

        for item in self.items.values():
            name = item["name"]
            quantity = item["quantity"]

            if quantity > largest_quantity:
                most_stocked_item_name = name
                largest_quantity = quantity

        return most_stocked_item_name

