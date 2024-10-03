import curses
import random
from game_setup import *
from combat import fight_mode

def main_character_select(stdscr, characters):
  count = 0  # To keep track of the selected weapon

  stdscr.addstr(0, 0, "Select your character:")

  # Loop to display and select a main character to play with
  while True:
    stdscr.clear()
    stdscr.addstr(0, 0, "Select your character:")

    # Display character options 
    for idx, character in enumerate(characters):
      if idx == count:
        stdscr.addstr(2 + idx, 0, f"> {character.get_name()}")  # Highlight selected weapon
      else:
        stdscr.addstr(2 + idx, 0, f"  {character.get_name()}")

    stdscr.addstr(len(characters) + 5, 0, "Use UP/DOWN arrow keys to choose, ENTER to confirm.")

    stdscr.refresh()  # Refresh the screen to show the changes
    key = stdscr.getch()  # Capture user input

    # Handle arrow key navigation
    if key == curses.KEY_UP and count > 0:
      count -= 1  # Move up in the list
    elif key == curses.KEY_DOWN and count < len(characters) - 1:
      count += 1  # Move down in the list
    elif key == curses.KEY_ENTER or key in [10, 13]:  # ENTER key (Linux: 10, Windows: 13)
      selected_character = characters[count]  # Select the character from the filtered list
      break 
  
  # Show the selected weapon
  stdscr.clear()
  stdscr.addstr(0, 0, f"You selected {selected_character.get_name()}.")
  stdscr.addstr(1, 0, "Press any key to continue to the game...")
  stdscr.refresh()
  stdscr.nodelay(False)  # Disable non-blocking mode to wait for key press
  stdscr.getch()  # Wait for key press
  return selected_character  # Return whether the player won or lost

def display_inventory(stdscr, inventory):
  stdscr.addstr(0, 0, "Your inventory contains:")
  for idx, item in enumerate(inventory):
      stdscr.addstr(1 + idx, 0, f"{idx}. {item.get_name()}")
    
  stdscr.addstr(10, 0, f"press 'q' to quit")
  stdscr.refresh()

def inventory_add_item(stdscr, inventory, item):
  stdscr.clear()
  inventory.append(item)  # Add the item to the inventory
  stdscr.addstr(5, 0, f"You picked up the {item.get_name()}.  ")
  stdscr.addstr(7, 0, f"Press any key to return to the game...")
  stdscr.refresh()
  stdscr.nodelay(False)  # Disable non-blocking mode to wait for key press

def generate_random_item():
  """Randomly generate an item based on probability."""
  chance = random.random()  # Random float between 0 and 1
  if chance < 0.2:  # 30% chance to generate an item
      return random.choice(possible_items)  # Return a random item from the list
  return None  # No item generated

def pick_up_item(stdscr, item, main_character):
  stdscr.clear()  # Clear the screen for the gift mode interface
  stdscr.addstr(0, 0, f"You see a {item.get_name()} here.")
  stdscr.addstr(1, 0, f"---------------------------------")
  stdscr.addstr(2, 0, f"{item.get_description()}")

  stdscr.addstr(5, 0, "press 'c' to collect or 'p' to put it down")
  stdscr.refresh()
  stdscr.nodelay(False)  # Disable non-blocking mode to wait for key press

  key = stdscr.getch() 
  if key == ord('c'):
    inventory_add_item(stdscr, main_character.get_inventory(), item) 
    return True
  elif key == ord('p'):
     return False

