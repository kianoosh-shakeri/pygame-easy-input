# pygame-easy-input
A simple class that allows an easier handling of input suitable for games that implement pygame events  
Currently supports keyboard only.
## How to use?
There's an example provided, check out input_sample.py. Here's a general idea of how you can implement this module into your game.  
First import the module  
import pygame_easy_input
Next, create and initialize an instance of the Input class before your main loop starts  
game_input=pygame_easy_input.Input()  
Now, in your main loop, poll a pygame event, update your input and pass the polled pygame.event to the function  
event=pygame.event.poll()  
game_input.update(event)  
And now here's how you print some text once the space key is pressed. Just add this line below game_input.update  
if game_input.is_pressed(pygame.K_SPACE):  
&nbsp;&nbsp;&nbsp;&nbsp;print("some text")