import curses
from motor import Motor

class Manual(Motor):
    def __init__(self):
        super().__init__()
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)

    def drive(self):
        try:
            while True:
                char = self.screen.getch()
                if char == ord('q'):
                    print('Manual Drive Disabled')
                    print("Press 'a' for Automatic, 'm' for Manual and 'q' to quit")
                    break
                # Drive Forward
                if char == curses.KEY_UP:
                    self.start()
                    self.forward(v=1)
                # Drive Backward
                elif char == curses.KEY_DOWN:
                    self.start()
                    self.backward(v=1)
                # Turn Right
                elif char == curses.KEY_RIGHT:
                    self.start()
                    self.right(v=1)
                # Turn Left
                elif char == curses.KEY_LEFT:
                    self.start()
                    self.left(v=1)
                # Stop
                elif char == 10:
                    self.stop(v=1)
                # Rotate CW
                elif char == curses.KEY_PPAGE:
                    self.start()
                    self.rotate_cw(v=1)
                # Rotate CCW
                elif char == curses.KEY_NPAGE:
                    self.start()
                    self.rotate_ccw(v=1)
        except:
            curses.nocbreak()
            self.screen.keypad(0)
            curses.echo()
            curses.endwin()
            raise

'''if __name__ == '__main__':
    manual = Manual()
    manual.drive()'''