from room import Room
from character import Enemy, Friend, Protagonist
from item import Gift, Potion, Weapon

elowen = Protagonist("Elowen the Wanderer", "A curious forest elf who has a natural affinity for the flora and fauna of the land. Her main strength lies in her ability to communicate with animals and harness nature's magic for defense and healing.")
finnian = Protagonist("Finnian the Tinkerer", "A half-gnome inventor known for his clever contraptions. Finnian is an adventurous soul who uses gadgets and wit to solve puzzles, avoid traps, and defeat enemies. He's always looking for rare materials to upgrade his inventions.")
lyra = Protagonist("Lyra the Lightbringer", "A human with a mysterious past, destined to control the powers of light and shadow. She can manipulate light to create illusions or guide her path through dark caverns. Her true power is yet to be fully unlocked, and part of her journey is about discovering it.")
thorn = Protagonist("Thorn the Beastmaster", "A mischievous fae with a bond to the spirit of wild creatures. Thorn has the ability to summon beasts to fight alongside him or to assist in tricky situations. He is small in stature but fierce in spirit.")

elowen.set_abilities(["Nature Magic", "Stealth"])
finnian.set_abilities(["Invention", "Mechanical Expertise"])
lyra.set_abilities(["Light Manipulation", "Shadow Control"])
thorn.set_abilities(["Creature Summoning", "Animal Communication"])

elowen.set_weaknesses(["Corrupted Seed", "Tainted Water"])
finnian.set_weaknesses(["Jinxed Tool ", "Rusty Invention"])
lyra.set_weaknesses(["Cursed Amulet", "Dark Crystal"])
thorn.set_weaknesses(["Beast Tamer's Collar", "Enchanted Whistle"])

CATEGORIES = {
    "light": "Light-based",
    "fire": "Fire-based",
    "physical": "Physical",
    "magical": "Magical",
    "electrical": "Electrical",
    "shadow": "Shadow-based"
}

sunstone_staff = Weapon('Sunstone Staff', 'A staff made from a sunstone, glowing with radiant light. It can channel healing energy and repel dark forces.', 25, "heals allies for 10 HP per hit", 75, CATEGORIES["light"] )
flamebloom_amulet = Weapon("Flamebloom Amulet", 'A pendant adorned with a fiery red flower, granting Elowen the power to control flames.', 25, 'Creates a fiery aura around Elowen, dealing 5 damage to nearby enemies', 50 ,CATEGORIES["fire"])
shock_grenade = Weapon("Shock Grenade", 'A throwable device that explodes upon impact, releasing a shockwave that stuns enemies.', 35, 'Stuns enemies in a small area for 2 turns.', 20, CATEGORIES["light"])
shadowflare_orb = Weapon("Shadowflare Orb", 'A dark orb that can be thrown at enemies, releasing a wave of shadow energy.', 30, 'Creates a burst of shadow energy that deals damage to enemies and blinds them.', 25, CATEGORIES["shadow"])

possible_items = [
    Weapon("Iron Sword", 'A staff made from a sunstone, glowing with radiant light. It can channel healing energy and repel dark forces.', 25, "heals allies for 10 HP per hit", 75, CATEGORIES["light"] ),
    Weapon("Wooden Bow", 'A staff made from a sunstone, glowing with radiant light. It can channel healing energy and repel dark forces.', 25, "heals allies for 10 HP per hit", 75, CATEGORIES["light"] ),
    Potion("Lesser Healing Potion", "Healing Potion"),
    Potion("Mana Elixir", "Mana elixer"),
    Gift("Mystic Feather", "feather"),
]

elowen.set_inventory([sunstone_staff, flamebloom_amulet, shock_grenade])
finnian.set_inventory([shock_grenade])
lyra.set_inventory([shadowflare_orb])

elder_grove = Room("Elder Willowroot's Grove")
elder_grove.set_description("A majestic grove dominated by the ancient Elder Willowroot tree, a wise guardian of the forest.")

glade = Room("The Glade")
glade.set_description("A peaceful clearing filled with soft grass and surrounded by tall trees.")

fairy_ring = Room("Fairy Ring")
fairy_ring.set_description("A circle of mushrooms said to be a gathering place for faeries.")

moonlit_stream = Room("Moonlit Stream")
moonlit_stream.set_description("A tranquil stream reflecting the light of the moon, creating a magical atmosphere.")

mushroom_grove = Room("Mushroom Grove")
mushroom_grove.set_description("A grove filled with vibrant, oversized mushrooms of all colors.")

