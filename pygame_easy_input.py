import pygame

#Input class. For a better and more neatly input handling
class Input:
	event: pygame.event
	held_keys=[]
	def update(self, event: pygame.event):
		self.event=event
		if self.event.type==pygame.KEYDOWN:
			self.held_keys.append(event.key)
		elif self.event.type==pygame.KEYUP:
			if self.event.key in self.held_keys:
				self.held_keys.remove(self.event.key)
	
	def is_pressed(self, keycode: int) -> bool:
		if self.event.type==pygame.KEYDOWN and self.event.key==keycode:
			return True
		return False
	
	def is_released(self, keycode: int) -> bool:
		if self.event.type==pygame.KEYUP and self.event.key==keycode:
			return True
		return False
	
	def is_down(self, keycode: int) -> bool:
		return keycode in self.held_keys
	
	def is_up(self, keycode: int) -> bool:
		return not keycode in self.held_keys