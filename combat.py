import curses

from item import Weapon

def fight_mode(stdscr, character, enemy, character_specific_damage):
    stdscr.clear()
    stdscr.addstr(0, 0, f"A wild {enemy.name} appears!\n")
    
    weapons = [item for item in character.inventory if isinstance(item, Weapon)]  # List of weapons
    count = 0  # To keep track of selected weapon
    
    # Enemy attacks first (only once)
    stdscr.addstr(1, 0, f"{enemy.name} attacks {character.name} with its {enemy.attack['damage']} base damage!\n")
    character.take_damage(enemy.attack['damage'])
    stdscr.addstr(2, 0, f"{character.name} has {character.get_health()} health left.\n")
    stdscr.addstr(5, 0, "Press any key to continue.\n")
    stdscr.refresh()
    stdscr.getch()  # Wait for input to continue

    while character.is_alive() and enemy.is_alive():  # Loop until one is defeated
        # Weapon selection
        if weapons:
            selected_weapon = None  
            # Initialize the selected_weapon variable for each turn
            while selected_weapon is None:
                stdscr.clear()
                stdscr.addstr(0, 0, "Combat Mode:")
                stdscr.addstr(1, 0, f"Select your weapon:")

                # Display the available weapons
                for idx, item in enumerate(weapons):
                    if idx == count:
                        stdscr.addstr(3 + idx, 0, f"> {item.get_name()}")  # Highlight selected weapon
                    else:
                        stdscr.addstr(3 + idx, 0, f"  {item.get_name()}")

                stdscr.addstr(len(weapons) + 5, 0, "Use UP/DOWN arrow keys to choose, ENTER to confirm.")
                stdscr.refresh()
                key = stdscr.getch()  # Capture user input

                # Handle weapon selection navigation
                if key == curses.KEY_UP and count > 0:
                    count -= 1  # Move up in the list
                elif key == curses.KEY_DOWN and count < len(weapons) - 1:
                    count += 1  # Move down in the list
                elif key == curses.KEY_ENTER or key in [10, 13]:  # Confirm selection (ENTER key)
                    selected_weapon = weapons[count]  # Set the selected weapon
                    select_message = f"You selected the {selected_weapon.get_name()} to fight {enemy.get_name()}."
        else: 
            # If no weapons are available, use unarmed attack
            selected_weapon = None  # No weapon selected, unarmed attack
            select_message = f"{character.name} has no weapons! Fighting unarmed...\n"

        # Show the selected weapon and confirm
        stdscr.clear()
        stdscr.addstr(0, 0, select_message)
        stdscr.addstr(1, 0, "Press any key to continue to the fight...")
        stdscr.refresh()
        stdscr.nodelay(False)  # Disable non-blocking mode to wait for key press
        stdscr.getch()  # Wait for key press

        # Character attacks
        stdscr.clear()
        if not selected_weapon:
            damage = 5
            attack_message = f"{character.name} attacks unarmed and deals {damage} damage!\n"
        elif any(weakness['weakness'] == selected_weapon for weakness in enemy.weaknesses):
            damage = selected_weapon.damage  # Apply bonus damage for weapon weakness
            attack_message = f"{character.name} uses {selected_weapon.get_name()} and deals {damage} damage!\n"
        else:
            damage = 10  # Default damage if not using a specific weapon or no weaknesses
            attack_message = f"{character.name} uses {selected_weapon.get_name()} and deals {damage} damage!\n"            
        
        enemy.take_damage(damage)  # Deal damage to the enemy
        stdscr.addstr(0, 0, attack_message)
        stdscr.addstr(1, 0, f"{enemy.name} has {enemy.get_health()} health left.\n")
        stdscr.refresh()

        # Check if enemy is defeated
        if not enemy.is_alive():
            stdscr.addstr(2, 0, f"{enemy.name} has been defeated!\n")
            stdscr.refresh()
            stdscr.getch()  # Wait for user input to exit
            return "win"  # Return "win" if the enemy is defeated

        # Enemy attacks the character
        stdscr.addstr(3, 0, f"{enemy.name} attacks {character.name}!\n")
        character.take_damage(character_specific_damage[character.get_name()])
        stdscr.addstr(4, 0, f"{character.name} has {character.get_health()} health left.\n")
        stdscr.refresh()

        # Check if character is defeated
        if not character.is_alive():
            stdscr.addstr(5, 0, f"{character.name} has been defeated!\n")
            stdscr.addstr(7, 0, f"GAME OVER...")
            stdscr.refresh()
            stdscr.getch()  # Wait for user input to exit
            return "lose"  # Return "lose" if the character is defeated

        stdscr.addstr(6, 0, "Press any key to continue the fight...\n")
        stdscr.refresh()
        stdscr.getch()  # Wait for key press to continue the fight
