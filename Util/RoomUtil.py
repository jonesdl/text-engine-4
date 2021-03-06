from Util.ErrorUtil import *
from Objects.Item import Item
from Objects.Room import Room
from Objects.Exit import Exit
from Objects.Door import Door
from Objects.Lock import Lock
from Objects.Trigger import Trigger
from Objects.UserScript import UserScript

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

    if room and type(room) is Room:
        if room_name and type(room_name) is str:
            room.room_file = room.room_file.replace(room.room_name.replace(" ", "_"), room_name.replace(" ", "_"))
            room.room_name = room_name
            room.save()
        else:
            error_handler("change_room_name", "no name")
    else:
        error_handler("change_room_name", "no room")


def set_room_description(room=None, room_description=None):
    # ##
    # Changes a room description to a room.
    # This message will be displayed when a user supplies a 'look' command.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    #
    # @arg room WhatIF Room Object
    # @arg room_description String describing the room.

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

    if room and type(room) is Room:
        if room_description:
            room.description = room_description
        else:
            error_handler("change_room_description", "invalid format")
    else:
        error_handler("change_room_description", "no room")


def add_light_to_room(room=None):
    # ##
    # Adds light to a room.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room and type(room) is Room:
        room.illuminated = True
    else:
        error_handler("add_light_to_room", "no object")


def remove_light_from_room(room=None):
    # ##
    # Removes light from a room.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    if room and type(room) is Room:
        room.illuminated = False
    else:
        error_handler("remove_light_from_room", "no object")


def create_room(room_name="",
                description="",
                illuminated=True,
                inventory=None,
                exits=None,
                triggers=None,
                user_scripts=None,
                visited=False):
    # ##
    # Creates a room to be further manipulated via the other room API functions.
    # Base room creation function.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    out = None
    if room_name:
        room_dict = dict()
        room_dict["room_name"] = room_name
        room_dict["room_file"] = "./Rooms/{}.room".format(room_name.replace(" ", "_"))

        if not description:
            error_handler("create_room", "no description")

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
            room_dict["triggers"] = list()
        else:
            room_dict["triggers"] = triggers

        if not user_scripts:
            room_dict['user-scripts'] = list()
        else:
            room_dict['user-scripts'] = user_scripts

        room_dict['visited'] = visited

        out = Room.from_dict(room_dict)
        out.save()

    else:
        error_handler("create_room", "no name")

    return out


def load_room(room_name=None, room_file=None):
    # ##
    # Load a json formatted room file.
    #
    # @author Dakotah Jones
    # @date 10/03/2018
    #
    # @arg room_name The room name spelled correctly with spaces.
    # @arg room_file The URL of the room file on disk.
    # @returns WhatIF Room Object.
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
                    error_handler("load_room", "file does not exist")

            if room_file:
                if "../" not in room_file and not room_file.startswith("/"):
                    if os.path.isfile(room_file):
                        with open(room_file) as f:
                            out = json.load(f)
                        f.close()
                    else:
                        error_handler("load_room", "file does not exist")
                else:
                    error_handler("load_room", "illegal file path")
            if out:
                out = Room.from_dict(out)
        else:
            error_handler("load_room", "too many arguments")
    else:
        error_handler("load_room", "no arguments")

    return out


def save_room(room=None):
    # ##
    # Save a json formatted room file to the file system.
    #
    # @author Dakotah Jones
    # @date 10/03/2018
    #
    # @arg room A WhatIF Room Object.
    # ##

    if room and type(room) is Room:
        room.save()
    else:
        error_handler("save_room", "no object")


def add_object_to_room(room=None, obj=None):
    if room:
        if isinstance(room, Room):
            if obj:
                if isinstance(obj, Item):
                    room.inventory.append(obj)
                else:
                    error_handler("add_object_to_room", "invalid object type")
            else:
                error_handler("add_object_to_room", "no object")
        else:
            error_handler("add_object_to_room", "invalid room type")
    else:
        error_handler("add_object_to_room", "no object")


# TODO Combe back to this when Items have been created.
def remove_object_from_room(room=None, obj_name=None):
    if room:
        if type(room) is dict:
            if "inventory" in room:
                inventory = room["inventory"]
                if type(inventory) is dict:
                    if type(obj_name) is str:
                        if obj_name in inventory:
                            # TODO Take quantity into account, drop quantity till zero then delete. [Dakotah]
                            del(inventory[obj_name])
                        else:
                            error_handler("remove_object_from_room", "no object")
                    else:
                        error_handler("remove_object_from_room", "invalid type")
                else:
                    error_handler("remove_object_from_room", "invalid format")
            else:
                error_handler("remove_object_from_room", "invalid object")
        else:
            error_handler("remove_object_from_room", "invalid type")
    else:
        error_handler("remove_object_from_room", "no room")


