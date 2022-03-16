class Weapon:
  def __init__(
      self, 
      name = 'Short Sword', 
      min_damage = 1,
      max_damage = 4,
      damage_type = 'Slashing'
    ):
    self.name = name
    self.min_damage = min_damage
    self.max_damage = max_damage
    self.type = damage_type
