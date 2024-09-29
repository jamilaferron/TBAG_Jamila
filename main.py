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

                         
# Assume Room and Character classes are defined elsewhere, as well as kitchen and other rooms.

def display_inventory(stdscr, inventory):
    stdscr.addstr(0, 0, "Inventory:")
    for idx, item in enumerate(inventory):
        #fix item description
        stdscr.addstr(1 + idx, 0, f"- {item}")
    stdscr.refresh()

def inventory_add_item(stdscr, inventory, item):
  inventory.append(item)  # Add the item to the inventory
  # Flashes very quickly
  stdscr.addstr(15, 0, f"You picked up the {item.get_name()}.")

def main(stdscr):
    # Setup for curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(5)   # Make getch() non-blocking
    stdscr.timeout(100) # Refresh screen every 100ms

    game_over = False
    inventory = []
    current_room = kitchen  
    show_inventory = False
    pick_up_item = False
    
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
      
      inhabitant = current_room.get_character()
      if inhabitant:
        stdscr.addstr(12, 0, inhabitant.describe())

      if show_inventory:
          stdscr.clear()
          display_inventory(stdscr, inventory)
      
      if pick_up_item:
        inventory_add_item(stdscr, inventory, item) 
        current_room.set_item(None)
        pick_up_item = False

      key = stdscr.getch()  # Capture keyboard input

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
        command = 'fight'
      elif key == ord('i'):
        stdscr.clear()  # Clear the screen before showing the inventory
        show_inv = True
      elif key == ord('q'):
        if show_inventory:
           show_inventory = False
        else:
           game_over = True  # Set game_over to True to exit the loop
        command = 'quit'
      else:
        command = None  # No valid command

      if command == 'pick up' and item:
        pick_up_item = True
      
      # fix else block not displaying
      if command in ['north', 'south', 'east', 'west']:
        if command in current_room.get_linked_rooms():
            current_room = current_room.move(command)
        else:
          stdscr.addstr(6, 0, "You can't go that way.")

      # fix fighting logic
      if command == 'fight':
        # Handle fight logic
        if inhabitant:
            stdscr.addstr(18, 0, f"What will you fight {inhabitant.get_name()} with?")
            has_won = inhabitant.fight('cheese')
            # if has_won:
            #     print(f"You defeated {inhabitant.get_name()}!")
            #     current_room.set_character(None)  # Remove the character after defeating them
            # else:
            #     print(f"{inhabitant.get_name()} defeated you!")
            #     game_over = True
            # if len(inventory) > 0:
            #     stdscr.addstr(15, 0, f"What will you fight {inhabitant.get_name()} with?")
            #     # weapon = input(f"What will you fight {inhabitant.get_name()} with?: ").lower()
                
            #     # Check if the weapon is in the player's inventory
            #     if command in [item.get_name() for item in inventory]:
            #         has_won = inhabitant.fight(command)
            #         if has_won:
            #             print(f"You defeated {inhabitant.get_name()}!")
            #             current_room.set_character(None)  # Remove the character after defeating them
            #         else:
            #             print(f"{inhabitant.get_name()} defeated you!")
            #             game_over = True
            #     else:
            #         print(f"You don't have a {command} in your inventory.")
            # else:
            #     print("You have no weapon to fight with.")
        else:
            print("There's no enemy here.")
      
      if command == 'quit':
        stdscr.addstr(16, 0, "Quitting the game...")

    stdscr.refresh()  # Refresh after processing commands

# Run the game
if __name__ == "__main__":
    curses.wrapper(main)
