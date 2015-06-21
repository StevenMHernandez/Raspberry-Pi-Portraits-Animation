print 'starting camera...'
import RPi.GPIO as GPIO
import time
import picamera
import requests
import json

GPIO.setmode(GPIO.BCM)

button_pin = 17
led_pin = 27

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

camera = picamera.PiCamera()

#                 #
# camera settings #
#                 #
camera.brightness = 55
camera.vflip = True
# camera.hflip = True
camera.quality = 90
camera.resolution = (656, 416)
camera.led = True
camera.awb_mode = 'off'
camera.awb_gains = (1.0, 3.0)
#                 #
#  end settings   #
#                 #

buttonValue = 0

url = 'http://localhost:3005/animation/images'
headers = {'content-type': 'application/json'}

print 'camera started.'

def led_blink_timer( seconds ):
	blink_time = seconds / 2 
	i = 1
	while (blink_time > .1):
		blink_time *= .5
		for x in range(0, i):
			led_on( blink_time )
			led_off( blink_time )
		i *= 2
	camera.led = True

def led_on( seconds ):
	camera.led = True
	GPIO.output(led_pin, 1)
	time.sleep(seconds)

def led_off( seconds ):
	camera.led = False
	GPIO.output(led_pin, 0)
	time.sleep(seconds / 2)

try:
	while True:
		if(GPIO.input(button_pin) == False):
			if(buttonValue == 0):
				buttonValue = 1
				camera.start_preview()
				led_blink_timer(5.0)
				uri = '/uploads/' + str(time.time()) + '.jpg'
				camera.stop_preview()
				GPIO.output(led_pin, 1)
				camera.capture('public' + uri)
				GPIO.output(led_pin, 0)
				payload = {'uri': uri}
				r = requests.post(url, data=json.dumps(payload), headers=headers)
		else:
			buttonValue = 0

except:
	GPIO.cleanup()
