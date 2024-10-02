from room import Room
from character import Protagonist
from item import Weapon

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

elder_grove = Room("Elder Willowroot's Grove")
elder_grove.set_description("A majestic grove dominated by the ancient Elder Willowroot tree, a wise guardian of the forest.")

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

elowen.set_inventory([sunstone_staff])
finnian.set_inventory([shock_grenade])
lyra.set_inventory([shadowflare_orb])

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
