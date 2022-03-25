import curses

def keyhandler(user_input):
  if (user_input == 'Q'):
    curses.echo()
    return False