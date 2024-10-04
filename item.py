class Item():
  def __init__(self, item_name, item_desc):
    self.name = item_name
    self.description = item_desc

  def get_name(self):
    return self.name
  
  def set_name(self, item_name):
    self.name = item_name
    
  def get_description(self):
    return self.description
  
  def set_description(self, item_description):
    self.description = item_description

class Weapon(Item):
  def __init__(self, item_name, item_desc):
    self.name = item_name
    self.description = item_desc
    self.num_uses = 2

  def set_num_uses(self, num_uses):
    self.num_uses = num_uses
  
  def get_num_uses(self):
    return self.num_uses
  
  def set_num_uses(self, num_uses):
    self.num_uses = num_uses
  
  def reduce_num_uses(self):
    self.num_uses -= 1

