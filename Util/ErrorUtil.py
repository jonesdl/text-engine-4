import os

def error_handler(function, reason):
     # ##
    # Is called whenever an error occurs.
    # Asks the user if they'd like to see documentation for the errored function.
    #
    # So far, error messages are created for:
    # change_room_name
    # change_room_description
    #
    #
    #
    #
    #
    # @author Anthony Catricala
    # @date 10/10/2018
    # ##

    # change_room_name
    if function = ("change_room_name"):
        print("It looks like you're trying to change the name of a room, ", end= "")

    if reason = "no name":
        print("but haven't given a room name.")
    elif reason = "invalid format":
        print("but did not use the command in the correct format.")
    elif reason = "no room":
        print("but did not specify which room you want to edit.")

    print("Would you like to see the documentation on changing room names? [y/n]")

    #change_room_description
    elif function = ("change_room_description"):
        print("It looks like you're trying to change a room's description, ", end= "")

    if reason = "no discription":
        print("but haven't given a new description for the room.")
    elif reason = "invalid format":
        print("but did not use the command in the correct format.")
    elif reason = "no room":
        print("but did not specify which room you want to edit.")

    print("Would you like to see the documentation for changing a room's description? [y/n]")

    #add_light_to_room
    elif function = ("add_light_to_room"):
        print("It looks like you're trying to add a light to a room, ", end= "")

    if reason = "invalid object":
        print("but you haven't given the command a valid object.")
    elif reason = "invalid type":
        print("but did not use a valid type.")
    elif reason = "no object":
        print("but did not supply an object for the Room argument.")

    print("Would you like to see the documentation for adding lights to rooms? [y/n]")

    #remove_light_from_room
    elif function = ("remove_light_from_room"):
        print("It looks like you're trying to remove a light from a room, ", end= "")

    if reason = "invalid object":
        print("but you haven't given the command a valid object.")
    elif reason = "invalid type":
        print("but did not use a valid type.")
    elif reason = "no object":
        print("but did not supply an object for the Room argument.")

    print("Would you like to see the documentation for removing lights from rooms? [y/n]")

    #create_room
    elif function = ("create_room"):
        print("It looks like you're trying to create a room, ", end= "")

    if reason = "no description":
        print("but haven't given a description for your new room.")
    elif reason = "no name":
        print("but haven't given a name for your new room.")

    print("Would you like to see the tutorial for creating rooms? [y/n]")

    #load room
    elif function = ("load_room"):
        print("It looks like you're trying to load a room, ", end= "")

    if reason = "file does not exist":
        print("but the file you're trying to load doesn't exist.")
    elif reason = "illegal file path":
        print("but you've given an invalid file path")
    elif reason = "too many arguments":
        print("but you've given too many arguments in your function.")
    elif reason = "no arguments":
        print("but you haven't put any arguments in your function.")

    print("Would you like to see the tutorial for loading rooms? [y/n]")










#--------------------------------------------------------------------------------
    
    see_tutorial = input().lower()

    if see_tutorial = "y" or "yes" or "":
        tutorial = "./Documentation/{}.txt".format(function)
        os.startfile(tutorial)
        exit()
    else:
        exit()