def create_door(is_open=False,
                lock=None,
                triggers=None,
                user_scripts=None):
    # ##
    # Create a door that can then be placed on containers or exits.
    #
    # @author Dakotah Jones
    # @date 10/03/2018
    # ##
    door_dict = dict()
    door_dict["open"] = is_open
    if lock:
        door_dict["lock"] = lock
    else:
        door_dict["lock"] = dict()

    if triggers:
        door_dict["triggers"] = triggers
    else:
        door_dict["triggers"] = list()

    if not user_scripts:
        door_dict["user-scripts"] = list()
    else:
        door_dict['user-scripts'] = user_scripts

    out = Door.from_dict(door_dict)

    return out


def create_lock(key: Item=None,
                is_locked=True,
                triggers=None,
                user_scripts=None):

    if key and isinstance(key, Item):
        lock_dict = dict()
        lock_dict["key"] = key.item_name
        lock_dict["locked"] = is_locked

        if triggers:
            lock_dict["triggers"] = triggers
        else:
            lock_dict["triggers"] = list()

        if user_scripts:
            lock_dict['user-scripts'] = user_scripts
        else:
            lock_dict["user-scripts"] = list()

        lock = Lock.from_dict(lock_dict)

    return lock


def apply_lock_to_door(door=None, lock=None):
    if lock:
        if type(lock) is Lock:
            if door:
                if type(door) is Door:
                    door.lock = lock
                else:
                    error_handler("apply_lock_to_door", "invalid door type")
            else:
                error_handler("apply_lock_to_door", "no door object")
        else:
            error_handler("apply_lock_to_door", "invalid lock type")
    else:
        error_handler("apply_lock_to_door", "no lock object")


def remove_lock_from_door(door=None):
    if door:
        if type(door) is Door:
            if door.lock:
                door.lock = None
            else:
                # TODO Error handling for 'There is no lock on that door.'
                print()
        else:
            error_handler("remove_lock_from_door", "invalid door type")
    else:
        error_handler("remove_lock_from_door", "no object")


def create_room_exit(compass_direction="",
                     links_to="",
                     description="",
                     is_blocked=False,
                     door=None,
                     triggers=None,
                     user_scripts=None):

    compass_direction = compass_direction.lower()
    compass_directions = ["north",
                          "northeast",
                          "east",
                          "southeast",
                          "south",
                          "southwest",
                          "west",
                          "northwest"]

    out = None
    if compass_direction:
        if type(compass_direction) is str:
            if compass_direction in compass_directions:

                if links_to:
                    if type(links_to) is str:
                        if os.path.isfile(links_to):

                            if description:
                                if type(description) is str:
                                    out = dict()
                                    out[compass_direction] = dict()

                                    room_exit = out[compass_direction]
                                    room_exit["links-to"] = links_to
                                    room_exit["description"] = description
                                    room_exit["blocked"] = is_blocked

                                    if door:
                                        room_exit["door"] = door
                                    else:
                                        room_exit["door"] = dict()

                                    if triggers:
                                        room_exit["triggers"] = triggers
                                    else:
                                        room_exit["triggers"] = list()

                                    if user_scripts:
                                        room_exit["user-scripts"] = user_scripts
                                    else:
                                        room_exit["user-scripts"] = list()

                                    out = Exit.from_dict(compass_direction, room_exit)

                                else:
                                    error_handler("create_room_exit", "invalid description type")
                            else:
                                error_handler("create_room_exit", "no description string")
                        else:
                            error_handler("create_room_exit", "room does not exist")
                    else:
                        error_handler("create_room_exit", "invalid link type")
                else:
                    error_handler("create_room_exit", "no link string")
            else:
                error_handler("create_room_exit", "invalid compass direction")
        else:
            error_handler("create_room_exit", "invalid compass direction type")
    else:
        error_handler("create_room_exit", "no compass direction string")

    return out


def apply_door_to_exit(room_exit=None, door=None):
    if room_exit:
        if type(room_exit) is Exit:
            if type(door) is Door:
                room_exit.door = door
            else:
                # TODO Error handling for 'Invalid type supplied for door argument.'
                print()
        else:
            error_handler("apply_door_to_exit", "invalid door type")
    else:
        error_handler("apply_door_to_exit", "no exit object")


