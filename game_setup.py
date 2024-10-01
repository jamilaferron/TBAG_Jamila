from room import Room

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
