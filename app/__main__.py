from app.models.actor import Actor
from app.models.character_class import CharacterClass
from app.models.weapon import Weapon
from app.models.armor import Armor
from app.models.abilities.attack import Attack
from app.utils.screen import Screen
from app.client.database import Database

from app.utils import die_roll

def game_loop():
  while (character.hitpoint_current > 0 and enemy.hitpoint_current > 0):
    screen = Screen()
    screen.clear()

    screen.render('A battle emerges..\n')

    screen.display_actor_info(character)
    screen.display_menu(character)
    screen.display_actor_info(enemy)

    keypress = input('What is thy bidding? ')
    command(keypress)
    enemy_response()

    input('Press enter to continue...')
  
  if (character.hitpoint_current > 0):
    print(f'{character.name} defeated {enemy.name}!!')
    return
  
  if (enemy.hitpoint_current > 0):
    print(f'{enemy.name} defeated {character.name}!!')


def command(keypress):
  for ability in character.abilities:
    if (ability.keypress == keypress):
      ability.action(character, enemy)

def enemy_response():
  ability = enemy.abilities[die_roll(0, len(enemy.abilities) - 1)]
  ability.action(enemy, character)

def parse_command_line_arguments():
  import argparse

  parser = argparse.ArgumentParser()

  parser.add_argument('--database_host', help='Database host address')
  parser.add_argument('--database_port', help='Database port')
  parser.add_argument('--database_username', help='Database username')
  parser.add_argument('--database_password', help='Database password')

  return parser.parse_args()

def battle_setup():
  random_weapon = database.get_weapon_by_id(die_roll(1, 3))
  character = Actor(
    weapon=Weapon(
      name=random_weapon['name'],
      min_damage=random_weapon['min_damage'],
      max_damage=random_weapon['max_damage'],
      attack_speed=random_weapon['attack_speed'],
    ),
    armor=Armor(),
    abilities=[Attack()]
  )

  random_enemy = database.get_enemy_by_id(die_roll(1, 3))
  random_enemy_weapon = database.get_weapon_by_id(die_roll(1, 3))
  random_enemy_class = database.get_character_class_by_id(random_enemy['character_class_id'])
  enemy = Actor(
    name = random_enemy['name'],
    character_class=CharacterClass(name=random_enemy_class['name']),
    hitpoint_current=random_enemy['hitpoint_current'],
    hitpoint_max=random_enemy['hitpoint_max'],
    hit_modifier=random_enemy['hit_modifier'],
    weapon=Weapon(
      name=random_enemy_weapon['name'],
      min_damage=random_enemy_weapon['min_damage'],
      max_damage=random_enemy_weapon['max_damage'],
      attack_speed=random_enemy_weapon['attack_speed'],
    ),
    armor=Armor(),
    abilities=[Attack()]
  )
  return (character, enemy)

if __name__ == '__main__':
  cli = parse_command_line_arguments()
  database = Database(host=cli.database_host, port=cli.database_port, username=cli.database_username, password=cli.database_password)
  
  character, enemy = battle_setup()
  game_loop()