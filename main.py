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

                         
def main(stdscr):
  # Setup for curses
  curses.curs_set(0)  # Hide the cursor
  stdscr.nodelay(1)   # Make getch() non-blocking
  
  game_over = False
  inventory = []
  current_room = kitchen
  while not game_over:
    stdscr.clear()  # Clear the screen

    # Display room details
    stdscr.addstr(1, 0, current_room.get_details())

    inhabitant = current_room.get_character()
    if inhabitant:
        stdscr.addstr(3, 0, f"You see {inhabitant.get_name()} here.")
        # inhabitant.describe()

    # Check if there's an item in the room
    # item = current_room.get_item()
    # if item:
    #     print(f"You see a {item.get_name()} here.")

    # Get player input
    # command = input("What do you want to do? ").lower()
    # stdscr.clear()  # Clear the screen

    # # Display room details
    # current_room.get_details()

    # inhabitant = current_room.get_character()
    # if inhabitant:
    #     inhabitant.describe()

    # item = current_room.get_item()
    # if item:
    #   stdscr.addstr(1, 0, f"You see a {item.get_name()} here.")
    
    # stdscr.addstr(2, 0, "Use arrow keys to move, 'p' to pick up, 'f' to fight, 'i' to check inventory, 'q' to quit.")
    # stdscr.refresh()

    # # Capture keyboard input
    # key = stdscr.getch()

    # if key == curses.KEY_UP:
    #   command = 'north'
    # elif key == curses.KEY_DOWN:
    #   command = 'south'
    # elif key == curses.KEY_LEFT:
    #   command = 'west'
    # elif key == curses.KEY_RIGHT:
    #   command = 'east'
    # elif key == ord('p'):
    #   command = 'pick up'
    # elif key == ord('f'):
    #   command = 'fight'
    # elif key == ord('i'):
    #   command = 'inventory'
    # elif key == ord('q'):
    #   game_over = True
    #   command = 'quit'
    # else:
    #   command = None

    # # Process the command (similar to your current game logic)
    # if command in ['north', 'south', 'east', 'west']:
    #   directions = current_room.get_linked_rooms()
    #   if command in directions:
    #     current_room = current_room.move(command)
    #   else:
    #     stdscr.addstr(4, 0, "You can't go that way.")

    # elif command == 'pick up' and item:
    #   inventory.append(item)
    #   stdscr.addstr(4, 0, f"You picked up the {item.get_name()}.")
    #   current_room.set_item(None)

    # elif command == 'fight' and inhabitant:
    #   if len(inventory) > 0:
    #     stdscr.addstr(5, 0, "Inventory: " + ", ".join([i.get_name() for i in inventory]))
    #     weapon = input(f"What will you fight {inhabitant.get_name()} with?: ").lower()
    #     if weapon in [i.get_name().lower() for i in inventory]:
    #       has_won = inhabitant.fight(weapon)
    #       if has_won:
    #         stdscr.addstr(6, 0, f"You defeated {inhabitant.get_name()}!")
    #         current_room.set_character(None)
    #       else:
    #         stdscr.addstr(6, 0, f"{inhabitant.get_name()} defeated you!")
    #         game_over = True
    #     else:
    #       stdscr.addstr(6, 0, f"You don't have a {weapon} in your inventory.")
    #   else:
    #       stdscr.addstr(5, 0, "You have no weapon to fight with.")

    # elif command == 'inventory':
    #   if inventory:
    #     stdscr.addstr(4, 0, "Inventory: " + ", ".join([i.get_name() for i in inventory]))
    #   else:
    #     stdscr.addstr(4, 0, "Your inventory is empty.")

    stdscr.refresh()

if __name__ == "__main__":
  curses.wrapper(main)