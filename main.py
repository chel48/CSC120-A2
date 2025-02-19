# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union

# Import the functions from computer.py and oo_resale_shop.py
from computer import Computer
from oo_resale_shop import ResaleShop

""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""
def create_computer(description: str,
                  processor_type: str,
                     hard_drive_capacity: int,
                     memory: int,
                     operating_system: str,
                     year_made: int,
                     price: int):
     return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
             'memory': memory,
             'operating_system': operating_system,
             'year_made': year_made,
             'price': price
     }

def main():
    
    # First, let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    computer = computer._create_computer()
    # print(computer)

    computer2 = Computer("Mac Pro (Late 2014)", "4.5 GHc 6-Core Intel Xeon E5",
    2048, 128, "macOS Monterey", 2014, 2000)
    computer2 = computer2._create_computer()

    #make the resale shop
    resale_shop = ResaleShop()

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer["description"])
    print("Adding to inventory...")
    itemid = resale_shop.buy(computer)
    print("Done.\n")

    print("Buying", computer2["description"])
    print("Adding to inventory...")
    itemid2 = resale_shop.buy(computer2)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resale_shop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", itemid, ", updating OS to", new_OS)
    print("Updating inventory...")
    resale_shop.refurbish(itemid, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resale_shop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", itemid)
    resale_shop.sell(itemid)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resale_shop.print_inventory()
    print("Done.\n")

    # Changes price of computer
    new_price = 2500
    print("Changing Price of Item", itemid2, "to", new_price)
    resale_shop.update_price(itemid2, new_price)
    print("Done.\n" )

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resale_shop.print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()
