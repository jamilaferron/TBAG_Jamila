from character import Enemy
from item import Item
from room import Room
from door import generate_locked_door

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall = Room("dining hall")
dining_hall.set_description("A large room with ornate golden decorations")
study = Room("study")
study.set_description("A dark dusty room with large shelves")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")

brad = Enemy("Bard", "A smelly golom")
brad.set_conversation("My precious....")
brad.set_weakness("sword")

cheese = Item("cheese", "A big block of smelly cheese")
sword = Item("sword", "A silver sword")
key = Item("key", "Locked door key")
ring = Item("ring", "A Shiny gold ring")

kitchen.link_room(dining_hall, "south")
kitchen.set_item(sword)
dining_hall.link_room(ballroom,"west")
dining_hall.link_room(study, "east")

dining_hall.set_character(dave)
dining_hall.set_item(cheese)
study.set_item(key)
dave.set_treasure(ring)
study.set_character(brad)
                         
current_room = kitchen

game_over = False
inventory = []
current_room = kitchen

# Game loop
while not game_over:
  current_room.get_details()

  # Check if there's a character in the room
  inhabitant = current_room.get_character()
  if inhabitant is not None:
      inhabitant.describe()

  # Check if there's an item in the room
  item = current_room.get_item()
  if item:
      print(f"You see a {item.get_name()} here.")

  # Get player input
  command = input("What do you want to do? ").lower()

  if command in ['north', 'south', 'east', 'west']:
      # Move to another room if possible
      linked_rooms = current_room.get_linked_rooms()
      if command in linked_rooms:
          current_room = current_room.move(command)
      else:
          random_door = generate_locked_door()
          if random_door:
              print("You have found a locked door")
              should_unlock = input("Try to unlock [y]es [n]o ").lower()

              if should_unlock == "y" and any(item.name == "key" for item in inventory):
                  print("The door swings open")
              elif should_unlock == "y" and not any(item.name == "key" for item in inventory):
                  print("You need to find the key for this door")
              else:
                print("You have decided to go a different way")

          else:
            print("You can't go that way.")

  elif command == "talk":
    if inhabitant:
        inhabitant.talk()
  elif command == "steal":
    if inhabitant:
        has_stolen = inhabitant.steal_from()
        if has_stolen:
            treasure = inhabitant.get_treasure()
            inventory.append(treasure)
            inhabitant.set_treasure(None)
  elif command.startswith('pick up'):
      # Attempt to pick up the item in the room
      if item:
          if command == f'pick up {item.get_name()}':
              inventory.append(item)
              print(f"You picked up the {item.get_name()}.")
              current_room.set_item(None)  # Remove the item from the room after picking it up
          else:
              print(f"You can't pick up a {command[8:]} here.")
      else:
          print("There is no such item here.")
  elif command == 'inventory':
      print("Inventory")
      print("_____________________")
      print(inventory)
      for idx, item in enumerate(inventory):
        print(f"{idx}. {item.get_name()}")

  elif command == 'fight':
      # Handle fight logic
      if inhabitant:
          if len(inventory) > 0:
             
              weapon = input(f"What will you fight {inhabitant.get_name()} with?: ").lower()
              
              # Check if the weapon is in the player's inventory
              if weapon in [item.get_name() for item in inventory]:
                  has_won = inhabitant.fight(weapon)
                  if has_won:
                      print(f"You defeated {inhabitant.get_name()}!")
                      current_room.set_character(None)  # Remove the character after defeating them
                  else:
                      print(f"{inhabitant.get_name()} defeated you!")
                      game_over = True
              else:
                  print(f"You don't have a {weapon} in your inventory.")
          else:
              print("You have no weapon to fight with.")
      else:
          print("There's no enemy here.")

  else:
      print("I don't understand that command.")
