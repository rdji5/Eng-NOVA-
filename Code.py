import RPi.GPIO as GPIO
import time

MOTOR_IN3, MOTOR_IN4, SERVO_PIN, TRIGGER_PIN, ECHO_PIN = 38, 32, 33, 31, 29
TARGET_DISTANCE, TOLERANCE = 22.5, 2.5
SERVO_STRAIGHT, SERVO_RIGHT, SERVO_LEFT = 50, 65, 35
MOTOR_SPEED, RUN_TIME = 40, 5.0

running = True

class WallFollowingCar:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(MOTOR_IN3, GPIO.OUT)
        GPIO.setup(MOTOR_IN4, GPIO.OUT)
        self.motor_pwm = GPIO.PWM(MOTOR_IN3, 1000)
        self.motor_pwm.start(0)
        GPIO.setup(SERVO_PIN, GPIO.OUT)
        self.servo_pwm = GPIO.PWM(SERVO_PIN, 50)
        self.servo_pwm.start(0)
        GPIO.setup(TRIGGER_PIN, GPIO.OUT)
        GPIO.setup(ECHO_PIN, GPIO.IN)
        self.set_servo_angle(SERVO_STRAIGHT)
        time.sleep(0.5)

    def measure_distance(self):
        GPIO.output(TRIGGER_PIN, False)
        time.sleep(0.000002)
        GPIO.output(TRIGGER_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIGGER_PIN, False)

        pulse_start, pulse_end = time.time(), time.time()
        timeout = time.time() + 0.1
        while GPIO.input(ECHO_PIN) == 0 and time.time() < timeout:
            pulse_start = time.time()
        timeout = time.time() + 0.1
        while GPIO.input(ECHO_PIN) == 1 and time.time() < timeout:
            pulse_end = time.time()

        distance = round((pulse_end - pulse_start) * 17150, 2)
        return max(2, min(400, distance))

    def set_servo_angle(self, angle):
        duty_cycle = 2.5 + (angle / 180.0) * 10.0
        self.servo_pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.05)

    def move_forward(self):
        GPIO.output(MOTOR_IN4, GPIO.HIGH)
        self.motor_pwm.ChangeDutyCycle(MOTOR_SPEED)

    def stop_motor(self):
        self.motor_pwm.ChangeDutyCycle(0)
        GPIO.output(MOTOR_IN3, GPIO.LOW)
        GPIO.output(MOTOR_IN4, GPIO.LOW)

    def wall_following_control(self):
        start_time = time.time()
        while running and (time.time() - start_time) < RUN_TIME:
            distance = self.measure_distance()
            error = distance - TARGET_DISTANCE
            if abs(error) <= TOLERANCE:
                self.set_servo_angle(SERVO_STRAIGHT)
            elif error < -TOLERANCE:
                self.set_servo_angle(SERVO_LEFT)
            else:
                self.set_servo_angle(SERVO_RIGHT)
            self.move_forward()
            time.sleep(0.1)

    def cleanup(self):
        global running
        running = False
        self.stop_motor()
        self.set_servo_angle(SERVO_STRAIGHT)
        time.sleep(0.5)
        self.servo_pwm.stop()
        self.motor_pwm.stop()
        GPIO.cleanup()

def main():
    car = WallFollowingCar()
    try:
        car.wall_following_control()
    finally:
        car.cleanup()

if __name__ == "__main__":
    main()
