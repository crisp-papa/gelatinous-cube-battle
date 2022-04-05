import curses
import __main__
import app.utils.constants as Constants

class Keyhandler():
  def __init__(self, character, database, displays):
    self.character = character
    self.database = database
    self.stdscr = displays.get('stdscr', None)
    self.game_panel = displays.get('game_panel', None)
    self.display_panel = displays.get('display_panel', None)
    self.game_log = displays.get('game_log', None)
    self.character_info = displays.get('character_info', None)

  def process_input(self, user_input):
    if (user_input == 'Q'):
      # Purge character from database?
      curses.echo()
      return False

    if (user_input == 'S'):
      # Save character to database
      message = 'Really Save? Y/N'
      upper, left = self.stdscr.getbegyx()
      min_y, min_x = int(upper + (Constants.STDSCR_HEIGHT * .2)), int(left + (Constants.STDSCR_WIDTH * .2))
      max_y, max_x = Constants.STDSCR_HEIGHT - min_y, Constants.STDSCR_WIDTH - min_x
      pad_height, pad_width = max_y - min_y, max_x - min_x
      message_y, message_x = int(pad_height * .5) - 1, int(pad_width * .5) - int(len(message) * .5) - 1
      pad = curses.newpad(pad_height, pad_width)
      pad.box()
      pad.addstr(message_y, message_x, message)
      pad.refresh(upper, left, min_y, min_x, max_y, max_x)

      user_input = self.stdscr.getkey()

      if (user_input == 'Y'):
        self.database.save_character_data(self.character)
        curses.echo()
        return False
      else:
        return True
