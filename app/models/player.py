class Player:
  def __init__(
      self, 
      name = 'Wanderer', 
      character_class = 'Soldier', 
      max_hp = 20,
      current_hp = 20,
      to_hit = 10,
      level = 1,
      weapon = None,
      armor = None
    ):
    self.name = name
    self.character_class = character_class
    self.max_hp = max_hp
    self.current_hp = current_hp
    self.to_hit = to_hit
    self.level = level
    self.weapon = weapon
    self.armor = armor