def gift_mode(stdscr, inventory, inhabitant):
  count = 0  # To keep track of the selected gift
  gifts = [item for item in inventory if isinstance(item, Gift)]  # Filter only gift items
  
  if not gifts:  # Check if there are no gifts available
    stdscr.addstr(0, 0, f"There are no gifts available to give to {inhabitant.get_name()}!")
    stdscr.addstr(1, 0, "Press any key to return to the game...")
    stdscr.refresh()
    stdscr.nodelay(False)
    stdscr.getch()  # Wait for key press
    stdscr.nodelay(True)  # Re-enable non-blocking mode for further gameplay
    return "no_gifts"  # Return a status indicating no gifts available
  
  stdscr.clear()  # Clear the screen for the gift mode interface
  stdscr.addstr(0, 0, "Gift Mode:")
  stdscr.addstr(1, 0, f"What will you gift to {inhabitant.get_name()}?")

  # Loop to display and select gifts from inventory
  while True:
    stdscr.clear()
    stdscr.addstr(0, 0, "Gift Mode:")
    stdscr.addstr(1, 0, f"What will you gift to {inhabitant.get_name()}?")

    # Display inventory options for only gifts
    for idx, item in enumerate(gifts):
      if idx == count:
        stdscr.addstr(3 + idx, 0, f"> {item.get_name()}")  # Highlight selected gift
      else:
        stdscr.addstr(3 + idx, 0, f"  {item.get_name()}")

    stdscr.addstr(len(gifts) + 5, 0, "Use UP/DOWN arrow keys to choose, ENTER to confirm, 'q' to quit.")
    stdscr.refresh()  # Refresh the screen to show the changes
    key = stdscr.getch()  # Capture user input

    # Handle arrow key navigation
    if key == curses.KEY_UP and count > 0:
      count -= 1  # Move up in the list
    elif key == curses.KEY_DOWN and count < len(gifts) - 1:
      count += 1  # Move down in the list
    elif key == ord('q'):  # Check if 'q' is pressed
      return "quit"  # Exit gifting mode and return to gameplay, currently has to be pressed twice
    elif key == curses.KEY_ENTER or key in [10, 13]:  # ENTER key (Linux: 10, Windows: 13)
      selected_gift = gifts[count]  # Select the gift from the filtered list
      break  # Exit the loop when the player confirms their selection

  # Show the selected gift
  stdscr.clear()
  stdscr.addstr(0, 0, f"You selected the {selected_gift.get_name()} to gift to {inhabitant.get_name()}.")
  stdscr.addstr(1, 0, "Press any key to continue gifting...")
  stdscr.refresh()
  stdscr.nodelay(False)  # Disable non-blocking mode to wait for key press
  stdscr.getch()  # Wait for key press
  stdscr.nodelay(True)  # Enable non-blocking mode again

  # Perform the gifting action
  inhabitant.receive_gift(selected_gift)  # You can define the logic for the inhabitant receiving the gift

  # Remove the gifted item from the inventory
  inventory.remove(selected_gift)

  # Clear the screen and confirm the gift was given
  stdscr.clear()
  stdscr.addstr(0, 0, f"You successfully gave the {selected_gift.get_name()} to {inhabitant.get_name()}.")
  stdscr.addstr(1, 0, "Press any key to return to the game...")
  stdscr.refresh()

  # Wait for the user to press a key to proceed
  stdscr.nodelay(False)
  stdscr.getch()  # Wait for key press
  stdscr.nodelay(True)  # Re-enable non-blocking mode for further gameplay

  return "gifted"  # Return status to indicate gift has been given

def generate_random_inhabitant(possible_inhabitants):
  """Randomly generate an item based on probability."""
  chance = random.random()  # Random float between 0 and 1
  if chance < 0.5:  # 30% chance to generate an inhabitant
      return random.choice(possible_inhabitants)
  return None  # No item generated
  
