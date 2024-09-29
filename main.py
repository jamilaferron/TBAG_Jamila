from character import Enemy
from item import Item
from room import Room
import curses

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall = Room("dining hall")
dining_hall.set_description("A large room with ornate golden decorations")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")

cheese = Item("cheese", "A big block of smelly cheese")
sword = Item("sword", "A silver sword")

kitchen.link_room(dining_hall, "south")
kitchen.set_item(sword)
dining_hall.link_room(ballroom,"west")

dining_hall.set_character(dave)
dining_hall.set_item(cheese)


def display_inventory(stdscr, inventory):
  stdscr.addstr(0, 0, "Your inventory contains:")
  for idx, item in enumerate(inventory):
      stdscr.addstr(1 + idx, 0, f"{idx}. {item.get_name()}")
    
  stdscr.addstr(10, 0, f"press 'q' to quit")
  stdscr.refresh()

def inventory_add_item(stdscr, inventory, item):
  inventory.append(item)  # Add the item to the inventory
  stdscr.addstr(11, 0, f"You picked up the {item.get_name()}.")
  stdscr.refresh()
  stdscr.nodelay(False)  # Disable non-blocking mode to wait for key press

def fight_mode(stdscr, inventory, inhabitant):
    count = 0  # To keep track of the selected weapon

    stdscr.clear()  # Clear the screen for the fight mode interface
    stdscr.addstr(0, 0, "Fight Mode:")
    stdscr.addstr(1, 0, f"What will you fight {inhabitant.get_name()} with?")

    # Loop to display and select weapons from inventory
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Fight Mode:")
        stdscr.addstr(1, 0, f"What will you fight {inhabitant.get_name()} with?")

        # Display inventory options
        for idx, item in enumerate(inventory):
            if idx == count:
                stdscr.addstr(3 + idx, 0, f"> {item.get_name()}")  # Highlight selected weapon
            else:
                stdscr.addstr(3 + idx, 0, f"  {item.get_name()}")

        stdscr.addstr(len(inventory) + 5, 0, "Use UP/DOWN arrow keys to choose, ENTER to confirm.")

        stdscr.refresh()  # Refresh the screen to show the changes
        key = stdscr.getch()  # Capture user input

        # Handle arrow key navigation
        if key == curses.KEY_UP and count > 0:
            count -= 1  # Move up in the list
        elif key == curses.KEY_DOWN and count < len(inventory) - 1:
            count += 1  # Move down in the list
        elif key == curses.KEY_ENTER or key in [10, 13]:  # ENTER key (Linux: 10, Windows: 13)
            selected_weapon = inventory[count]
            break  # Exit the loop when the player confirms their selection

    # Show the selected weapon
    stdscr.clear()
    stdscr.addstr(0, 0, f"You selected the {selected_weapon.get_name()} to fight {inhabitant.get_name()}.")
    stdscr.addstr(1, 0, "Press any key to continue to the fight...")
    stdscr.refresh()
    stdscr.nodelay(False)  # Disable non-blocking mode to wait for key press
    stdscr.getch()  # Wait for key press
    stdscr.nodelay(True)  # Enable non-blocking mode again

    # Perform the fight
    has_won = inhabitant.fight(selected_weapon.get_name())

    # Clear the screen and show the fight result
    stdscr.clear()

    if has_won:
        stdscr.addstr(0, 0, f"You have defeated {inhabitant.get_name()} with the {selected_weapon.get_name()}!")
        fight_result = "won"
    else:
        stdscr.addstr(0, 0, f"You were defeated by {inhabitant.get_name()}... Game Over!")
        fight_result = "lost"

    stdscr.addstr(2, 0, "Press any key to return to the game...")  # Add a message for the user to continue
    stdscr.refresh()

    # Wait for the user to press a key to proceed
    stdscr.nodelay(False)
    stdscr.getch()  # Wait for key press
    stdscr.nodelay(True)  # Re-enable non-blocking mode for further game play

    return fight_result  # Return whether the player won or lost

def main(stdscr):
    # Setup for curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(5)   # Make getch() non-blocking
    stdscr.timeout(100) # Refresh screen every 100ms

    game_over = False
    inventory = []
    current_room = kitchen  
    inventory_mode = False
    pick_up_item = False
    can_move = True
    fighting_mode = False
    
    while not game_over:
        
      stdscr.clear()  # Clear the screen
      stdscr.refresh()  # Refresh the screen to show changes

      stdscr.addstr(1, 0, "Use arrow keys to move, 'p' to pick up, 'f' to fight, 'i' to check inventory, 'q' to quit.")
      # Display room details
      stdscr.addstr(2, 0, current_room.get_details())

      # Check if there's an item in the room
      item = current_room.get_item()
      if item:
        stdscr.addstr(11, 0, f"You see a {item.get_name()} here.")
      
      # Check if there is an inhabitant in the room
      inhabitant = current_room.get_character()
      if inhabitant:
        stdscr.addstr(12, 0, inhabitant.describe())

      # Check if game is in inventory mode
      if inventory_mode:
          stdscr.clear()
          display_inventory(stdscr, inventory)
      
      # Check if item picked up
      if pick_up_item:
        inventory_add_item(stdscr, inventory, item) 
        current_room.set_item(None)
        pick_up_item = False

      # movement check
      if not can_move:
         stdscr.addstr(15, 0, "You can't go that way.")
      else: 
        can_move = True

      # Check if game is in fight mode      
      if fighting_mode:
          # Check if there is an inhabitant in the room before entering fight mode
        if inhabitant:
            # Enter fight mode
            fight_result = fight_mode(stdscr, inventory, inhabitant)
            if fight_result == "lost":
                game_over = True  # If the player lost, end the game
            elif fight_result == "won":
               current_room.set_character(None)               
        else:
            stdscr.refresh()
            stdscr.nodelay(False)

       # Capture keyboard input  
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
      elif key == ord('p'):
        command = 'pick up'
      elif key == ord('f'):
        fighting_mode = True
      elif key == ord('i'):
        # Clear the screen before showing the inventory
        stdscr.clear()  
        command = 'inventory'
      elif key == ord('q'):
        if inventory_mode:
           inventory_mode = False
        elif fighting_mode:
          fighting_mode = False 
        else:
           game_over = True  # Set game_over to True to exit the loop
        command = 'quit'
      else:
        command = None  # No valid command

      # Pick up item
      if command == 'pick up' and item:
        pick_up_item = True
      
      # Open inventory
      if command == 'inventory':
         inventory_mode = True

      # Move character 
      if command in ['north', 'south', 'east', 'west']:
        if command in current_room.get_linked_rooms():
            can_move = True
            current_room = current_room.move(command)
        else:
          can_move = False
      
      if command == 'quit':
        stdscr.addstr(16, 0, "Quitting the game...")

    stdscr.refresh()  # Refresh after processing commands

# Run the game
if __name__ == "__main__":
    curses.wrapper(main)
