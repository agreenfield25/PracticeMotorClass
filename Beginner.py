# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Motor:

    def __init__(self):
        self.speed = .5
        # set speed immediately

    def set_speed(self, speed):
        self.speed = speed
        # define speed

    def speed_up(self):
        self.speed = self.speed * 2

        # double the variable speed

    def slow_down(self):
        self.speed = self.speed / 2

        # half the variable speed
