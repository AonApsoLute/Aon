"""
Raspberry Pi capture 360
Copyright 2017 Wanchai Saechia
"""
import glob
import os
import sys
import select
import pygame

import pygame.camera
import time

from RPIO import PWM

servo = PWM.Servo()

width = 640
height = 480


# Prefix for positive training image filenames.
POSITIVE_FILE_PREFIX = 'positive_'	

if __name__ == '__main__':
	count = 1
	
for count in range(180) :
		
	filename = (POSITIVE_FILE_PREFIX + '%d.jpg' % count)
									
	import pygame
			
	import pygame.camera
			
	from pygame.locals import *
	x = (450 + ((count-1) * 10))
	print x
	servo.set_servo(18, x)
	time.sleep(3)	
	pygame.init()
	pygame.camera.init()
			
	cam = pygame.camera.Camera("/dev/video0",(640,480))
	cam.start()
	cam.get_raw()
	image = cam.get_image()
			
	pygame.image.save(image, filename)
			
	cam.stop()
			
	count += 1
	servo.stop_servo(18)

