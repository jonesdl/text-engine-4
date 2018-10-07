import json
import os


def change_room_name(room=None, room_name=None):
    # ##
    # Updates a rooms name.
    # The room name is displayed when entering a room.
    # The room name also determines the '.room' file name.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    if room:
        if "room_name" in room:
            if room_name:
                # Updating room name and the reference to the room file.
                room["room_name"] = room_name
                room["room_file"] = "./Rooms/{}.room".format(room_name.replace(" ", "_"))

                # TODO Recursively find/update all exit references in other rooms. [Dakotah]

            else:
                # TODO Error handling for 'No room name was supplied.'.
                print()
        else:
            # TODO Error handling for 'Invalid room format supplied'.
            print()
    else:
        # TODO Error handling for 'No room supplied'
        print()


def set_room_description(room=None, room_description=None):
    # ##
    # Changes a room description to a room.
    # This message will be displayed when a user supplies a 'look' command.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    change_room_description(room, room_description)


def change_room_description(room=None, room_description=None):
    # ##
    # Changes a room description to a room.
    # This message will be displayed when a user supplies a 'look' command.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if room:
        if "description" in room:
            if room_description:
                room["description"] = room_description
            else:
                # TODO Error handling for 'No room description was supplied'
                print()
        else:
            # TODO Error handling for 'Invalid room format supplied'.
            print()
    else:
        # TODO Error handling for 'No room supplied'
        print()


def create_object(object_name=None,
                  object_description=None,
                  alias=None,
                  illuminated=False,
                  obtainable=True,
                  inventory=None,
                  door=None,
                  triggers=None):
    # ##
    # Creates an object that the player can interact with.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    out = None

    if object_name:
        out = dict()
        out[object_name] = dict()
        obj = out[object_name]

        if object_description:
            if type(object_description) is str:
                obj["description"] = object_description

                if alias and type(alias) is list:
                    obj["alias"] = alias
                else:
                    obj["alias"] = []
                    if type(alias) is not list:
                        # TODO Error handling for "Invalid type supplied to alias argument."
                        print()

                if type(illuminated) is bool:
                    obj["illuminated"] = illuminated
                else:
                    obj["illuminated"] = False
                    # TODO Error handling for "Invalid type supplied to illuminated argument."
                    print()

                if type(obtainable) is bool:
                    obj["obtainable"] = obtainable
                else:
                    obj["obtainable"] = True
                    # TODO Error handling for "Invalid type supplied to obtainable argument."
                    print()

                if inventory:
                    if type(inventory) is dict:
                        # TODO Add checks for correct input.
                        for key, value in inventory.items():
                            obj["inventory"] = inventory
                    else:
                        # TODO Error handling for "Invalid type supplied for inventory argument."
                        print()
                else:
                    obj["inventory"] = dict()

                if door:
                    if type(door) is dict:
                        # TODO Add checks for correct input.
                        obj["door"] = door
                    else:
                        # TODO Error handling for "Invalid type supplied for door argument."
                        print()
                else:
                    obj["door"] = dict()

                if triggers:
                    if type(triggers) is dict:
                        # TODO Add checks for correct input.
                        for key, value in triggers.items():
                            obj["triggers"][key] = value
                    else:
                        # TODO Error handling for "Invalid type supplied for triggers argument."
                        print()
                else:
                    obj["triggers"] = dict()

            else:
                # TODO Error handling for "Invalid type supplied for object description."
                print()
        else:
            # TODO Error handling for "No object description supplied."
            print()
    else:
        # TODO Error handling for "No object name supplied."
        print()

    return out


def add_light_to_room(room=None):
    # ##
    # Adds light to a room preventing darkness.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room:
        if type(room) is dict:
            if "illuminated" in room:
                room["illuminated"] = True
            else:
                # TODO Error handling for 'Invalid object supplied to room argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for room argument.'
            print()
    else:
        # TODO Error handling for 'No object supplied for room argument.'
        print()


def remove_light_from_room(room=None):
    # ##
    # Removes light from a room causing darkness.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    if room:
        if type(room) is dict:
            if "illuminated" in room:
                room["illuminated"] = False
            else:
                # TODO Error handling for 'Invalid object supplied for room argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for room argument.'
            print()
    else:
        # TODO Error handling for 'No object supplied for room argument.'
        print()


