class Room:
    def __init__(self, description_in="", north_in=None, east_in=None, south_in=None, west_in=None):
        self.description = description_in
        self.north = north_in
        self.east = east_in
        self.south = south_in
        self.west = west_in


def main():

    global next_room
    user_input = ""
    room_list = []
    current_room = 0
    done = False

    """Dungeon: Room 0"""
    room = Room("You're in a dark, windowless room. You're hungover, and you dont know where you're at..\n"
                "However, you know your not in Kansas anymore..But you notice a faint light coming from the north\n"
                "Despite what they say about going into the light... you should probably it.",
                1,
                None,
                None,
                None)
    room_list.append(room)

    """Dungeon Hallway: Room 1"""
    room = Room("You enter the dungeon hallway. It's long, dark, and smells kinda funny.\n"
                "It's still hard to see but there is a light toward the north.",
                2,
                None,
                1,
                None)
    room_list.append(room)

    """Secure Area: Room 2"""
    room = Room("You come to an intersection in the hallway, surrounded by doors.\n"
                "Which door, which door? There is no more light to be seen. Adventure awaits..",
                4,
                3,
                1,
                5)
    room_list.append(room)

    """Closet: Room 3"""
    room = Room("You entered a supply closet. There is nothing here for you. Unless you feel like cleaning..",
                None,
                None,
                None,
                2)
    room_list.append(room)

    """Chambers: Room 4"""
    room = Room("You enter a chamber with a bunch of scary looking tools and a very uncomfortable looking bed.\n"
                "This was not listed on the AirBNB listing..this is... torture...\n"
                "Probably should leave the way you came..slowly but quickly.",
                None,
                None,
                2,
                None)
    room_list.append(room)

    """Upper Level: Room 5"""
    room = Room("You picked the right door and are now hiking up the stairs./n"
                "The light can be seen again to the north, the light of hope.",
                6,
                2,
                None,
                None)
    room_list.append(room)

    """Upper Hallway: Room 6"""
    room = Room("Dang, another hallway, at least this one smells better..\n"
                "The light you see to the north isn't your hangover, although its not helping..",
                7,
                None,
                5,
                None)
    room_list.append(room)

    """Warehouse: Room 7"""
    room = Room("You exit the hallway into an abandoned warehouse.\n"
                "You still dont know where you are but one thing is for sure..\n"
                "Your friends are jerks for leaving you here.",
                8,
                9,
                6,
                None)
    room_list.append(room)

    """Outside: Room 8"""
    room = Room("Take a breath of fresh air and adjust to the sun..You see all of your friends cheering.\n"
                "You have escaped the building and survived pledge week.\n"
                "Congratulations, you are now a member of a fraternity.\n"
                "Your parents should be proud.",
                None,
                None,
                7,
                None)
    room_list.append(room)

    """Bathroom: Room 9"""
    room = Room("Nothing like draining the tank after an experience like that.",
                None,
                None,
                None,
                7)
    room_list.append(room)

    """Main Game"""
    while user_input is not done:
        print("")
        print(room_list[current_room].description)
        print("")
        user_input = input("Where do you want to go? ").upper()

        if user_input == "N" or user_input == "NORTH":
            next_room = room_list[current_room].north

        elif user_input == "S" or user_input == "SOUTH":
            next_room = room_list[current_room].south

        elif user_input == "E" or user_input == "EAST":
            next_room = room_list[current_room].east

        elif user_input == "W" or user_input == "WEST":
            next_room = room_list[current_room].west

        if next_room is None:
            print("")
            print("You can't go that way")

        else:
            current_room = next_room

        if next_room == 8:
            print(room_list[8].description)
            break


main()
