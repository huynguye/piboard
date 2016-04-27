import pygame
import time
import curses

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

up    = pygame.mixer.Sound('beats/clap.wav')
down  = pygame.mixer.Sound('beats/closed.wav')
left  = pygame.mixer.Sound('beats/cymbal.wav')
right = pygame.mixer.Sound('beats/kick.wav')

s_clap   = pygame.mixer.Sound('beats/clap.wav')
s_closed = pygame.mixer.Sound('beats/closed.wav')
s_cymbal = pygame.mixer.Sound('beats/cymbal.wav')
s_kick   = pygame.mixer.Sound('beats/kick.wav')
s_open   = pygame.mixer.Sound('beats/open.wav')
s_snare  = pygame.mixer.Sound('beats/snare.wav')

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

screen.clear()

while True:
	screen.addstr(1, 0, "Ready to accept up, down, left or right to play sounds or q to quit!")
	screen.addstr(2, 0, "To get to a new console press Alt-F2")

	event = screen.getch()
	screen.clear()

	if event == ord('q'):
		break
	elif event == curses.KEY_UP:
		# screen.addstr(0, 0, "You pressed up!")
		up.play()
	elif event == curses.KEY_DOWN:
		# screen.clear()
		# screen.addstr(0, 0, "You pressed down!")
		down.play()
	elif event == curses.KEY_LEFT:
		# screen.clear()
		# screen.addstr(0, 0, "You pressed left!")
		left.play()
	elif event == curses.KEY_RIGHT:
		# screen.clear()
		# screen.addstr(0, 0, "You pressed right!")
		right.play()
	else:
		# screen.clear()
		# screen.addstr(0, 0, "That key doesn't do anything!")
		pass

curses.endwin()
