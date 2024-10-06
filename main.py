from character import Enemy, Friend
from item import Item, Weapon
from room import Room

def inventory_remove_item(inventory, item_name):
    for item in inventory:
        if item.name == item_name:
            inventory.remove(item)
            break  # Exit the loop after removing the item
    else:
        print(f"Item '{item_name}' not found in inventory.")

# Weapons
sunstone_staff = Weapon("sunstone staff", "A staff made from a sunstone, glowing with radiant light. It can channel healing energy and repel dark forces.")
shock_grenade = Weapon("shock grenade", "A throwable device that explodes upon impact, releasing a shockwave that stuns enemies.")
sword = Weapon("sword", "A silver sword")

# Items
key = Item("key", "Locked door key")
ring = Item("ring", "A Shiny gold ring")
talisman = Item("Talisman of Purity ", "A relic imbued with cleansing magic, used to purge areas corrupted by blight or to heal companions afflicted by the Blightwalker's touch.")
golems_heart = Item("Golem’s Heart", "A rare artifact that can be used to temporarily summon an Ironclad Sentinel to fight by the player's side for a short period.")
bark_amulet = Item("Sacred Bark Amulet", "An enchanted relic made from the bark of a once-mighty tree, symbolizing the protection and longevity of the forest.")
astral_map = Item("Astral Map", "A detailed chart of the constellations, showing hidden stars and paths unknown to most mortals, enhancing her ability to navigate the night.")

# Friendly characters
willowroot = Friend("Elder Willowroot","A wise, ancient talking tree who has deep knowledge of the forest and its history. Often gives guidance to adventurers and protects the balance of nature.")
willowroot.set_conversation("The Thicket is twisted with dark roots. Fire will clear the way, but only light can banish what lurks within.")
willowroot.set_token(bark_amulet)

luna = Friend("Luna the Night Sage", "A mysterious figure draped in dark robes, adorned with shimmering stars. She appears at night and offers cryptic prophecies, granting temporary night vision or revealing hidden paths.")
luna.set_conversation("Under the pale moonlight, shadows cast long but light reveals the way.")
luna.set_token(astral_map)

# Enemy Characters
blightwalker = Enemy("The Blightwalker", "A towering figure of rot and ruin, spreading decay wherever it treads. It corrupts the forests and poisons the waters, making Elowen's nature magic weaker in its presence.")
blightwalker.set_conversation("Watch as life withers in my wake… nothing can escape decay.")
blightwalker.set_weakness(sunstone_staff)
blightwalker.set_treasure(talisman)

sentinel = Enemy("Ironclad Sentinel", "The Ironclad Sentinel, is a remnant of an ancient civilization, fit perfectly in the crumbling ruins of the Lost Temple, guarding its secrets.")
sentinel.set_conversation("Your weapons are like whispers against steel!")
sentinel.set_weakness(shock_grenade)
sentinel.set_treasure(golems_heart)

# Set up Rooms
elder_grove = Room("Elder Willowroot's Grove")
elder_grove.set_description("A majestic grove dominated by the ancient Elder Willowroot tree, a wise guardian of the forest.")
elder_grove.set_character(willowroot)
elder_grove.set_item(key)

glade = Room("Glade")
glade.set_description("A peaceful clearing filled with soft grass and surrounded by tall trees.")
glade.set_item(bark_amulet)

mushroom_grove = Room("Mushroom Grove")
mushroom_grove.set_description("A grove filled with vibrant, oversized mushrooms of all colors.")
mushroom_grove.set_item(sunstone_staff)

darkened_thicket = Room("Darkened Thicket")
darkened_thicket.set_description("A shadowy part of the forest where the light struggles to penetrate, home to mysterious creatures.")
darkened_thicket.set_character(blightwalker)
darkened_thicket.set_item(key)

whispering_meadow = Room("Whispering Meadow")
whispering_meadow.set_description("A serene meadow where the whispers of the wind carry secrets of the forest.")
whispering_meadow.set_character(luna)

glimmering_stream = Room("Glimmering Stream")
glimmering_stream.set_description("A sparkling stream filled with crystal-clear water, where small fish dart playfully.")
glimmering_stream.set_item(shock_grenade)

