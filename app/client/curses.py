import curses
from app.utils.display_utils import DisplayUtils
from app.utils.keyhandler import Keyhandler
import app.utils.constants as Constants

class CursesClient:
  def __init__(self, character, database):
    self.character = character
    self.database = database
    self.displays = {}

  def setup_displays(self, stdscr):
    # Subtracting 2 from these values to account for the border of the window
    game_panel_height = Constants.STDSCR_HEIGHT - 2
    game_panel_width = int(Constants.STDSCR_WIDTH * .64 - 2)
    game_panel_y = 1
    game_panel_x = 1

    game_panel = curses.newwin(
      game_panel_height,
      game_panel_width,
      game_panel_y,
      game_panel_x
    )
    game_panel.overlay(stdscr)
    

    # Display panel, essentially just the bordered window to attach other display windows to
    display_panel_height = Constants.STDSCR_HEIGHT
    display_panel_width = Constants.STDSCR_WIDTH - game_panel_width
    display_panel_y = 0
    display_panel_x = Constants.STDSCR_WIDTH - display_panel_width

    display_panel = curses.newwin(
      display_panel_height,
      display_panel_width,
      display_panel_y,
      display_panel_x
    )
    display_panel.box()
    display_panel.overlay(stdscr)
    self.displays['display_panel'] = display_panel

      # Display game log within panel
    game_log_height = display_panel_height // 2 + 4
    game_log_width = display_panel_width
    game_log_y = display_panel_y
    game_log_x = display_panel_x
    game_log_panel = curses.newwin(
      game_log_height,
      game_log_width,
      game_log_y,
      game_log_x
    )

    for index, info_string in enumerate(['Thy smash a key!!', "Thine key hath been smashed!!", "Game log will go here eventually!!"]):
      game_log_panel.addstr(index + 1, 1, info_string)

    game_log_panel.border(0, 0, curses.ACS_HLINE)
    game_log_panel.overlay(stdscr)
    self.displays['game_log'] = game_log_panel
    
    # Display character info within panel
    character_info_height = display_panel_height // 2 - 3
    character_info_width = display_panel_width
    character_info_y = display_panel_height // 2 + 3
    character_info_x = display_panel_x
    character_info_display = curses.newwin(
      character_info_height,
      character_info_width,
      character_info_y,
      character_info_x
    )

    display_utils = DisplayUtils()
    for index, info_string in enumerate(display_utils.build_actor_info(self.character, True)):
      character_info_display.addstr(index + 1, 1, info_string)

    character_info_display.overlay(stdscr)

    self.displays['stdscr'] = stdscr
    self.displays['game_panel'] = game_panel
    self.displays['display_panel'] = display_panel
    self.displays['game_log'] = game_log_panel
    self.displays['character_info'] = character_info_display

    stdscr.refresh()

  def main(self, stdscr):
    stdscr.resize(Constants.STDSCR_HEIGHT, Constants.STDSCR_WIDTH)
    stdscr.clear()
    stdscr.box()
    self.setup_displays(stdscr)
    keyhandler = Keyhandler(self.character, self.database, self.displays)

    while (True):
      user_input = stdscr.getkey()
      return keyhandler.process_input(user_input)

