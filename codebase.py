import sys
import os
import math
import pygame
import random


pygame.init()
width = 900
height = 600
background_color = (255,255,255)

black = (0,0,0)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Gravity Simulation')
screen.fill(background_color)

class Particle(object):
    def __init__(self, position , size):
        self.x,self.y = position
        self.size = size
        self.color = (0,0,225)
        self.thickness = 1
        self.speed = 0.01
        self.angle = 0
    

    
    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), self.size, self.thickness)
    
    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

number_of_particles = 10
my_particles = []

for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size,width - size)
    y = random.randint(size, height - size)

    particle = Particle((x,y),size)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi * 2)
    my_particles.append(particle)
    


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    for particle in my_particles:
        particle.move()
        particle.display()
    pygame.display.flip()




