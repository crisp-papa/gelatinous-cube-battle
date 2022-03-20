from curses import wrapper

def main(stdscr):
  # Clear screen
  stdscr.clear()
  stdscr.addstr('@')

  stdscr.refresh()
  user_input = stdscr.getkey()

  if (user_input.upper() == 'Q'):
    return

wrapper(main)