def encounter(stdscr, main_character, current_room):
    stdscr.clear()  # Clear the screen for the gift mode interface
   
    stdscr.addstr(1, 0, "--------------------------------------------------------------------------")
    stdscr.addstr(3, 0, f"You are in the {current_room.get_name()}\n--------------------------------------------- \n{current_room.get_description()}\n")

    inhabitant = current_room.get_inhabitant()
   
    if isinstance(inhabitant, Friend):          
        stdscr.addstr(0, 0, "Press 'g' to gift, or 'q' to move along.")
        stdscr.addstr(12, 0, f"You encountered {inhabitant.get_name()}, a friendly face!")
    elif isinstance(inhabitant, Enemy):
        stdscr.addstr(0, 0, "Press 'f' to fight or 'q' to attempt to flee.")
        stdscr.addstr(12, 0, f"A wild {inhabitant.get_name()} appears! Prepare for battle!")

    key = stdscr.getch() 
    if key == ord('g') and isinstance(inhabitant, Friend):
        gift_mode(stdscr, main_character.get_inventory(), inhabitant) 
        return True
    elif key == ord('f') and isinstance(inhabitant, Enemy):
        fight_result = fight_mode(stdscr, main_character, inhabitant, character_specific_damage)

        # If the fight is won, remove the enemy from the room
        if fight_result == "win":
            stdscr.addstr(14, 0, f"You defeated {inhabitant.get_name()}!")
            current_room.set_inhabitant(None)  # Remove the enemy from the room
            stdscr.addstr(15, 0, "Press any key to continue...")
            stdscr.refresh()
            stdscr.nodelay(False)
            stdscr.getch()  # Wait for key press
        return fight_result
    else:
        return None  # No interaction occurred



def main(stdscr):
  # Setup for curses
  curses.curs_set(0)  # Hide the cursor
  stdscr.nodelay(5)   # Make getch() non-blocking
  stdscr.timeout(100) # Refresh screen every 100ms

# Game modes
  game_setup_mode = True
  inventory_mode = False
  pick_up_mode = False
  encounter_mode = False

  game_over = False
  main_character = None
  current_room = elder_grove
  can_move = True

  while not game_over:
        
    stdscr.clear()  # Clear the screen
    stdscr.refresh()  # Refresh the screen to show changes

    while game_setup_mode:
      main_character = main_character_select(stdscr, [elowen, finnian, lyra, thorn])
      game_setup_mode = False
    
    stdscr.addstr(0, 0, "Use arrow keys to move, 'i' to check inventory, 'q' to quit.")
    stdscr.addstr(1, 0, "--------------------------------------------------------------------------")

    # # Display room details
    stdscr.addstr(3, 0, current_room.get_details())

    # Check if game is in inventory mode
    if inventory_mode:
        stdscr.clear()
        display_inventory(stdscr, main_character.get_inventory())
    
    if pick_up_mode:
      has_picked_up = pick_up_item(stdscr, current_room.get_item(), main_character)
      if has_picked_up:
        current_room.set_item(None)
        pick_up_mode = False
      else:
        pick_up_mode = False
    
    if encounter_mode:
        result = encounter(stdscr, main_character, current_room)
        if result == "won" or result == "fled":
            encounter_mode = False  # Exit encounter mode if the fight is over or the player flees
    
     # movement check
    if not can_move:
        # displays when exiting fight mode
        stdscr.addstr(15, 0, "You can't go that way.")
    else: 
      can_move = True

    key = stdscr.getch()  

    # Handle user input
    if key == curses.KEY_UP:
      command = 'north'
    elif key == curses.KEY_DOWN:
      command = 'south'
    elif key == curses.KEY_LEFT:
      command = 'west'
    elif key == curses.KEY_RIGHT:
      command = 'east'
    elif key == ord('i'):
      # Clear the screen before showing the inventory
      stdscr.clear()  
      inventory_mode = True
    elif key == ord('q'):
        if inventory_mode:
            inventory_mode = False
        elif encounter_mode:
            encounter_mode = False
        else:
            game_over = True  # Set game_over to True to exit the loop
    elif key == ord('f'):
      fighting_mode = True
    elif key == ord('g'):
      # Clear the screen before showing the inventory
      stdscr.clear()  
      command = 'gift'
    
    else:
      command = None  # No valid command
    
    if command in ['north', 'south', 'east', 'west']:
        if command in current_room.get_linked_rooms():
            can_move = True
            current_room = current_room.move(command)

            # Generate a random item in the new room
            new_item = generate_random_item()
            if new_item:
                current_room.set_item(new_item)  # Set the item in the room
                pick_up_mode = True
            
            new_inhabitant = generate_random_inhabitant([current_room.get_enemy(), current_room.get_friend()])
            if new_inhabitant:
               current_room.set_inhabitant(new_inhabitant)
               encounter_mode = True
        else:
            can_move = False


# Run the game
if __name__ == "__main__":
    curses.wrapper(main)