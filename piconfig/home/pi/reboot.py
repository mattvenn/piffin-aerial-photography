import time, RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

import os,time

led_pin = 8
button_pin = 10

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def flash(times):
	#turn on led
	for i in range(times):
		GPIO.output(led_pin, True)
		time.sleep(0.1)
		GPIO.output(led_pin, False)
		time.sleep(0.1)

#wait for button

flash(5)
GPIO.wait_for_edge(button_pin, GPIO.FALLING)  
print("shutdown")
flash(5)
os.system("/sbin/halt")

