from door import print_door, print_open_door

class Room():
  def __init__(self, room_name):
    self.name = room_name
    self.description = None
    self.linked_rooms = {}
    self.character = None
    self.item = None
 
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
  
  def link_room(self, room_to_link, direction, is_locked):
    opposite_direction = {
      "north": "south",
      "south": "north",
      "east": "west",
      "west": "east"
    }

    self.linked_rooms[direction] = {"room": room_to_link, "locked": is_locked}
    room_to_link.linked_rooms[opposite_direction[direction]] = {"room": self, "locked": is_locked}
 
  def get_linked_rooms(self):
    return self.linked_rooms
    
  def get_details(self):
    print("")
    print(f"You are in the {self.name}")
    print("-----------------------------------------------")
    print(self.description)
    for direction in self.linked_rooms:
      room = self.linked_rooms[direction]["room"]
      print(f"The {room.get_name()} is {direction}")
      
  def move(self, direction, inventory):
    opposite_direction = {
      "north": "south",
      "south": "north",
      "east": "west",
      "west": "east"
    }

    if direction in self.linked_rooms:
      if self.linked_rooms[direction]['locked']:
        print("You have found a locked dook.")
        print_door(8, 7)
        should_unlock = input("Try to unlock [y]es [n]o ").lower()

        if should_unlock == "y" and any(item.name == "key" for item in inventory):
            print("You used the key! The door swings open.")
            print_open_door(8, 7)
            self.linked_rooms[direction]['locked'] = False
            self.linked_rooms[direction]['room'].linked_rooms[opposite_direction[direction]]['locked'] = False
            return self.linked_rooms[direction]['room']
        elif should_unlock == "y" and not any(item.name == "key" for item in inventory):
            print("You don't have a key! Find one to unlock this door.")
            return self
        else:
            print("You decided to stay in the current room.")
            return self
      else:
        return self.linked_rooms[direction]['room']
    else:
        print("You can't go that way")
        return self
    
  def set_character(self, new_character):
    self.character = new_character

  def get_character(self):
    return self.character
  
  def set_item(self, new_item):
    self.item = new_item
    return self.item

  def get_item(self):
    return self.item