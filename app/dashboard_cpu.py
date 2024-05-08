import curses
import psutil

def draw_bars(win, core_data):
    win.clear()
    h, w = win.getmaxyx()
    for i, usage in enumerate(core_data):
        bar_length = int((usage / 100.0) * (w - 20))
        bar = '█' * bar_length + '-' * (w - 20 - bar_length)
        win.addstr(i, 0, f"Core {i+1} — Efficiency: [{bar}] {usage}%")
    win.refresh()

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(True)  # Make getkey non-blocking
    while True:
        if stdscr.getch() == ord('q'):  # Press 'q' to quit
            break
        core_data = psutil.cpu_percent(interval=1, percpu=True)
        draw_bars(stdscr, core_data)

if __name__ == "__main__":
    curses.wrapper(main)