hidden_fae_village = Room("Hidden Fae Village")
hidden_fae_village.set_description("A magical village concealed by illusion, where the fae gather and share their wisdom.")
hidden_fae_village.set_item(astral_map)

ruins_of_temple = Room("Ruins of the Lost Temple")
ruins_of_temple.set_description("Ancient, crumbling structures that hint at a time when magic was worshiped.")
ruins_of_temple.set_character(sentinel)

# Link Rooms
elder_grove.link_room(glade, "south", False)
glade.link_room(mushroom_grove, "east", False) 
mushroom_grove.link_room(darkened_thicket, "south", False)
mushroom_grove.link_room(whispering_meadow, "east", True)
darkened_thicket.link_room(glimmering_stream, "east", False)
glimmering_stream.link_room(whispering_meadow, "north", False)
whispering_meadow.link_room(hidden_fae_village, "east", False)
hidden_fae_village.link_room(ruins_of_temple, "north", False)

game_over = False
inventory = []
current_room = elder_grove

# Game loop
while not game_over:
    # while not current_room.get_locked_status(): 
        current_room.get_details()
        print("\n")
        actions = ["[i]nventory", "[n]orth", "[e]ast", "[s]outh", "[w]est"]

        # Check if there's a character in the room
        inhabitant = current_room.get_character()
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            actions.extend(["[t]alk", "[f]ight", "[r]ob"])
            inhabitant.describe()
        elif inhabitant is not None and isinstance(inhabitant, Friend):
            actions.extend(["[t]alk", "[g]ift"])
            inhabitant.describe()

        # Check if there's an item in the room
        item = current_room.get_item()
        if item:
            actions.append(f"[p]ick up {item.get_name()}")
            print(f"You see a {item.get_name()} here.")
            
    # Get player input
        print("\n---------------------------------------")
        print("\nWhat action would you like to do?\n")
        action_list = ""
        for i, action in enumerate(actions):
            print(action)
        command = input(">").lower()
    
        # Allow moving with n, e, s, w commands
        linked_rooms = current_room.get_linked_rooms()
        direction_map = {'n': 'north', 'e': 'east', 's': 'south', 'w': 'west'}
        command = direction_map.get(command, command)  
            
        if command in ["north", "south", "east", "west"]:
            current_room = current_room.move(command, inventory)
        elif command in ["talk", "t"]:
            if inhabitant:
                inhabitant.talk()

        elif command in ["rob", "r"]:
            if inhabitant:
                has_stolen = inhabitant.steal_from()
                if has_stolen:
                    treasure = inhabitant.get_treasure()
                    inventory.append(treasure)
                    inhabitant.set_treasure(None)

        elif command.startswith("pick up") or command == "p":
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

        elif command in ["inventory", "i"]:
            print("Inventory")
            print("_____________________")
            for idx, item in enumerate(inventory):
                if isinstance(item, Weapon):
                    print(f"{idx}. {item.get_name()} - {item.get_num_uses()}")
                else:
                    print(f"{idx}. {item.get_name()}")
        elif command in ["gift", "g"]:
            if isinstance(inhabitant, Friend):
                gifts = [item for item in inventory if not isinstance(item, Weapon)]
                if len(gifts) > 0:
                    inhabitant.talk()
                    print(f"\nWhat gift will you present to {inhabitant.get_name()}?:")
                    for idx, item in enumerate(gifts):
                        print(f"{idx}. {item.get_name()}")
                    
                    gift_index = input(">")
                    if gift_index.isdigit() and int(gift_index) < len(gifts):
                        selected_gift = gifts[int(gift_index)]
                        has_gifted = inhabitant.gift(selected_gift.get_name())

                        if has_gifted:
                            inventory_remove_item(inventory, selected_gift.get_name())
                    else:
                        print("Invalid gift selection.")
                else:
                    print(f"You have no gifts to present to {inhabitant.get_name()}.")
        elif command == 'fight' or command == 'f':
        # Handle fight logic
            if isinstance(inhabitant, Enemy):
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
