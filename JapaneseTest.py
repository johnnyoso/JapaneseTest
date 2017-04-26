import pygame, random
from pygame.locals import *

def name():
	
	## Start the Pygame display and set screen size ##
	pygame.init()
	screen = pygame.display.set_mode((480, 360))
	
	## Some constants to define ##
	font = pygame.font.Font(None, 30)
	x = 0
	clock = pygame.time.Clock()
	frame_count = 0
	frame_rate = 60
	wronganswer = ""
	name = ""
	game = True
	
	## Where the Japanese Characters and Listed ##
	japchar=["katakana_A.png", "katakana_I.png", "katakana_U.png"]
	
	## This will produce a list of random numbers from sample the size of japchar list but never repeating ##
	randomchar=random.sample(xrange(0,len(japchar)),len(japchar))
	
	## This dictionary is used to compare user input with the display image, accepts both small and big caps ##
	japchardic1={'katakana_A.png':'a', 'katakana_I.png':'i', 'katakana_U.png':'u'}
	japchardic2={'katakana_A.png':'A', 'katakana_I.png':'I', 'katakana_U.png':'U'}
	## This will load the first image (since x = 0) value from the randomly generated list ##
	currentchar = pygame.image.load(japchar[randomchar[x]])
	
	## The start of the game loop ##
	while game == True:
		for evt in pygame.event.get():
			if evt.type == KEYDOWN:
				
				## This accepts raw input from the user and stores the value into the 'name' variable
				if evt.unicode.isalpha():
					name += evt.unicode
				
				## Generic backspace function
				elif evt.key == K_BACKSPACE:
					name = name[:-1]
					
				elif evt.key == K_ESCAPE:
					game = False

				elif evt.key == K_RETURN:
					
					## This compares the 'name' user input if equal with the loaded image file name equivalent value in dictionary (small cap) ##
					if (name == japchardic1[japchar[randomchar[x]]]):
						try:
							currentchar = pygame.image.load(japchar[randomchar[x+1]])
							x = x+1
							name = ""
							wronganswer = ""
						## This gives an error message if the dictionary runs out of characters to compare
						except IndexError:
							wronganswer = "game finished"
						
					## This compares the 'name' user input if equal with the loaded image file name equivalent value in dictionary (big cap) ##
					elif (name == japchardic2[japchar[randomchar[x]]]):
						try:
							currentchar = pygame.image.load(japchar[randomchar[x+1]])
							x = x+1
							name = ""
							wronganswer = ""
						except IndexError:
							wronganswer = "game finished"
					
					## If 'name' is not equal to the loaded image file dictionary value ##
					else: 
						name = ""
						wronganswer = "wrong answer try again"
			elif evt.type == QUIT:
				return
				
		screen.fill((0, 0, 0))
		
		# --- Timer going up ---
		# Calculate total seconds
		total_seconds = frame_count // frame_rate
		
		# Divide by 60 to get total minutes
		minutes = total_seconds // 60
		
		# Use modulus (remainder) to get seconds
		seconds = total_seconds % 60
		
		# Use python string formatting to format in leading zeros
		output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
		
		# Blit the timer to the screen
		gametimer = font.render(output_string, True, (255, 255, 255))
		rect = gametimer.get_rect()
		rect.x = 350
		rect.y  =10
		screen.blit(gametimer, rect)
		
		# Blit the user keyboard input on the screen
		block1 = font.render(name, True, (255, 255, 255))
		rect1 = block1.get_rect()
		rect1.bottom = screen.get_rect().bottom
		screen.blit(block1, rect1)
		
		# Blit the "wrong answer" message on the screen
		block2 = font.render(wronganswer, True, (255, 255, 255))
		rect2 = block2.get_rect()
		rect2.top = screen.get_rect().top
		screen.blit(block2, rect2)
		
		# Blit the current japanese character image on the screen
		rect3 = currentchar.get_rect()
		rect3.center = screen.get_rect().center
		screen.blit(currentchar, rect3)
		
		frame_count += 1
		
		# Limit to 20 frames per second
		clock.tick(frame_rate)
		print output_string
		
		# Update the screen 
		pygame.display.flip()

if __name__ == "__main__":
    name()
    pygame.quit()
