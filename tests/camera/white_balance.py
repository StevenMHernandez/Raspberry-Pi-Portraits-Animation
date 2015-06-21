import time
import picamera

camera = picamera.PiCamera()

camera.vflip = True
camera.awb_mode = 'off'

print 'This test boosts the camera\'s white balance every half second.'
print 'This test doesn\'t really give useful information'
print 'it misses a whole range of stuff.'
print 'Press ctrl + c at the desired white balance to stop the test.'
time.sleep(1)

try:
	camera.start_preview()
	for x in range(0, 80):
		gain = float(x) / 10
		camera.awb_gains = (1, gain)
		time.sleep(0.5)

except KeyboardInterrupt:
	print '\nTest stopped with gain set to (%s, %s)' % (1, gain)
	camera.stop_preview()/
