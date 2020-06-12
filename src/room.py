# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        # return f"Your current location is: {self.name} and description is: {self.description}"

        if len(self.items) > 0:
            item_list = "This room has the following: "
            for i, item in enumerate(self.items):
                item_list += " " + str(i+1) + "-" + item
            return self.name + " " + self.description + "\n" + item_list
        else:
            return self.name + " " + self.description + "\n" + "There's currently no items in this room"
