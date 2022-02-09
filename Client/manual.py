import curses
from motor import Motor
car = Motor()
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

def manual_drive():
    try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                print('Quit')
                break
            # Drive Forward
            if char == curses.KEY_UP:
                car.start()
                car.forward()
            # Drive Backward
            elif char == curses.KEY_DOWN:
                car.start()
                car.backward()
            # Turn Right
            elif char == curses.KEY_RIGHT:
                car.start()
                car.right()
            # Turn Left
            elif char == curses.KEY_LEFT:
                car.start()
                car.left()
            # Stop
            elif char == 10:
                car.stop()
            # CW
            elif char == curses.KEY_PPAGE:
                car.start()
                car.rotate_cw()
            # CCW
            elif char == curses.KEY_NPAGE:
                car.start()
                car.rotate_ccw()
    finally:
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()

manual_drive()