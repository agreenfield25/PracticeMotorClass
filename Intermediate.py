from Beginner import Motor


class MotorController:

    def __init__(self, list_of_motors: list[Motor]):
        self.motors = list_of_motors

    def set_speed(self, speed):
        for motor in self.motors:
            motor.set_speed(speed)

    def speedup(self):
        for bob in self.motors:
            bob.speed_up()

    def slow_down(self):
        for jill in self.motors:
            jill.slow_down()
    def add_Motor(self, motor:Motor):
        self.motors.append(motor)

    if __name__ == "main":
        motor1 = Motor()
        motor2 = Motor()
        motor3 = Motor()
