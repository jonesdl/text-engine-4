from Util.RoomUtil import *
from Objects.Trigger import *

from os import chdir
chdir("..")

# CREATE START ROOM.
# NORTH: OPEN EXIT LEADING TO THE HALLWAY
start_room = create_room(room_name="Missing Flag Room",
                         description="A well lit room surrounded with decorations.\n"
                                     "In the center of the room stands a plaque mentioning a flag.\n"
                                     "You look around the room but no flag can be seen.\n"
                                     "An archway to the north leads into an open hallway.\n"
                                     "At the end of the hallway through an open door you spot the flag.")

# TRIGGER: NOTIFICATION THAT THE STORAGE ROOM DOOR HAS SLAMMED SHUT AND LOCKED.
door_slam = PrintTrigger(trigger_command="go",
                         description="As you enter the hallway the door to the north slams shut.\n"
                                     "You hear the a 'click' as the door locks from the other side.\n"
                                     "I wonder if there is another key around here.\n")
apply_trigger(start_room, door_slam)

# CREATE HALLWAY TO THE NORTH
# NORTH: LOCKED DOOR LEADING TO STORAGE ROOM
# EAST:  DOOR LEADING TO LARGE BEDROOM
lock_room = create_room(room_name="Hallway",
                        description="To the north there is a door to the storage room.\n"
                                    "To the east there is a door to a large bedroom.\n")

# LINK THE MISSING FLAG ROOM AND THE HALLWAY
link_two_rooms(start_room, lock_room, "north", "A very tall open archway.")


# CREATE LARGE BEDROOM TO THE EAST OF THE HALLWAY
# WEST: DOOR LEADING TO THE HALLWAY
# ITEM: STORAGE ROOM KEY
key_room = create_room(room_name="Large Bedroom",
                       description="A large comfy looking bed sits on the opposite end of the room.\n"
                                   "As you look around you notice a glint of light reflecting off of a key sitting on a bedside table.\n"
                                   "I wonder if that key will unlock the door in the hallway.")


# LINK HALLWAY TO BEDROOM
link_two_rooms(lock_room, key_room, "east", "A sturdy bedroom door.")


# CREATE THE BEDROOM DOOR
# APPLY THE BEDROOM DOOR TO BOTH ROOMS
hallway_east_exit = lock_room.get_exit("east")
bedroom_door = create_door()
apply_door_to_exit(hallway_east_exit, bedroom_door)
bedroom_west_exit = key_room.get_exit("west")
apply_door_to_exit(bedroom_west_exit, bedroom_door)


# CREATE THE STORAGE ROOM
# SOUTH: HALLWAY (BLOCKED)
# WEST: HIDDEN CORRIDOR TO MISSING FLAG ROOM
# ITEM: FLAG
flag_room = create_room(room_name="Storage Room",
                        description="A dimly lit storage room.\n"
                                    "Ornate antique furniture sit untouched, "
                                    "covered in weathered cloth and blankets of dust.\n"
                                    "The flag seems to be the only object in the room that has been moved in years.\n"
                                    "Flickers of light come from a stone archway to the west.")


# LINK HALLWAY TO STORAGE ROOM
link_two_rooms(lock_room, flag_room, "north", "A locked door to a storage room.")


# CREATE THE STORAGE ROOM DOOR AND LOCK
hallway_north_exit = lock_room.get_exit("north")
storage_room_lock, storage_room_key = create_lock_and_key("storage room key", "An old brass key.")
storage_room_door = create_door()
apply_lock_to_door(storage_room_door, storage_room_lock)
apply_door_to_exit(hallway_north_exit, storage_room_door)


# CREATE THE DOOR AND LOCK FROM THE INSIDE VIEW
storage_room_south_exit = flag_room.get_exit("south")
storage_room_south_exit.block()
storage_room_lock, storage_room_key = create_lock_and_key("storage room key", "An old brass key.", False)
storage_room_door = create_door(True)
apply_lock_to_door(storage_room_door, storage_room_lock)
apply_door_to_exit(storage_room_south_exit, storage_room_door)


# UPON ENTERING A ROOM THE EXIT GETS BLOCKED
falling_cabinet = PrintTrigger("enter", "As you enter the room a dusty old cabinet falls over and blocks the southern door.")
apply_trigger(flag_room, falling_cabinet)


# CREATE HIDDEN CORRIDOR
user_script_room = create_room(room_name="Hidden Corridor",
                               description="A dark hidden tunnel with a glimpse of light to the south.\n"
                                           "The stone archway to the east leads back into the storage room.")


# LINK THE STORAGE ROOM AND THE HIDDEN CORRIDOR
link_two_rooms(flag_room, user_script_room, "west", "A stone archway.")


# CREATE EXIT WHICH LEADS BACK TO START ROOM
hidden_corridor_south_exit = create_room_exit(compass_direction="south",
                                              links_to=start_room.room_file,
                                              description="The light at the end of the tunnel leads to the missing flag room.")
apply_exit_to_room(user_script_room, hidden_corridor_south_exit)


# CREATE EXAMPLE USER SCRIPT
user_script = create_user_script(trigger_command="enter",
                                 before="print('Hello World!')",
                                 instead="print('This was done instead!')",
                                 after="self.load('Rooms/Missing_Flag_Room.room')")
apply_user_script(user_script_room, user_script)


rooms = [start_room,
         lock_room,
         key_room,
         flag_room,
         user_script_room]

for room in rooms:
    room.save()
