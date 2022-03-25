class Armor:
  def __init__(self, name = None, armor_defense = 0, magic_defense = 0):
    self.name = name
    self.armor_defense = armor_defense
    self.magic_defense = magic_defense

  def defense_value(self):
    return self.armor_defense + self.magic_defense
