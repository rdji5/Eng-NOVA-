import RPi.GPIO as GPIO
import time

class FutureEngineersRobot:
    def __init__(self):
        # Setup motor and servo pins
        self.IN3 = 38
        self.IN4 = 32
        self.SERVO_PIN = 33

        # Servo angles for directions
        self.STRAIGHT = 50
        self.RIGHT = 100
        self.LEFT = 10

        # Ultrasonic sensor pins and distance limits
        self.FRONT_TRIGGER = 13
        self.FRONT_ECHO = 11
        self.WALL_DISTANCE = 60
        self.MAX_DISTANCE = 200

        # Turn control variables
        self.is_turning = False
        self.turn_start_time = 0
        self.turn_duration = 1.3
        self.straight_after_turn_duration = 2.5
        self.straight_after_turn_start = 0
        self.moving_straight_after_turn = False

        # Initialize GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.SERVO_PIN, GPIO.OUT)
        self.servo_pwm = GPIO.PWM(self.SERVO_PIN, 50)
        self.servo_pwm.start(0)

        GPIO.setup(self.FRONT_TRIGGER, GPIO.OUT)
        GPIO.setup(self.FRONT_ECHO, GPIO.IN)

        # Start driving straight
        self.set_steering_angle(self.STRAIGHT)
        self.keep_moving_forward()

    def set_steering_angle(self, angle):
        # Move servo to target angle
        duty_cycle = 2.5 + (angle / 180.0) * 10
        self.servo_pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.05)
        self.servo_pwm.ChangeDutyCycle(0)

    def keep_moving_forward(self):
        # Move forward
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)

    def stop_motor(self):
        # Stop moving
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

    def measure_distance_ultra_fast(self):
        # Measure distance using ultrasonic sensor
        try:
            GPIO.output(self.FRONT_TRIGGER, False)
            time.sleep(0.001)
            GPIO.output(self.FRONT_TRIGGER, True)
            time.sleep(0.00001)
            GPIO.output(self.FRONT_TRIGGER, False)
            start_time = time.time()
            while GPIO.input(self.FRONT_ECHO) == 0:
                pulse_start = time.time()
                if pulse_start - start_time > 0.05:
                    return self.MAX_DISTANCE
            while GPIO.input(self.FRONT_ECHO) == 1:
                pulse_end = time.time()
                if pulse_end - pulse_start > 0.05:
                    return self.MAX_DISTANCE
            distance = (pulse_end - pulse_start) * 17150
            return round(distance, 1) if 2 < distance < self.MAX_DISTANCE else self.MAX_DISTANCE
        except:
            return self.MAX_DISTANCE

    def start_90_degree_turn(self):
        # Start turning left
        self.keep_moving_forward()
        self.set_steering_angle(self.LEFT)
        self.is_turning = True
        self.turn_start_time = time.time()

    def run_mission_one(self):
        try:
            time.sleep(1)
            start_time = time.time()
            while True:
                current_time = time.time()
                # Stop after 46 seconds
                if current_time - start_time >= 46:
                    self.emergency_stop()
                    break
                # Handle turning
                if self.is_turning:
                    elapsed_turn = current_time - self.turn_start_time
                    if elapsed_turn < self.turn_duration:
                        self.keep_moving_forward()
                        self.set_steering_angle(self.LEFT)
                    else:
                        self.is_turning = False
                        self.moving_straight_after_turn = True
                        self.straight_after_turn_start = current_time
                        self.set_steering_angle(self.STRAIGHT)
                # Go straight after turn
                elif self.moving_straight_after_turn:
                    elapsed_straight = current_time - self.straight_after_turn_start
                    if elapsed_straight < self.straight_after_turn_duration:
                        self.keep_moving_forward()
                        self.set_steering_angle(self.STRAIGHT)
                    else:
                        self.moving_straight_after_turn = False
                # Normal driving
                else:
                    self.keep_moving_forward()
                    distance = self.measure_distance_ultra_fast()
                    # Turn if wall detected
                    if distance <= self.WALL_DISTANCE:
                        self.start_90_degree_turn()
                    else:
                        self.set_steering_angle(self.STRAIGHT)
                time.sleep(0.05)
        except KeyboardInterrupt:
            self.emergency_stop()

    def emergency_stop(self):
        # Stop everything safely
        try:
            self.stop_motor()
            self.servo_pwm.stop()
            GPIO.cleanup()
        except:
            pass

def main():
    try:
        robot = FutureEngineersRobot()
        robot.run_mission_one()
    except:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
