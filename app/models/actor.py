from app.models.armor import Armor
from app.models.character_class import CharacterClass
from app.models.weapon import Weapon

class Actor:
  def __init__(
      self, 
      name = 'Wanderer', 
      character_class = CharacterClass(name='Soldier'), 
      hitpoint_max = 20,
      hitpoint_current = 20,
      hit_modifier = 3,
      level = 1,
      dodge = 10,
      weapon = Weapon(),
      armor = Armor(),
      abilities = []
    ):
    self.name = name
    self.character_class = character_class
    self.hitpoint_max = hitpoint_max
    self.hitpoint_current = hitpoint_current
    self.hit_modifier = hit_modifier
    self.level = level
    self.weapon = weapon
    self.armor = armor
    self.abilities = abilities
    # prototypes
    self.dodge = dodge
