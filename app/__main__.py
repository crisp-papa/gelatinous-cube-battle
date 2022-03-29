from app.models.actor import Actor
from app.models.character_class import CharacterClass
from app.models.weapon import Weapon
from app.models.armor import Armor
from app.models.abilities.attack import Attack
from app.utils.display_utils import DisplayUtils
from app.client.database import Database
from app.client.curses import CursesClient

from app.utils import die_roll
import curses

def parse_command_line_arguments():
  import argparse

  parser = argparse.ArgumentParser()

  parser.add_argument('--database_host', help='Database host address')
  parser.add_argument('--database_port', help='Database port')
  parser.add_argument('--database_username', help='Database username')
  parser.add_argument('--database_password', help='Database password')

  return parser.parse_args()

def character_setup():
  random_weapon = database.get_weapon_by_id(die_roll(1, 3))
  random_armor = database.get_armor_by_id(die_roll(1, 3))
  character = Actor(
    weapon=Weapon(
      name=random_weapon['name'],
      min_damage=random_weapon['min_damage'],
      max_damage=random_weapon['max_damage'],
      attack_speed=random_weapon['attack_speed'],
    ),
    armor=Armor(
      name=random_armor['name'],
      armor_defense=random_armor['armor_defense'],
      magic_defense=random_armor['magic_defense']
    ),
    abilities=[Attack()]
  )
  return character

if __name__ == '__main__':
  cli = parse_command_line_arguments()
  database = Database(host=cli.database_host, port=cli.database_port, username=cli.database_username, password=cli.database_password)
  character = character_setup()
  curses_client = CursesClient(character, database)

  curses.wrapper(curses_client.main)