import picamera
from time import sleep
camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.brightness = 60
camera.start_preview()
sleep(2)
camera.capture('/home/pi/Pictures/image1.jpeg')
camera.stop_preview()