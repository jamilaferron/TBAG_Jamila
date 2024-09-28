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