import picamera
from time import sleep
camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()
camera.start_recording("/home/pi/demo.h264")
sleep(20)
camera.stop_recording()
camera.stop_preview()