def add_light_to_object(obj=None):
    # ##
    # Adds light to an object.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if obj:
        if type(obj) is dict:
            if len(obj) == 1:
                for key, value in obj.items():
                    if "illuminated" in value:
                        value["illuminated"] = True
                    else:
                        # TODO Error handling for 'Invalid object supplied for room argument.'
                        print()
            else:
                # TODO Error handling for 'Too many objects supplied within obj argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for room argument.'
            print()
    else:
        # TODO Error handling for "No room or object supplied."
        print()


def remove_light_from_object(obj=None):
    # ##
    # Removes light from an object.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if obj:
        if type(obj) is dict:
            if len(obj) == 1:
                for key, value in obj.items():
                    if "illuminated" in value:
                        value["illuminated"] = False
                    else:
                        # TODO Error handling for 'Invalid object supplied for room argument.'
                        print()
            else:
                # TODO Error handling for 'Too many objects supplied within obj argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for room argument.'
            print()
    else:
        # TODO Error handling for "No room or object supplied."
        print()


def create_room(room_name="",
                room_file="",
                description="",
                illuminated=True,
                inventory=None,
                exits=None,
                triggers=None):
    # ##
    # Creates a room to be further manipulated via the other room API functions.
    # Base room creation function.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    room_dict = dict()
    if room_name:
        room_dict["room_name"] = room_name
        if not room_file:
            room_file = "./Rooms/{}.room".format(room_name.replace(" ", "_"))
        room_dict["room_file"] = room_file

        if not description:
            # TODO Error handling for room without description.
            print()

        room_dict["description"] = description
        room_dict["illuminated"] = illuminated

        if not inventory:
            room_dict["inventory"] = dict()
        else:
            room_dict["inventory"] = inventory

        if not exits:
            room_dict["exits"] = dict()
        else:
            room_dict["exits"] = exits

        if not triggers:
            room_dict["triggers"] = dict()
        else:
            room_dict["triggers"] = triggers

    else:
        # TODO Error handling for no name entered.
        print()

    return room_dict


def load_room(room_name=None, room_file=None):
    # ##
    # Load a json formatted room file.
    #
    # @author Dakotah Jones
    # @date 10/03/2018
    # ##

    out = None
    if room_name or room_file:
        if not (room_name and room_file):
            if room_name:
                file_path = "./Rooms/{}.room".format(room_name.replace(" ", "_"))
                if os.path.isfile(file_path):
                    with open(file_path) as f:
                        out = json.load(f)
                    f.close()
                else:
                    # TODO Error handling for "File does not exist."
                    print()

            if room_file:
                if "../" not in room_file and not room_file.startswith("/"):
                    if os.path.isfile(room_file):
                        with open(room_file) as f:
                            out = json.load(f)
                        f.close()
                    else:
                        # TODO Error handling for "File does not exist."
                        print()
                else:
                    # TODO Error handling for "Illegal file path supplied."
                    print()
        else:
            # TODO Error handling for too many arguments supplied. (One or the other.)
            print()
    else:
        # TODO Error handling for no arguments supplied.
        print()

    return out


def save_room(room=None):
    # ##
    # Save a json formatted room file to the file system.
    #
    # @author Dakotah Jones
    # @date 10/03/2018
    # ##

    if room:
        if "room_file" in room:
            room_file = room["room_file"]
            room_json = json.dumps(room, indent=4)
            if "../" not in room_file and room_file.endswith(".room"):
                if os.path.isfile(room_file):
                    yes = ["y", "yes"]
                    no = ["n", "no"]
                    overwrite = input(
                        "Room file already exists, would you like to overwrite {}: ".format(room["room_name"]))

                    while overwrite not in yes and overwrite not in no:
                        overwrite = input("Invalid option supplied, overwrite (y/n): ")

                    if overwrite in yes:
                        tmp_file = "{}.tmp".format(room_file)
                        with open(tmp_file, "w") as f:
                            f.write(room_json)
                        f.close()
                        os.remove(room_file)
                        os.rename(tmp_file, room_file)
                    else:
                        # TODO Notify the user that the room data has not been saved.
                        print()
                else:
                    with open(room_file, "w+") as f:
                        f.write(room_json)
                    f.close()
            else:
                # TODO Error handling for "Invalid file name."
                print()
        else:
            # TODO Error handling for "Invalid object supplied as room argument."
            print()
    else:
        # TODO Error handling for "No object supplied as room argument."
        print()


