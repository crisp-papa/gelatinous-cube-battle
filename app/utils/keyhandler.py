import curses
import __main__

class Keyhandler():
  def __init__(self, character, database, displays):
    self.character = character
    self.database = database
    self.game_log = displays['game_log']
    self.stdscr = displays['stdscr']

  def process_input(self, user_input):
    if (user_input == 'Q'):
      # Purge character from database?
      curses.echo()
      return False, 

    if (user_input == 'S'):
      # Save character to database
      self.game_log.addstr(1, 1, 'Really Save? Y/N')
      self.game_log.refresh()
      user_input = self.stdscr.getkey()

      if (user_input == 'Y'):
        self.database.save_character_data(self.character)
        curses.echo()
        return False
      else:

        return True
