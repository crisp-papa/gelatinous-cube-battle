import curses
from app.utils.display_utils import DisplayUtils
from app.utils.keyhandler import keyhandler

def main(stdscr, character, database):
  STDSCR_WIDTH = 100
  STDSCR_HEIGHT = 24
  stdscr.resize(STDSCR_HEIGHT, STDSCR_WIDTH)
  display_utils = DisplayUtils()

  while (True):
    # Clear screen
    stdscr.clear()
    stdscr.box()

    # Subtracting 2 from these values to account for the border of the window
    game_panel_height = STDSCR_HEIGHT - 2
    game_panel_width = int(STDSCR_WIDTH * .64 - 2)
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
    display_panel_height = STDSCR_HEIGHT
    display_panel_width = STDSCR_WIDTH - game_panel_width
    display_panel_y = 0
    display_panel_x = STDSCR_WIDTH - display_panel_width

    display_panel = curses.newwin(
      display_panel_height,
      display_panel_width,
      display_panel_y,
      display_panel_x
    )
    display_panel.box()
    display_panel.overlay(stdscr)

      # Display game log within panel, should probably be a function
    game_log_height = display_panel_height // 2 + 4
    game_log_width = display_panel_width
    game_log_y = display_panel_y
    game_log_x = display_panel_x
    game_log_display = curses.newwin(
      game_log_height,
      game_log_width,
      game_log_y,
      game_log_x
    )

    for index, info_string in enumerate(['Thy smash a key!!', "Thine key hath been smashed!!", "Game log will go here eventually!!"]):
      game_log_display.addstr(index + 1, 1, info_string)

    game_log_display.border(0, 0, curses.ACS_HLINE)
    game_log_display.overlay(stdscr)
    
    # Display character info within panel, should probably be a function
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

    for index, info_string in enumerate(display_utils.build_actor_info(character, True)):
      character_info_display.addstr(index + 1, 1, info_string)

    character_info_display.overlay(stdscr)

    stdscr.refresh()

    user_input = stdscr.getkey()
    return keyhandler(user_input)
