from room import Room

from player import Player

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


def compass(player, direction):
    attr = direction + '_to'

    if hasattr(player.location, attr):
        player.location = getattr(player.location, attr)
    else:
        print("You can't go that direction")


player = Player(room["outside"])


user_playing = True

while True:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print("\n")
    print(player.location)
    # * Waits for user input and decides what to do.
    user_input = input(
        "\nEnter (n), (s), (e), (w) or (q) to: ").strip().lower().split()
    # first_first_char = first_char[0]
    # first_char = first_first_char[0]
    # If the user enters "q", quit the game.
    if user_input[0] == 'q':
        break
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    # User can enter 'north', 'south', 'east', 'west', or just allow them to
    # enter 'n', 's', 'e', 'w' in order to move
    # strip off everything but the first char

    if user_input[0] == 'n':
        # move to the north
        compass(player, user_input[0])
    elif user_input[0] == 's':
        # move to the south
        compass(player, user_input[0])
    elif user_input[0] == 'e':
        # move to the east
        compass(player, user_input[0])
    elif user_input[0] == 'w':
        # move to the west
        compass(player, user_input[0])
