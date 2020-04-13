import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12,250)

GPIO.setup(16, GPIO.OUT)
pwm2 = GPIO.PWM(16,250)

dc=75
pwm.start(dc)
pwm2.start(dc)

while True:
    for dc in range(0, 101, 5):
        pwm.ChangeDutyCycle(dc)
        pwm2.ChangeDutyCycle(dc)
        time.sleep(0.05)
        print(dc) 
    for dc in range(95, 0, -5):
        pwm.ChangeDutyCycle(dc)
        pwm2.ChangeDutyCycle(dc)
        time.sleep(0.05)
        print(dc)

pwm.stop()
GPIO.cleanup()