from app.models.player import Player
from app.models.weapon import Weapon
from app.models.armor import Armor
from app.utils.screen import Screen


short_sword = Weapon()
leather_armor = Armor()
character = Player(weapon=short_sword, armor=leather_armor)

screen = Screen()
screen.clear()
screen.render('A battle emerges..\n')
screen.display_player_info(character)