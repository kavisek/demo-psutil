import curses
import psutil

def setup_colors():
    # Initialize color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green on black
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Red on black

def draw_bars(win, core_data):
    win.clear()
    h, w = win.getmaxyx()
    for i, usage in enumerate(core_data):
        bar_length = int((usage / 100.0) * (w - 20))
        # Decide color based on usage
        color = 1 if usage < 50 else 2
        bar = '█' * bar_length + '-' * (w - 20 - bar_length)
        # Print each core's usage with appropriate color
        win.addstr(i, 0, f"Core {i+1} — Efficiency: [", curses.color_pair(color))
        win.addstr(bar, curses.color_pair(color))
        win.addstr(f"] {usage:5.1f}%")
    win.refresh()

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    setup_colors()
    stdscr.nodelay(True)  # Make getkey non-blocking
    while True:
        if stdscr.getch() == ord('q'):  # Press 'q' to quit
            break
        core_data = psutil.cpu_percent(interval=1, percpu=True)
        draw_bars(stdscr, core_data)

if __name__ == "__main__":
    curses.wrapper(main)
