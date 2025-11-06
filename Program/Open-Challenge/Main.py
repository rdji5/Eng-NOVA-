def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    
    GPIO.setup(MOTOR_IN3, GPIO.OUT)
    GPIO.setup(MOTOR_IN4, GPIO.OUT)
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    
    for trig in [FRONT_TRIG, RIGHT_TRIG, LEFT_TRIG]:
        GPIO.setup(trig, GPIO.OUT)
        GPIO.output(trig, False)
    
    for echo in [FRONT_ECHO, RIGHT_ECHO, LEFT_ECHO]:
        GPIO.setup(echo, GPIO.IN)

def mpu6050_init():
    try:
        bus.write_byte_data(MPU6050_ADDR, 0x6B, 0)
        time.sleep(0.1)
        return True
    except:
        return False

def motor_forward():
    GPIO.output(MOTOR_IN3, GPIO.LOW)
    GPIO.output(MOTOR_IN4, GPIO.HIGH)


def motor_stop():
    GPIO.output(MOTOR_IN3, GPIO.LOW)
    GPIO.output(MOTOR_IN4, GPIO.LOW)


def setup_servo():
    global servo_pwm
    servo_pwm = GPIO.PWM(SERVO_PIN, 50)
    servo_pwm.start(0)
    time.sleep(0.1)


def set_servo_angle(angle):
    duty = 2.5 + (angle / 180.0) * 10
    servo_pwm.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo_pwm.ChangeDutyCycle(0)


def steer_straight():
    set_servo_angle(SERVO_STRAIGHT)

def steer_left():
    set_servo_angle(SERVO_LEFT)

def steer_right():
    set_servo_angle(SERVO_RIGHT)


def get_distance(trig_pin, echo_pin):
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)


while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()
        if pulse_start - timeout > 0.1:
            return -1

while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()
        if pulse_end - pulse_start > 0.1:
            return -1


pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 1)
    
    return distance if distance < 400 else -1

def get_front_distance():
    return get_distance(FRONT_TRIG, FRONT_ECHO)

def get_right_distance():
    return get_distance(RIGHT_TRIG, RIGHT_ECHO)

def get_left_distance():
    return get_distance(LEFT_TRIG, LEFT_ECHO)


def detect_direction():
    left_readings = []
    right_readings = []
    
    for i in range(10):
        left = get_left_distance()
        right = get_right_distance()
        
        if left > 0:
            left_readings.append(left)
        if right > 0:
            right_readings.append(right)
        
        time.sleep(0.1)

avg_left = sum(left_readings) / len(left_readings) if left_readings else 0
    avg_right = sum(right_readings) / len(right_readings) if right_readings else 0


if avg_left > DIRECTION_CHECK_DISTANCE:
        return 'CCW'
    elif avg_right > DIRECTION_CHECK_DISTANCE:
        return 'CW'
    else:
        if avg_left > avg_right:
            return 'CCW'
        else:
            return 'CW'


def turn_90(turn_right):
    if turn_right:
        steer_right()
    else:
        steer_left()
    
    motor_forward()
    time.sleep(TURN_DURATION)
    steer_straight()


def navigate():
    global sections_completed, direction, running
    
    motor_forward()
    steer_straight()


while running and sections_completed < TOTAL_SECTIONS:
        front_dist = get_front_distance()
        
        if front_dist <= DETECTION_DISTANCE and front_dist > 0:
            motor_stop()


if direction is None:
                time.sleep(2)
                direction = detect_direction()
            else:
                time.sleep(0.1)


if direction == 'CW':
                turn_90(True)
            else:
                turn_90(False)


motor_forward()
            steer_straight()
            time.sleep(STRAIGHT_AFTER_TURN)
            
            sections_completed += 1


else:
            motor_forward()
            steer_straight()
        
        time.sleep(0.05)


motor_stop()
    steer_straight()
    time.sleep(0.5)
    running = False


def main():
    global running
    
    try:
        setup_gpio()
        setup_servo()
        mpu6050_init()
        time.sleep(0.5)
        
        steer_straight()
        motor_stop()
        
        running = True
        navigate()
