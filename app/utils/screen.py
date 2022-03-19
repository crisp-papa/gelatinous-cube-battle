from os import system, name

class Screen:
  def clear(self):
    system('clear') if name == 'posix' else system('cls')
  
  def display_actor_info(self, actor, verbose=False):
    print(f'{actor.name}, a level {actor.level} {actor.character_class.name}')
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
    
  def side_by_side(strings, size=30, space=4):
    strings = list(strings)
    result = []

    while any(strings):
        line = []

        for i, s in enumerate(strings):
            line.append(s[:size].ljust(size))
            strings[i] = s[size:]

        result.append((" " * space).join(line))
    
    return "\n".join(result)