class Character():
  def __init__(self, char_name, char_description):
    self.name = char_name
    self.description = char_description
    self.conversation = None

  def get_name(self):
    return self.name
  
  def describe(self):
    string = f"{self.name} is in this room! \n {self.description}"
    return string

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

class Protagonist(Character):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.abilities = []
    self.weaknesses = []
    self.inventory = []
    self.health = 50

  def set_abilities(self, abilities):
    self.abilities.extend(abilities) 

  def get_abilities(self):
    return self.abilities
  
  def set_weaknesses(self, weaknesses):
    self.weaknesses.extend(weaknesses)
  
  def get_weaknesses(self):
    return self.weaknesses

  def get_inventory(self):
    return self.inventory
  
  def set_inventory(self, inventory):
    self.inventory.extend(inventory)

  def set_hp(self, new_hp):
    self.hp = new_hp

  def get_health(self):
    return self.health
  
  def take_damage(self, amount):
    self.health -= amount
  
  def is_alive(self):
    return self.health > 0
    
class Enemy(Character):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.weaknesses = []
    self.attack = None
    self.health = 50
    

  def set_weaknesses(self, weaknesses):
    self.weaknesses.extend(weaknesses)
  
  def get_weaknesses(self):
    return self.weaknesses
  
  def set_attack(self, attack):
    self.attack = attack
  
  def get_attack(self):
    return self.attack
  
  def fight(self, combat_item):
    if combat_item == self.weakness:
      return True
    else:
      return False
    
  def set_hp(self, new_hp):
    self.hp = new_hp

  def get_health(self):
    return self.health
  
  def take_damage(self, amount):
        self.health -= amount
 
  def is_alive(self):
    return self.health > 0

    
class Friend(Character):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.gift = None

  def set_gift(self, item_gift):
    self.gift = item_gift

  def get_gift(self):
    return self.gift
  
  def accept_gift(self, gift_item):
    if gift_item == self.gift:
      return True
    else:
      return False
