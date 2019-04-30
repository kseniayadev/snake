import time
import random

import pygame

pygame.init()
sc = pygame.display.set_mode((400, 400))

clock = pygame.time.Clock()

BLACK = pygame.Color('black')
YELLOW = pygame.Color('yellow')
RED = pygame.Color('red')


head = [10, 10]
tail = [[10, 11]]


def generate():
	x = random.randint(0, 19)
	y = random.randint(0, 19)
	while [x, y] in [head, *tail]:
		x = random.randint(0, 19)
		y = random.randint(0, 19)
	return [x, y]

	
aim = generate()


def draw_brick(x, y, color):
	sc.fill(
	color,
		(x * 20, y * 20, 20, 20),
	)

delay = 0
threshold = 1000
dir = 'u'
running = True
while running:
	def end():
		global running
		font = pygame.font.Font(None, 24)
		text = font.render(str(len(tail)), 1, (255, 0, 0))
		sc.fill(BLACK)
		w, h = text.get_size()
		sc.blit(text, (200 - w // 2, 200 - h // 2))
		pygame.display.flip()
		time.sleep(3)
		running = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYUP:
			key = pygame.key.name(event.key)
			if key == 'w':
				dir = 'u'
			elif key == 's':
				dir = 'd'
			elif key == 'a':
				dir = 'l'
			elif key == 'd':
				dir = 'r'
	sc.fill(BLACK)
	draw_brick(*head, YELLOW)
	for block in tail:
		draw_brick(*block, YELLOW)
	draw_brick(*aim, RED)
	pygame.display.flip()
	delay += clock.tick(100)
	if delay >= threshold:
		delay = 0
		if dir == 'u':
			head[1] -= 1
		elif dir == 'd':
			head[1] += 1
		elif dir == 'l':
			head[0] -= 1
		elif dir == 'r':
			head[0] += 1
		if head in tail:
			end()
		if any(val < 0 or val > 19 for val in head):
			end()
		if head == aim:
			tail.append(tail[-1].copy())
			aim = generate()
			threshold -= 50
			if threshold <= 0:
				threshold = 10
		tail.pop()
		tail.insert(0, head.copy())