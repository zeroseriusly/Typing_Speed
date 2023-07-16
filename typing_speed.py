import curses
import time


def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

    text = "Hello!"
    typed_text = ""

    stdscr.addstr(0, 5, text)
    stdscr.refresh()
    curses.napms(1000)

    keyPress = stdscr.getkey()

    stdscr.addstr(2, 0, "Start typing:")

    start_time = time.time()

    while True:
        key = stdscr.getch()
        if key == 27:  # ESC key to exit
            break
        elif key == 10:  # Enter key to finish typing
            break
        else:
            typed_text += chr(key)
            stdscr.addstr(4, 0, typed_text)

    seconds_passed = max((time.time() - start_time), 1)
    cpm = int(len(typed_text) / (seconds_passed / 60))
    wpm = round((cpm / 5), 2)

    stdscr.addstr(5, 0, f"Typing Speed in words per minute (wpm): {wpm}")
    stdscr.addstr(6, 0, f"Typing Speed in characters per minute: {cpm}")
    stdscr.addstr(7, 0, f"Seconds elapsed: {round(seconds_passed, 2)} seconds")

    for index, letter in enumerate(typed_text):
        correct_char = text[index]
        if letter != correct_char:
            text_color = curses.color_pair(2)
        else:
            text_color = curses.color_pair(1)

        stdscr.addstr(0, index, letter, text_color)

    stdscr.getch()  # Wait for a key press before exiting


curses.wrapper(main)
