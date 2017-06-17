import picamera
import time
from cv2 import waitKey
cam = picamera.PiCamera()
while True:
	cam.start_preview(fullscreen=False, window = (100,100,640,480))
	#time.sleep(10)

	cam.stop_preview()
	key = raw_input("Enter the Hot Key:")
 
	if key == 'c':

		cam.capture('lassi.jpg')

	elif key == 'q':
		cam.stop_preview()


