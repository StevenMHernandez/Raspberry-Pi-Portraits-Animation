import time
import picamera

camera = picamera.PiCamera()

camera.vflip = True

print 'This test boosts the camera brightness every half second.'
print 'Press ctrl + c at the desired brightness to stop the test.'
time.sleep(5)

try:
	camera.start_preview()
	for x in range(25, 100):
		brightness = x
		camera.brightness = brightness
		time.sleep(0.5)

except KeyboardInterrupt:
	print '\nTest stopped with brightness of: ' + str(brightness)
	camera.stop_preview()
