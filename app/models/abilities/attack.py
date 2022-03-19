from app.models.actor import Actor
from app.utils import die_roll

class Attack():
  def __init__(
      self, 
      name = '(A)ttack'
    ):
    self.name = name
    self.keypress = 'A'

  def action(self, assailant: Actor, defender: Actor):
    hit = die_roll(maximum=20)

    if (hit + assailant.hit_modifier >= defender.dodge):
      damage = die_roll(minimum=assailant.weapon.min_damage, maximum=assailant.weapon.max_damage)
      damage = damage - defender.armor.defense_value()
      if damage > 0:
        defender.hitpoint_current -= damage
        print(f'{assailant.name} hit {defender.name} with their {assailant.weapon.name} for {damage} damage!!')
      else:
        print(f'{assailant.name} wrought no damage.')
    else:
      print(f'{assailant.name} missed...')
  