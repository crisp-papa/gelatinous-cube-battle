from os import system, name

class Screen:
  def clear(self):
    system('clear') if name == 'posix' else system('cls')
  
  def display_actor_info(self, actor, verbose=False):
    print(f'{actor.name}, a level {actor.level} {actor.character_class}')
    print(f'Health: {actor.hitpoint_current}/{actor.hitpoint_max}')
    print(f'Weapon: {actor.weapon.name}')
    
    if (verbose):
      print(f'Hit Modifier: {actor.weapon.hit_modifier}')
      print(f'Armor: {actor.armor.name}')
      print(f'Armor Defense: {actor.armor.armor_defense}')
      print(f'Magic Defense: {actor.armor.magic_defense}')

  def render(self, *display):
    for item in display:
      print(f'{item}')
      
  def display_menu(self, character):
    for ability in character.abilities:
      print(ability.name)
    