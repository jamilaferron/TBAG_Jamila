from character import Enemy
from item import Item
from room import Room

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
                         
current_room = kitchen

game_over = False
inventory = []
current_room = kitchen

  # Game loop
while not game_over:
  current_room.get_details()

  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
  
  # Check if there's an item in the room
  item = current_room.get_item()
  if item:
      print(f"You see a {item.get_name()} here.")
    
  command = input("What do you want to do? ").lower()
    

  if command in ['north', 'south', 'east', 'west']:

    if command in current_room.get_linked_rooms():
      current_room = current_room.move(command)
    else:
      print("You can't go that way.")

  elif command.startswith('pick up'):
        # Attempt to pick up the item in the room
        if item and command == f'pick up {item.get_name()}':
            if item.get_name() in ['sword', 'cheese']:
                inventory.append(item)
                print(f"You picked up the {item.get_name()}.")
                current_room.set_item(None)  # Remove the item from the room after picking it up
        else:
            print("There is no such item here.")
  elif command == 'fight':
      if inhabitant and len(inventory) > 0:
        print(inventory)
        print(inhabitant.__dict__)
        weapon = input(f"What will you fight {inhabitant.get_name()} with?: ")
        if weapon in ['sword', 'cheese']:
          has_won = inhabitant.fight(weapon)
          if has_won:
            current_room.set_character(None)
          else:
             game_over = True
        else:
           print(f"you do not have a {weapon} in your inventory" )
      else:
          print("There's no enemy here or you have no weapon.")
  else:
        print("I don't understand that command.")