def add_object_to_room(room=None, item=None):
    if room is not None and item is not None:
        for key, value in item.items():
            room["inventory"][key] = value


def create_alias_list():
    # ##
    # Simple return an empty list function.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    return []


def add_alias_to_alias_list(alias=None, alias_list=None):
    # ##
    # Add an alias to a standalone alias list.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if type(alias_list) is list:
        if alias:
            if type(alias) is str:
                alias_list.append(alias)
            else:
                # TODO Error Handling for "Illegal type supplied to alias argument"
                print()
        else:
            # TODO Error Handling for "No string supplied to alias argument"
            print()
    else:
        # TODO Error Handling for "Illegal type supplied to alias list argument"
        print()


def remove_alias_to_alias_list(alias=None, alias_list=None):
    # ##
    # Remove an alias to from a standalone alias list.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if type(alias_list) is list:
        if alias:
            if type(alias) is str:
                if alias in alias_list:
                    alias_list.remove(alias)
                else:
                    # TODO Error Handling for "Alias supplied was not part of the alias list."
                    print()
            else:
                # TODO Error Handling for "Illegal type supplied to alias argument"
                print()
        else:
            # TODO Error Handling for "No string supplied to alias argument"
            print()
    else:
        # TODO Error Handling for "Illegal type supplied to alias list argument"
        print()


def apply_alias_list_to_object(obj=None, alias_list=None):
    # ##
    # Sets an alias list to the supplied object
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if obj:
        if type(obj) is dict:
            if "alias" in obj:
                if type(alias_list) is list:
                    obj["alias"] = alias_list
                else:
                    # TODO Error Handling for 'Illegal type supplied for alias list argument.
                    print()
            else:
                # TODO Error Handling for 'Invalid object supplied to obj argument.'
                print()
        else:
            # TODO Error Handling for 'Illegal type supplied to obj argument.'
            print()
    else:
        # TODO Error Handling for 'No object supplied to obj argument.'
        print()


def add_alias_to_object(obj=None, alias=None):
    # ##
    # Add an alias to an object.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if obj:
        if "alias" in obj:
            if alias:
                if type(alias) is str:
                    object_alias = obj["alias"]
                    object_alias.append(alias)
                else:
                    # TODO Error Handling for 'Illegal type supplied for alias argument.'
                    print()
            else:
                # TODO Error Handling for 'No string supplied as alias argument.'
                print()
        else:
            # TODO Error Handling for 'Invalid object supplied as obj argument.'
            print()
    else:
        # TODO Error Handling for 'No object supplied as obj argument.'
        print()


def remove_an_alias_from_object(obj=None, alias=None):
    # ##
    # Remove an alias to an object.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if obj:
        if type(obj) is dict and "alias" in obj:
            if alias:
                if type(alias) is str:
                    object_alias_list = obj["alias"]
                    if alias in object_alias_list:
                        object_alias_list.remove(alias)
                    else:
                        # TODO Error Handling for 'Alias supplied was not an alias of this object.'
                        print()
                else:
                    # TODO Error Handling for 'Illegal type supplied for alias argument.'
                    print()
            else:
                # TODO Error Handling for 'No string supplied as alias argument.'
                print()
        else:
            # TODO Error Handling for 'Invalid object supplied as obj argument.'
            print()
    else:
        # TODO Error Handling for 'No object supplied as obj argument.'
        print()


def clear_object_alias_list(obj=None):
    # ##
    # Remove an alias to an object.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if obj:
        if type(obj) is dict and "alias" in obj:
            object_alias_list = obj["alias"]
            object_alias_list = []
        else:
            # TODO Error Handling for 'Invalid object supplied as obj argument.'
            print()
    else:
        # TODO Error Handling for 'No object supplied as obj argument.'
        print()


# TODO This one is going to be harder than originally expected.
# TODO Map this out before starting.
def link_two_rooms(start_room=None, direction=None, destination_room=None, locked=False, door_open=True, open_description="", locked_description="", door_key=""):
    if start_room is None:
        print("Error :: No starting was provided.")
    elif direction is None:
        print("Error :: No direction was provided.")
    elif destination_room is None:
        print("Error :: No destination_room was provided.")
    else:
        start_room["go"][direction] = dict()
        room_exit = start_room["go"][direction]
        room_exit["room_name"] = destination_room["room_name"]
        room_exit["locked"] = locked
        room_exit["open"] = door_open
        room_exit["open_description"] = open_description
        room_exit["key"] = door_key
