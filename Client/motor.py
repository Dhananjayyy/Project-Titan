import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

class Motor:
    def __init__(self):
        self.PWMA = 7
        self.PWMB = 40
        self.STB = 36
        self.AIN1 = 5
        self.AIN2 = 3
        self.BIN1 = 37
        self.BIN2 = 38
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.AIN1,GPIO.OUT)
        GPIO.setup(self.AIN2,GPIO.OUT)
        GPIO.setup(self.PWMA,GPIO.OUT)
        GPIO.setup(self.STB,GPIO.OUT)
        GPIO.setup(self.BIN1,GPIO.OUT)
        GPIO.setup(self.BIN2,GPIO.OUT)
        GPIO.setup(self.PWMB,GPIO.OUT)
        self.pwm = GPIO.PWM(self.PWMA,100)
        self.pwm1 = GPIO.PWM(self.PWMB, 100)
        self.pwm.start(0)
        self.pwm1.start(0)
        self.start()

    def start(self):
        GPIO.output(self.STB,True)

    def forward(self,s=60,t=0,v=0):
        self.pwm.ChangeDutyCycle(s)
        self.pwm1.ChangeDutyCycle(s)
        GPIO.output(self.AIN1,False)
        GPIO.output(self.AIN2,True)
        GPIO.output(self.BIN1,False)
        GPIO.output(self.BIN2,True)
        sleep(t)
        if v==1: print('Forward')
    
    def backward(self,s=50,t=0,v=0):
        self.pwm.ChangeDutyCycle(s)
        self.pwm1.ChangeDutyCycle(s)
        GPIO.output(self.AIN1,True)
        GPIO.output(self.AIN2,False)
        GPIO.output(self.BIN1,True)
        GPIO.output(self.BIN2,False)
        sleep(t)
        if v==1: print('Backward')
    
    def right(self,s1=50,s2=0,t=0,v=0):
        self.pwm.ChangeDutyCycle(s1)
        self.pwm1.ChangeDutyCycle(s2)
        GPIO.output(self.AIN1,False)
        GPIO.output(self.AIN2,True)
        GPIO.output(self.BIN1,False)
        GPIO.output(self.BIN2,True)
        sleep(t)
        if v==1: print('Right')

    def left(self,s1=0,s2=50,t=0,v=0):
        self.pwm.ChangeDutyCycle(s1)
        self.pwm1.ChangeDutyCycle(s2)
        GPIO.output(self.AIN1,False)
        GPIO.output(self.AIN2,True)
        GPIO.output(self.BIN1,False)
        GPIO.output(self.BIN2,True)
        sleep(t)
        if v==1: print('Left')

    def stop(self, t=0,v=0):
        GPIO.output(self.STB,False)
        self.pwm.ChangeDutyCycle(0)
        self.pwm1.ChangeDutyCycle(0)
        GPIO.output(self.AIN1,False)
        GPIO.output(self.AIN2,False)
        GPIO.output(self.BIN1,False)
        GPIO.output(self.BIN2,False)
        sleep(t)
        if v==1: print('Stop')
    
    def rotate_cw(self,s=50,t=0,v=0):
        self.pwm.ChangeDutyCycle(s)
        self.pwm1.ChangeDutyCycle(s)
        GPIO.output(self.AIN1,False)
        GPIO.output(self.AIN2,True)
        GPIO.output(self.BIN1,True)
        GPIO.output(self.BIN2,False)
        sleep(t)
        if v==1: print('Rotate CW')

    def rotate_ccw(self,s=50,t=0,v=0):
        self.pwm.ChangeDutyCycle(s)
        self.pwm1.ChangeDutyCycle(s)
        GPIO.output(self.AIN1,True)
        GPIO.output(self.AIN2,False)
        GPIO.output(self.BIN1,False)
        GPIO.output(self.BIN2,True)
        sleep(t)
        if v==1: print('Rotate CCW')