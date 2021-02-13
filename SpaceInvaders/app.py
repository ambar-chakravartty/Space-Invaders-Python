import pygame
import random
import math
#Dimensions
screen_width = 800
screen_height = 600

#Classe
class Ship:
	def __init__(self,xpos,ypos): 
		self.img = pygame.image.load('rocket.png')
		self.x = xpos
		self.y = ypos
		self.v = 0

	def show(self):
		screen.blit(self.img,(self.x,self.y))

	def move(self):
		self.x += self.v

class Alien:
	def __init__(self,xpos,ypos): 
		self.img = pygame.image.load('alien.png')
		self.x = xpos
		self.y = ypos
		self.v = 0.07
		self.xv = 1
		self.rect = self.img.get_rect()

	def show(self):
		screen.blit(self.img,(self.x,self.y))

	def move(self):
		self.y += self.v




	def is_collided_with(self, sprite):
		return self.rect.colliderect(sprite.rect)

class Bullet():
	"""docstring for Bullet"""
	def __init__(self,v):
		
		self.img = pygame.image.load('bullet.png')
		self.x = ship.x
		self.y = ship.y
		self.v = v
		self.c = 0 
		self.rect = pygame.Rect(self.x,self.y,2,40)
		#self.rect = 

	def show(self):
		screen.blit(self.img,(self.x,self.y))

	def move(self):
		self.y += self.v
	
	def reset(self):
		if self.y < 0:
			self.y = ship.y 
			self.v = 0
			self.x = ship.x+30

#Initializing The Display
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('Space Invaders')
icon =pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)
b_img = pygame.image.load('space.png')

ship = Ship(screen_width/2-32,500) # An instance of the ship class

#Bullets
lasers = []

#Aliens
aliens = []
for i in range(1,13):			#Loop to add aliens to the array of aliens
	aliens.append(Alien(i*80,20))

def crash(a,b):  #Function to detect collision between ammo and aliens
	distance = math.sqrt(math.pow(a.x - b.x, 2) + (math.pow(a.y - b.y, 2)))
	if distance < 27:
		return True
	else:
		return False

count = 0
def add():  #Function to add extra aliens to the aliens array
	global count 
	for i in range(1,7):
		count += 1
		aliens.append(Alien(i*80,20))

#Game Loop
running = True 
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				ship.v = -5
			if event.key == pygame.K_RIGHT:
				ship.v = 5
			if event.key == pygame.K_SPACE:
				laser = Bullet(-9)
				lasers.append(laser)
				


		if event.type == pygame.KEYUP:
			ship.v = 0
			
			

	

	screen.fill((0,0,0))
	screen.blit(b_img,(0,0))

	for i in lasers:
		i.show()
		i.move()
		
	ship.show()
	ship.move()

	for i in aliens:
		i.move()
		i.show()

	for i in lasers:
		for j in aliens:
			if crash(j,i):
				aliens.remove(j)

	if len(aliens) <= 3: 
		add()

	pygame.display.flip()
	clock.tick(60)
