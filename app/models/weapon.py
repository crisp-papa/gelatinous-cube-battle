class Weapon:
  def __init__(
      self, 
      name = 'Fists', 
      min_damage = 0,
      max_damage = 1,
      damage_type = 'Blunt',
      attack_speed = 5,
      hit_modifier = 3
    ):
    self.name = name
    self.min_damage = min_damage
    self.max_damage = max_damage
    self.damage_type = damage_type
    self.attack_speed = attack_speed
    self.hit_modifier = hit_modifier
