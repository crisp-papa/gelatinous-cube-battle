from os import system, name

class Screen:
  def clear(self):
    system('clear') if name == 'posix' else system('cls')
  
  def display_player_info(self, player):
    print(f'{player.name}, a level {player.level} {player.character_class}')
    print(f'Health: {player.current_hp}/{player.max_hp}')
    print(f'Weapon: {player.weapon.name}')
    print(f'Armor: {player.armor.name}')

  def render(self, *display):
    for item in display:
      print(f'{item}')
      