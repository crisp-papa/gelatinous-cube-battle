from app.models.armor import Armor
from app.models.weapon import Weapon
from app.models.abilities.attack import Attack


class Actor:
  def __init__(
      self, 
      name = 'Wanderer', 
      character_class = 'Soldier', 
      hitpoint_max = 20,
      hitpoint_current = 20,
      hit_modifier = 10,
      level = 1,
      weapon = Weapon(),
      armor = Armor(),
      abilities = [ Attack() ]
    ):
    self.name = name
    self.character_class = character_class
    self.hitpoint_max = hitpoint_max
    self.hitpoint_current = hitpoint_current
    self.hit_modifier = hit_modifier
    self.level = level
    self.weapon = weapon
    self.armor = armor
    # prototypes
    self.abilities = abilities