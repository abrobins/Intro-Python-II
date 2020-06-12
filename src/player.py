from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def move(self, direction):

        if hasattr(self.location, f'{direction}_to'):
            self.location = getattr(self.location, f'{direction}_to')

        else:
            print("You can't go that direction")

    def drop_item(self, item_d):
        for item_of_player in self.inventory:
            if item_of_player == item_d:
                self.inventory.remove(item_of_player)
                self.location.items.append(item_of_player)

    def print_inv(self):
        curr_inventory = "Current Inventory: "
        for i, item in enumerate(self.inventory):
            curr_inventory += " " + str(i+1) + "-" + item
        print(curr_inventory)
