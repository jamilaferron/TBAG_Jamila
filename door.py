def print_door(height, width):
    # Ensure the height is large enough to place a keyhole
    if height < 5 or width < 3:
        print("Door is too small to add a keyhole.")
        return

    # Top of the door (frame)
    print("+" + "-" * (width - 2) + "+")
    
    # Door body (sides with space or keyhole)
    keyhole_position = height // 2  # Keyhole placed at the vertical center
    for i in range(height - 2):
        if i == keyhole_position - 1:  # Place the keyhole in the middle
            print("|" + " " * ((width - 3) // 2) + "O" + " " * ((width - 3) // 2) + "|")
        else:
            print("|" + " " * (width - 2) + "|")
    
    # Bottom of the door (frame)
    print("+" + "-" * (width - 2) + "+")

def print_open_door(height, width):
    # Ensure the height and width are large enough
    if height < 5 or width < 3:
        print("Door is too small to create an open door.")
        return

    # Top of the door (frame)
    print("+" + "-" * (width - 2) + "+")
    
    # Door body (sides with open space)
    for i in range(height - 2):
        print("|" + " " * (width - 2) + "|")
    
    # Bottom of the door (frame)
    print("+" + "-" * (width - 2) + "+")