from typing import Dict, Union, Optional
"""
creates a resale shop object that can perform the functions needed of a 
resale shop
"""
class ResaleShop:
    """
initializes the variables inventory and item_id so they can be used and added to later
"""
    def __init__(self):
        self.inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
        self.item_id = 0

    """
Takes in a Dict containing all the information about a computer,
adds it to the inventory, returns the assigned item_id
"""
    def buy(self, computer: Dict[str, Union[str, int, bool]]):
        self.item_id = self.item_id + 1
        self.inventory[self.item_id] = computer
        return self.item_id

    """
prints all the items in the inventory (if it isn't empty), prints error otherwise
"""
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
         # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")

    """
Updates the price depending on the year of the computer and updates the os in the inventory
"""
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

        if new_os is not None:
            computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

    """
Takes in an item_id, removes the associated computer if it is the inventory, 
prints error message otherwise
"""
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    """
updates the price of an item to the price defined by the variable new_price
"""
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")