def remove_door_from_exit(room_exit=None):
    if room_exit:
        if type(room_exit) is Exit:
            if room_exit.door:
                room_exit.door = None
            else:
                # TODO Error handling for 'No door exists on that exit.'
                print()
        else:
            error_handler("remove_door_from_exit", "invalid type")
    else:
        error_handler("remove_door_from_exit", "no object")


def apply_exit_to_room(room=None, room_exit=None):
    if room:
        if type(room) is Room:
            if room_exit:
                if type(room_exit) is Exit:
                    room.exits.append(room_exit)
                else:
                    error_handler("apply_exit_to_room", "invalid exit type")
            else:
                error_handler("apply_exit_to_room", "no exit object")
        else:
            error_handler("apply_exit_to_room", "invalid room type")
    else:
        error_handler("apply_exit_to_room", "no room object")


def remove_exit_from_room(room=None, compass_direction=None):
    compass_direction = compass_direction.lower()
    compass_directions = ["north",
                          "northeast",
                          "east",
                          "southeast",
                          "south",
                          "southwest",
                          "west",
                          "northwest"]

    if room:
        if type(room) is Room:
            if compass_direction:
                if type(compass_direction) is str:
                    room_exits = room.exits
                    if compass_direction in compass_directions:
                        exit_found = False
                        for e in room_exits:
                            if e.compass_direction == compass_direction:
                                room_exits.remove(e)
                        if not exit_found:
                            error_handler("remove_exit_from_room", "no exit in speci direction")
                    else:
                        error_handler("remove_exit_from_room", "invalid string")
                else:
                    error_handler("remove_exit_from_room", "no compass direction type")
            else:
                error_handler("remove_exit_from_room", "no compass direction object")
        else:
            error_handler("remove_exit_from_room", "invalid room type")
    else:
        error_handler("remove_exit_from_room", "no room object")


def create_user_script(trigger_command="",
                       before="",
                       instead="",
                       after="",
                       before_file="",
                       instead_file="",
                       after_file=""):
    out = None
    if type(trigger_command) is str:
        if type(before) is str:
            if type(instead) is str:
                if type(after) is str:
                    out = UserScript(trigger_command, before, instead, after, before_file, instead_file, after_file)
                else:
                    # TODO Error handling; Wrong type (String)
                    print()
            else:
                # TODO Error handling; Wrong type (String)
                print()
        else:
            # TODO Error handling; Wrong type (String)
            print()
    else:
        # TODO Error handling; Wrong type (String)
        print()

    return out


def apply_user_script_to_room(room=None, user_script=None):
    if type(room) is Room:
        apply_user_script(room, user_script)
    else:
        # TODO Error handling; Wrong type (Room)
        print()


def apply_user_script_to_exit(exit=None, user_script=None):
    if type(exit) is Exit:
        apply_user_script(exit, user_script)
    else:
        # TODO Error handling; Wrong type (Exit)
        print()


def apply_user_script_to_door(door=None, user_script=None):
    if type(door) is Door:
        apply_user_script(door, user_script)
    else:
        # TODO Error handling; Wrong type (Door)
        print()


def apply_user_script_to_lock(lock=None, user_script=None):
    if type(lock) is Lock:
        apply_user_script(lock, user_script)
    else:
        # TODO Error handling; Wrong type (Lock)
        print()


def apply_user_script(obj=None, user_script=None):
    applicable_objects = [Room, Exit, Door, Lock, Item]
    if type(obj) in applicable_objects:
        if type(user_script) is UserScript:
            obj.user_scripts.append(user_script)
        else:
            # TODO Error handling; Wrong type (UserScript)
            print()
    else:
        # TODO Error handling; Wrong type (Room, Exit, Door, Lock, etc)
        print()


def apply_trigger(obj: (Room, Exit, Door, Lock, Item), trigger: Trigger):
    applicable_objects = [Room, Exit, Door, Lock, Item]
    if type(obj) in applicable_objects:
        if Trigger in type(trigger).__bases__:
            obj.triggers.append(trigger)
        else:
            # TODO Error handling for "Invalid trigger type."
            print()
    else:
        # TODO Error handling for "Invalid object type."
        print()


def link_two_rooms(from_room: Room, to_room: Room, direction: str="", description: str=""):
    compass_directions = {
        "north": "south",
        "south": "north",
        "east": "west",
        "west": "east"
    }

    if direction and direction in compass_directions.keys():
        from_room.exits.append(Exit(direction, to_room.room_file, description))
        to_room.exits.append(Exit(compass_directions[direction], from_room.room_file, description))
    else:
        # TODO Error handling for invalid compass direction.
        print()
