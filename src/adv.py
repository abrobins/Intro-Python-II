from room import Room

from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# player = Player("Blair", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


player = Player("Blair", room["outside"])

room["foyer"].items = ["machete", "sword"]


while True:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print("\n")
    print(player.location)
    user_input = input(
        "\nEnter (n), (s), (e), (w), (d), (i) for inventory, (take [item]), (drop [item]) or (q) to quit: ").split()
    if len(user_input) == 1:

        if user_input[0] == 'q':
            print("Thanks for playing. We hope to see you again soon!")
            break

        if user_input[0] == 'n':

            # move to the north
            player.move(user_input[0])
        if user_input[0] == 's':
            # move to the south
            player.move(user_input[0])
        if user_input[0] == 'e':
            # move to the east
            player.move(user_input[0])
        if user_input[0] == 'w':
            # move to the west
            player.move(user_input[0])
        elif user_input[0] == 'i':
            player.print_inv()

    elif len(user_input) == 2:
        if user_input[0] == "take" or user_input[0] == "get":
            for item in player.location.items:
                if item == user_input[1]:
                    player.inventory.append(item)
                    player.location.items.remove(item)
                    print(f"You have picked up {item}")
                else:
                    print("No such item in this room")
        elif user_input[0] == "drop":
            for item in player.inventory:
                if item == user_input[1]:
                    player.drop_item(user_input[1])
                    print(f"You have dropped {item}")
                else:
                    print(
                        f"{player.name} doesn't have that item in their inventory - Sorry!")
        else:
            print("Invalid user entry enter drop or get followed by the item name")
    else:
        print("Invalid user entry")
