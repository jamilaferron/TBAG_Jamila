from character import Enemy
from item import Item, Weapon
from room import Room
from door import generate_locked_door

import time
import sys

def print_sequence( symbol_sequence, message):
    for _ in range(1):  # Loop through the sequence multiple times
        for symbol in symbol_sequence:
            sys.stdout.write(f"\r{symbol} {message} {symbol}  ")  # Overwrites the current line
            sys.stdout.flush()  # Ensure the output is written immediately
            time.sleep(0.2)  # Pause between prints

def print_enemy(inhabitant):
    print_sequence(["👹", " ", "👹", " ", "👹"], f"{inhabitant}is in this room!")

def print_item(item):
    print_sequence(["✨", " ", "✨", " ", "✨"], f"You see a {item} here.")

def inventory_remove_item(inventory, item_name):
    for item in inventory:
        if item.name == item_name:
            inventory.remove(item)
            print(f"Removed: {item.name}")
            break  # Exit the loop after removing the item
    else:
        print(f"Item '{item_name}' not found in inventory.")



kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall = Room("dining hall")
dining_hall.set_description("A large room with ornate golden decorations")
study = Room("study")
study.set_description("A dark dusty room with large shelves")

sunstone_staff = Weapon("sunstone staff", "A staff made from a sunstone, glowing with radiant light. It can channel healing energy and repel dark forces.")
shock_grenade = Weapon("shock grenade", "A throwable device that explodes upon impact, releasing a shockwave that stuns enemies.")
sword = Weapon("sword", "A silver sword")
key = Item("key", "Locked door key")
ring = Item("ring", "A Shiny gold ring")
talisman = Item("Talisman of Purity ", "A relic imbued with cleansing magic, used to purge areas corrupted by blight or to heal companions afflicted by the Blightwalker's touch.")
golems_heart = Item("Golem’s Heart", "A rare artifact that can be used to temporarily summon an Ironclad Sentinel to fight by the player's side for a short period.")

blightwalker = Enemy("The Blightwalker", "A towering figure of rot and ruin, spreading decay wherever it treads. It corrupts the forests and poisons the waters, making Elowen's nature magic weaker in its presence.")
blightwalker.set_conversation("Watch as life withers in my wake… nothing can escape decay.")
blightwalker.set_weakness(sunstone_staff)

sentinel = Enemy("Ironclad Sentinel", "The Ironclad Sentinel, is a remnant of an ancient civilization, fit perfectly in the crumbling ruins of the Lost Temple, guarding its secrets.")
sentinel.set_conversation("Your weapons are like whispers against steel!")
sentinel.set_weakness(sunstone_staff)



kitchen.link_room(dining_hall, "south")
kitchen.set_item(sunstone_staff)
dining_hall.link_room(ballroom,"west")
dining_hall.link_room(study, "east")

dining_hall.set_character(blightwalker)
study.set_character(sentinel)
dining_hall.set_item(shock_grenade)
ballroom.set_item(sword)
study.set_item(key)
blightwalker.set_treasure(talisman)
sentinel.set_treasure(golems_heart)
                         
current_room = kitchen

game_over = False
inventory = []
current_room = kitchen

# Game loop
while not game_over:
    current_room.get_details()
    print("\n")
    actions = ["[i]nventory", "[n]orth", "[e]ast", "[s]outh", "[w]est"]

    # Check if there's a character in the room
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        actions.extend(["[t]alk", "[f]ight", "[r]ob"])
        print_enemy(inhabitant.get_name())
        print(f"\n{inhabitant.get_description()}")

    # Check if there's an item in the room
    item = current_room.get_item()
    if item:
        actions.append(f"[p]ick up {item.get_name()}")
        print_item(item.get_name())
        

  # Get player input
    print("\n---------------------------------------")
    print("\nWhat action would you like to do?\n")
    action_list = ""
    for i, action in enumerate(actions):
        action_list += f"{action}                    "
    print(f"{action_list}\n")
    command = input(">").lower()
  
     # Allow moving with n, e, s, w commands
    direction_map = {'n': 'north', 'e': 'east', 's': 'south', 'w': 'west'}
    command = direction_map.get(command, command)  
          

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

    elif command == "talk" or command == 't':
        if inhabitant:
            inhabitant.talk()

    elif command == "rob" or command == 'r':
        if inhabitant:
            has_stolen = inhabitant.steal_from()
            if has_stolen:
                treasure = inhabitant.get_treasure()
                inventory.append(treasure)
                inhabitant.set_treasure(None)

    elif command.startswith('pick up') or command == 'p':
        # Attempt to pick up the item in the room
        if item:
            if command == 'p':
                command = f"pick up {item.get_name()}"

            if command == f'pick up {item.get_name()}':
                inventory.append(item)
                print(f"You picked up the {item.get_name()}.")
                current_room.set_item(None)  # Remove the item from the room after picking it up
            else:
                print(f"You can't pick up a {command[8:]} here.")
        else:
            print("There is no such item here.")

    elif command == 'inventory' or command == 'i':
        print("Inventory")
        print("_____________________")
        for idx, item in enumerate(inventory):
            if isinstance(item, Weapon):
                print(f"{idx}. {item.get_name()} - {item.get_num_uses()}")
            else:
                print(f"{idx}. {item.get_name()}")

    elif command == 'fight' or command == 'f':
    # Handle fight logic
        if inhabitant:
            if len(inventory) > 0:
                inhabitant.talk()

                weapons = [item for item in inventory if isinstance(item, Weapon)]

                print(f"\nWhat will you fight {inhabitant.get_name()} with?:")
                for idx, item in enumerate(weapons):
                    print(f"{idx}. {item.get_name()}")

                weapon_index = input(">")
                
                # Validate weapon index
                if weapon_index.isdigit() and int(weapon_index) < len(weapons):
                    selected_weapon = weapons[int(weapon_index)]

                    has_won = inhabitant.fight(selected_weapon.get_name())

                    if has_won:
                        # Reduces the number of times a player can use a weapon 
                        selected_weapon.reduce_num_uses()

                        # If the number of uses reaches 0, remove the weapon from the inventory
                        if selected_weapon.get_num_uses() == 0:
                            inventory_remove_item(inventory, selected_weapon.get_name())

                        current_room.set_character(None)  # Remove the character after defeating them
                    else:
                        game_over = True
                else:
                    print("Invalid weapon selection.")
            else:
                print("You have no weapon to fight with.")
        else:
            print("There's no enemy here.")
    else:
        print("I don't understand that command.")
