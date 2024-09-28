class Character():
  def __init__(self, char_name, char_description):
    self.name = char_name
    self.description = char_description
    self.conversation = None

  def get_name(self):
    return self.name
  
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

  def set_weakness(self, item_weakness):
    self.weakness = item_weakness

  def get_weakness(self):
    return self.weakness
  
  def fight(self, combat_item):
    if combat_item == self.weakness:
      print("You fend " + self.name + " off with the " + combat_item )
      return True
    else:
      print(self.name + " crushes you, puny adventurer")
      return False