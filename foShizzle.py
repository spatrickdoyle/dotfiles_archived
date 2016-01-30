import pygame,time,math,subprocess,urllib,os

KEYDOWN = pygame.KEYDOWN
KEYUP = pygame.KEYUP
K_DOWN = pygame.K_DOWN
K_UP = pygame.K_UP
K_RIGHT = pygame.K_RIGHT
K_LEFT = pygame.K_LEFT
K_SPACE = pygame.K_SPACE
MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN
MOUSEBUTTONUP = pygame.MOUSEBUTTONUP
MOUSEMOTION = pygame.MOUSEMOTION
EventPoll = pygame.event.get
Rect = pygame.Rect

RED = "RED"
BLUE = "BLUE"
WHITE = "WHITE"
GREY = "GREY"
GREEN = "GREEN"
TORQ = "TORQ"
YELLOW = "YELLOW"
PURPLE = "PURPLE"

def init(x,y,full=None,mouse=None,nobar=None):
	pygame.init()
	pygame.mixer.init()
	global screen
	if full == None:
		return None
	if full == True:
		screen = pygame.display.set_mode((x,y),pygame.FULLSCREEN)
	if nobar == True:
		screen = pygame.display.set_mode((x,y),pygame.NOFRAME)
	else:
		screen = pygame.display.set_mode((x,y))
	pygame.mouse.set_visible(mouse)
	return screen

def joy_init(joyst):
	joy = pygame.joystick.Joystick(joyst)
	joy.init()
	return joy

def caption(te):
	pygame.display.set_caption(te)

def icon(path):
	a = pygame.image.load(path)
	pygame.display.set_icon(a)


def bg(r,g,b):
	screen.fill((r, g, b))


def getX(joys):
	return joys.get_axis(0)
def getY(joys):
	return joys.get_axis(1)
def get3(joys):
	return joys.get_axis(2)
def get4(joys):
	return joys.get_axis(3)
def get_button(joys,button):
	return joys.get_button(button)

def ScreenClose(evente):
	if evente.type == pygame.QUIT:
		raise SystemExit
def button_event(evente,rect):
	if evente.type == pygame.MOUSEBUTTONDOWN:
		if evente.button == 1:
			eventX = evente.pos[0]
			eventY = evente.pos[1]
			if rect.collidepoint(eventX,eventY):
				return True
	return False
def hover(evente,rect):
	eventX = evente.pos[0]
	eventY = evente.pos[1]
	if rect.collidepoint(eventX,eventY):
		return True
	return False


def textInit(size,font="Ubuntu",bold=None,italic=None):
	return pygame.font.SysFont(font, size,bold,italic)
def textLoad(obj,text,color):
	return obj.render(text, 2, color)#.convert()

def imageLoad(path):
	return pygame.image.load(path)#.convert()

def sound(filename):
	pygame.mixer.music.load(filename)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		continue
	pygame.mixer.music.stop()
def sound_loop(filename):
	pygame.mixer.music.load(filename)
	pygame.mixer.music.play()
def sound_stop():
	pygame.mixer.music.stop()


def color(text,color,bold):
	if color == 'GREY':
		number = 30
	elif color == 'RED':
		number = 31
	elif color == 'GREEN':
		number = 32
	elif color == 'YELLOW':
		number = 33
	elif color == 'BLUE':
		number = 34
	elif color == 'PURPLE':
		number = 35
	elif color == 'TORQ':
		number = 36
	elif color == 'WHITE':
		number = 37
	else:
		number = color
	#return '\033[%dm'%(b)+c+'\033[97m'
	os.system('''echo -e "\e[%d;%dm%s\e[0m"'''%(bold,number,text))


def flip(clocke,f=0):
	pygame.display.update()
	return clocke.tick(f)
def clock():
	clock = pygame.time.Clock()
	return clock