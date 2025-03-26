import RPi.GPIO as GPIO
import time


sensor_left= 16
sensor_right= 11


GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_left, GPIO.IN)
GPIO.setup(sensor_right, GPIO.IN)




ena = 22
in1 = 24
in2 = 26

ena2 = 40
in3 = 36
in4 = 32


# Board and pin setup MOTOR 1 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ena, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)


# Board and pin setup MOTOR 2 

GPIO.setup(ena2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)


# Set all pins low to start MOTOR 1 
GPIO.output(ena, GPIO.LOW)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)


# Set all pins low to start MOTOR 2 
GPIO.output(ena2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

# Create PWM instance on enable pin A at 50 Hz
motor1 = GPIO.PWM(ena, 100)
motor2 = GPIO.PWM(ena2, 100)



def color():
    if sensor_value == 1:
        color = "white"
        movestraight()
        
    else:
        color= "black"
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        motor1.start(0)
        motor2.start(0)
        
        
def movestraight():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in4, GPIO.HIGH)

        # Start motor with 25% duty cycle
    motor1.start(39)
    motor2.start(32)



def moveright():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in4, GPIO.HIGH)

    # Start motor with 25% duty cycle
    motor1.start(0)
    motor2.start(24)

def moveleft():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    motor1.start(22)
    motor2.start(0)
   


    
# def motor():
#     if color == str("black"):
#          # Set in1 high for counter-clockwise rotation
#         GPIO.output(in1, GPIO.HIGH)

#         # Start motor with 25% duty cycle
#         motor1.start(25)
#         time.sleep(5)
#     else: 
#         motor1.stop()


try:
    while True:

        sensor_valueleft = GPIO.input(sensor_left)
        sensor_valueright = GPIO.input(sensor_right)
        if sensor_valueleft and sensor_valueright == 0:
            movestraight()
        elif sensor_valueleft == 1:
            moveleft()
        elif sensor_valueright == 1:
            moveright()


except KeyboardInterrupt:
    GPIO.cleanup()
