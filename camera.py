import RPi.GPIO as GPIO
import time
import picamera
import requests
import json

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

camera = picamera.PiCamera()

buttonValue = 0

url = 'http://localhost:3005/animation/images'
headers = {'content-type': 'application/json'}

print 'camera started.'

try:
	while True:
		if(GPIO.input(18) == False):
			if(buttonValue == 0):
				buttonValue = 1
#				camera.start_preview()
				camera.vflip = True
#				camera.hflip = True
				camera.quality = 90
				camera.resolution = (800, 600)
				time.sleep(0.5)
				uri = '/uploads/' + str(time.time()) + '.jpg'
				camera.capture('public' + uri)
				payload = {'uri': 'uri'}
				r = requests.post(url, data=json.dumps(payload), headers=headers)
				print(r.text)
#				camera.stop_preview()
		else:
			buttonValue = 0
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
