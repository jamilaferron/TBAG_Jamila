import random

class Room():
  def __init__(self, room_name):
    self.name = room_name
    self.description = None
    self.linked_rooms = {}
    self.enemy = None
    self.friend = None
    self.item = None
    self.inhabitant = None
 
  
  def get_name(self):
    return self.name
  
  def set_name(self, room_name):
    self.name = room_name
    
  def get_description(self):
    return self.description
  
  def set_description(self, room_description):
    self.description = room_description
  
  def describe(self):
    print(self.description)
  
  def link_room(self, room_to_link, direction):
    self.linked_rooms[direction] = room_to_link
    
    # Automatically link the opposite direction
    opposite_directions = {
        "north": "south",
        "south": "north",
        "east": "west",
        "west": "east"
    }
    room_to_link.linked_rooms[opposite_directions[direction]] = self

  
  def get_linked_rooms(self):
    return self.linked_rooms
    

  def get_details(self):
    # Basic details about the room
    string = f"You are in the {self.name}\n--------------------------------------------- \n{self.description}\n"
    
    # Include directions to linked rooms
    if self.linked_rooms:
        string += "You can go to:\n"
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            string += f"The {room.get_name()} which is to the {direction}\n"
    
    return string
      
  def move(self, direction):
    if direction in self.linked_rooms:
        return self.linked_rooms[direction]
    else:
        print("You can't go that way")
        return self
    
  def set_enemy(self, new_enemy):
    self.enemy = new_enemy

  def get_enemy(self):
    return self.enemy
  
  def set_friend(self, new_friend):
    self.friend = new_friend

  def get_friend(self):
    return self.friend
  
  def set_inhabitant(self, new_inhabitant):
    self.inhabitant = new_inhabitant

  def get_inhabitant(self):
    return self.inhabitant
  
  def set_item(self, new_item):
    self.item = new_item
    return self.item

  def get_item(self):
    return self.item
