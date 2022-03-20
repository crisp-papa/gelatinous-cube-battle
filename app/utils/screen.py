from os import system, name

class Screen:
  def clear(self):
    system('clear') if name == 'posix' else system('cls')
  
  def build_actor_info(self, actor, verbose=False):
    actor_info = []
    actor_info.append(f'{actor.name}, a level {actor.level} {actor.character_class.name}\n')
    actor_info.append(f'Health: {actor.hitpoint_current}/{actor.hitpoint_max}\n')
    actor_info.append(f'Weapon: {actor.weapon.name}')
    
    if (verbose):
      actor_info.append(f'Hit Modifier: {actor.weapon.hit_modifier}')
      actor_info.append(f'Armor: {actor.armor.name}')
      actor_info.append(f'Armor Defense: {actor.armor.armor_defense}')
      actor_info.append(f'Magic Defense: {actor.armor.magic_defense}')

    return actor_info

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