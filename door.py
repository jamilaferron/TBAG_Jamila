import random


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

def generate_locked_door():
  """Randomly generate an item based on probability."""
  chance = random.random()  # Random float between 0 and 1
  if chance < 0.4:  # 30% chance to generate an item
      print_door(8, 7)  # Return a random item from the list
      return True  # Return a random item from the list
  return False  # No item generated