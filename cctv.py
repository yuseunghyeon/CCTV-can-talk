import picamera
import datetime
import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("siren.wav")

def recording():
	with picamera.PiCamera() as cctv:
		cctv.resolution = (640,480)
		current = datetime.datetime.now()
		name= current.strftime('%Y-%m-%d %H:%M:%S')
		cctv.start_recording(output = name + '.h264')
		cctv.wait_recording(15)
		cctv.stop_recording()
	
num=1;
if num==1:
	print("This is a project that makes the role of crime prevention more clear.")
	print("This cctv saves the video with a warning tone every 15 seconds")	
	print("If you want to finish this cctv, push Ctrl + z")

while True:
	recording()
	pygame.mixer.music.play()
	print("This is {} time this cctv has been doing this".format(num))
	num=num+1	