darkened_thicket = Room("Darkened Thicket")
darkened_thicket.set_description("A shadowy part of the forest where the light struggles to penetrate, home to mysterious creatures.")

glimmering_stream = Room("Glimmering Stream")
glimmering_stream.set_description("A sparkling stream filled with crystal-clear water, where small fish dart playfully.")

whispering_meadow = Room("Whispering Meadow")
whispering_meadow.set_description("A serene meadow where the whispers of the wind carry secrets of the forest.")

hidden_fae_village = Room("Hidden Fae Village")
hidden_fae_village.set_description("A magical village concealed by illusion, where the fae gather and share their wisdom.")

ruins_of_temple = Room("Ruins of the Lost Temple")
ruins_of_temple.set_description("Ancient, crumbling structures that hint at a time when magic was worshiped.")

elder_grove.link_room(glade, "south")
glade.link_room(fairy_ring, "east") 
fairy_ring.link_room(moonlit_stream, "south")
moonlit_stream.link_room(mushroom_grove, "east")
mushroom_grove.link_room(darkened_thicket, "south")
mushroom_grove.link_room(whispering_meadow, "east")
darkened_thicket.link_room(glimmering_stream, "east")
glimmering_stream.link_room(whispering_meadow, "north")
whispering_meadow.link_room(hidden_fae_village, "east")
hidden_fae_village.link_room(ruins_of_temple, "north")

blightwalker = Enemy("The Blightwalker", "A towering figure of rot and ruin, spreading decay wherever it treads. It corrupts the forests and poisons the waters, making Elowen's nature magic weaker in its presence.")
blightwalker.set_weaknesses([{"weakness": sunstone_staff, "damage": 40}, {"weakness": flamebloom_amulet, "damage": 40}, {"weakness": shadowflare_orb, "damage": 30}])
blightwalker.set_attack({"attack": "corrupting touch", "damage": 15})
darkened_thicket.set_enemy(blightwalker)
elder_grove.set_enemy(blightwalker)

sentinel = Enemy("Ironclad Sentinels", "The Ironclad Sentinel, is a remnant of an ancient civilization, fit perfectly in the crumbling ruins of the Lost Temple, guarding its secrets.")
sentinel.set_weaknesses([{"weakness": shock_grenade, "damage": 10}])
sentinel.set_attack({"attack": "heavy melee strike", "damage": 12})
ruins_of_temple.set_enemy(sentinel)

saboteur = Enemy("The Blightwalker", "A sly mage who specializes in short-circuiting any mechanical or technological devices Finnian might deploy in battle.")
saboteur.set_weaknesses([{"weakness": sunstone_staff, "damage": 15}])
saboteur.set_attack({"attack": "magical disruption", "damage": 10})
hidden_fae_village.set_enemy(saboteur)


willowroot = Friend("Elder Willowroot","A wise, ancient talking tree who has deep knowledge of the forest and its history. Often gives guidance to adventurers and protects the balance of nature.")
elder_grove.set_friend(willowroot)

sylas = Friend("Sylas the Herbalist","A friendly gnome who specializes in potion-making. He provides players with herbal remedies and teaches them about the local flora, offering quests to gather rare herbs.")
glade.set_friend(sylas)

fayla = Friend("Fayla the Mischief Maker", "A playful fae who loves riddles and tricks. She offers challenges to the player and rewards them with enchanted items if they succeed in her games.")
fairy_ring.set_friend(fayla)

nymia = Friend("Nymia the Water Spirit", "A serene spirit who resides in the stream. She grants players temporary water-related abilities or offers quests to cleanse the stream of impurities.")
moonlit_stream.set_friend(nymia)

milo = Friend("Milo the Mushroom Sage", "A wise old mushroom creature who provides players with knowledge about the various fungi in the grove. He can guide players in finding rare mushrooms for crafting.")
mushroom_grove.set_friend(milo)

villager = Friend("Hidden Fae Villager","A secretive group of forest fae who live in an isolated village. They're not often seen by outsiders, but if found, they can offer magical assistance or warn of dangers in the forest.")
hidden_fae_village.set_friend(villager)

bogart = Friend("Bogart the Trickster ","A mischievous shape-shifting goblin who enjoys playing pranks on travelers. He guards some secrets of the lost temple but is not inherently evil—just tricky to deal with.")
ruins_of_temple.set_friend(bogart)

character_specific_damage = {
    "Elowen the Wanderer": 5,  # Resistant to decay
    "Finnian the Tinkerer": 10,  # Vulnerable to decay
    "Lyra the Lightbringer": 12,  # Weak against decay
    "Thorn the Beastmaster": 20  # Neutral damage (example value)
}