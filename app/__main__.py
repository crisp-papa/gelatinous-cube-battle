from app.models.actor import Actor
from app.models.weapon import Weapon
from app.models.armor import Armor
from app.utils.screen import Screen
from app.client.database import Database

def game_loop():
  while (True):
    screen = Screen()
    # screen.clear()

    screen.render('A battle emerges..\n')
    screen.display_actor_info(character)
    input('')

def parse_command_line_arguments():
  import argparse

  parser = argparse.ArgumentParser()

  parser.add_argument('--database_host', help='Database host address')
  parser.add_argument('--database_port', help='Database port')
  parser.add_argument('--database_username', help='Database username')
  parser.add_argument('--database_password', help='Database password')

  return parser.parse_args()

if __name__ == '__main__':
  cli = parse_command_line_arguments()
  database = Database(host=cli.database_host, port=cli.database_port, username=cli.database_username, password=cli.database_password)
  weap = database.get_weapon_by_id(2)
  print(weap)
  weapon = Weapon()
  armor = Armor()
  character = Actor(weapon=weapon, armor=armor)
  game_loop()