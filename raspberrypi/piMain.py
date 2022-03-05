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
panik = GPIO.PWM(PWM2,5)

kalm.start(0)
panik.start(0)

print("PWM set up")


panik.ChangeDutyCycle(50)
kalm.ChangeDutyCycle(50)
GPIO.output(PWM_EN,1)

def kalm_me(dutyCycle,time):
    kalm.ChangeDutyCycle(dutyCycle)
    time.sleep(0.1)
    GPIO.output(PWM_EN,1)
    time.sleep(time)
    GPIO.output(PWM_EN,0)
    kalm.ChangeDutyCycle(0)

def panik_me(dutyCycle,time):
    panik.ChangeDutyCycle(dutyCycle)
    time.sleep(time)
    panik.ChangeDutyCycle(0)
try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
