"""Input handling sample using the Input class written by Kianoosh Shakeri

Add your own desired way of output. Currently it just prints to the console"""

import pygame
from cytolk import tolk
import input

pygame.init()
tolk.load()

pygame.display.set_caption("Input handler sample")
screen=pygame.display.set_mode((640, 480))

game_input=input.Input()
clock=pygame.time.Clock()
key_up_moment=pygame.time.get_ticks()

while True:
	now=pygame.time.get_ticks()
	event=pygame.event.poll()
	if event.type==pygame.QUIT:
		break
	#Fill the screen with the color white
	screen.fill([255,255,255])
	#update the input handler class
	game_input.update(event)
	if game_input.is_pressed(pygame.K_SPACE):
		print("Space is pressed")
	if game_input.is_down(pygame.K_LCTRL):
		print("Left control is being held down")
	#While the space key is not pressed down, it keeps generating a message each 1.5 seconds.
	if now-key_up_moment >= 1500 and game_input.is_up(pygame.K_SPACE):
		print("Space key is not pressed")
		key_up_moment=now
	pygame.display.flip()
	#Limit the updates to 30 frames per second
	clock.tick(30)

pygame.quit()