import pygame
import sys
from pygame.locals import *

pygame.init()

def main(argv):
	if(len(sys.argv) != 2):
		sys.exit('Usage: largeType.py <string>')

	word=str(sys.argv[1])

	infoObject = pygame.display.Info()
	screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
	font = pygame.font.Font(None, 150)
	pygame.display.set_caption('LargeType')

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))

	text = font.render(word, 1, (255, 255, 255))
	textPosition= text.get_rect()
	textPosition.centerx = background.get_rect().centerx
	textPosition.centery = background.get_rect().centery
	background.blit(text, textPosition)

	screen.blit(background, (0,0))
	pygame.display.flip()

	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

		screen.blit(background, (0, 0))
		pygame.display.flip()

if __name__ == "__main__":
	main(sys.argv[1:])