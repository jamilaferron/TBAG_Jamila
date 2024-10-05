class Character():
  def __init__(self, char_name, char_description):
    self.name = char_name
    self.description = char_description
    self.conversation = None

  def get_name(self):
    return self.name
  
  def get_description(self):
    return self.description
  
  def set_description(self, new_description):
    self.description = new_description

  def describe(self):
    print(f"{self.name} is in this room!")
    print( self.description)

  def set_conversation(self, conversation):
      self.conversation = conversation

  # Talk to this character​
  def talk(self):
    if self.conversation is not None:
      print(f"[{self.name}] says: {self.conversation}")
    else:
      print(f"{self.name} doesn't want to talk to you")

  def fight(self, combat_item):
    print(self.name + " doesn't want to fight with you")
    return True


class Enemy(Character):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.weakness = None
    self.treasure = None

  def set_weakness(self, item_weakness):
    self.weakness = item_weakness

  def get_weakness(self):
    return self.weakness
  
  def get_treasure( self):
    return self.treasure

  def set_treasure( self, treasure):
    self.treasure = treasure
  
  def fight(self, combat_item):
    if combat_item == self.weakness.get_name():
      print("You fend " + self.name + " off with the " + combat_item )
      return True
    else:
      print(self.name + " crushes you, puny adventurer")
      return False
    
  def steal_from(self):
    if self.treasure:
      print(f"You have stolen {self.name}'s {self.treasure.get_name()}" )
      return True
    else: 
      print(f"{self.name} has no treasure to steal" )
      return False
    
class Friend(Character):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.token = None

  def set_token(self, item_token):
    self.token = item_token

  def get_token(self):
    return self.token
  
  def gift(self, gifted_item):
    if gifted_item == self.token.get_name():
      print(f"I am honored by your generosity. This {gifted_item} will help me greatly!")
      return True
    else:
      print(f"You are generous, but I must decline. There are others who need a {gifted_item} more.")
      return False
  