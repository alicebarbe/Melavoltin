import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PWM1 = 12
PWM2 = 13
PWM_EN = 19


GPIO.setup(PWM1,GPIO.OUT)
GPIO.setup(PWM2,GPIO.OUT)
GPIO.setup(PWM_EN,GPIO.OUT)
kalm = GPIO.PWM(PWM1,200)
panik = GPIO.PWM(PWM2,10)

kalm.start(0)
panik.start(0)

print("PWM set up")


panik.ChangeDutyCycle(50)
kalm.ChangeDutyCycle(0)
GPIO.output(PWM_EN,1)

while True:
    pass


GPIO.cleanup()
