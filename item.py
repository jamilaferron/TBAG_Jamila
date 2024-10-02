class Item():
  def __init__(self, item_name, item_desc, item_type):
    self.name = item_name
    self.description = item_desc
    self.type = item_type

  def get_name(self):
    return self.name
  
  def set_name(self, item_name):
    self.name = item_name
    
  def get_description(self):
    return self.description
  
  def set_description(self, item_description):
    self.description = item_description

  def get_type(self):
    return self.type

  def set_type(self, item_type):
    self.type = item_type
  
class Weapon(Item):
  def __init__(self, item_name, item_desc, damage, effect, durability, category):
    super().__init__(item_name, item_desc, 'weapon')
    self.damage = damage
    self.effect = effect
    self.durability = durability
    self.category = category

class Gift(Item):
  def __init__(self, item_name, item_desc):
    super().__init__(item_name, item_desc, 'gift')

class Potion(Item):
  def __init__(self, item_name, item_desc):
    super().__init__(item_name, item_desc, 'gift')
  
