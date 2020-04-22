import sys
import os
import math
import pygame
import random


pygame.init()
width = 900
height = 600
background_color = (255,255,255)
elasticity = 0.75
gravity = ( 0.02,math.pi)
timescale=1



mass_of_air = 0.2



screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Gravity Simulation')
screen.fill(background_color)

def addVectors(vector1,vector2):
    angle1, length1 = vector1
    angle2, length2 = vector2
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    
    angle = 0.5 * math.pi - math.atan2(y , x)
    length = math.hypot(x, y)
    return (angle, length)

def findParticles(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None


def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    distance = math.hypot(dx, dy)
    if distance < p1.size + p2.size:
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        total_mass = p1.mass + p2.mass

        (p1.angle, p1.speed) = addVectors((p1.angle, p1.speed * (p1.mass - p2.mass) / total_mass), (angle, 2 * p2.speed * p2.mass / total_mass))
        (p2.angle, p2.speed) = addVectors((p2.angle, p2.speed * (p2.mass - p1.mass) / total_mass), (angle + math.pi, 2 * p1.speed * p1.mass / total_mass))
        p1.speed *= elasticity
        p2.speed *= elasticity

        overlap = 0.5 * (p1.size + p2.size - distance+1)
        p1.x += math.sin(angle) * overlap
        p1.y -= math.cos(angle) * overlap
        p2.x -= math.sin(angle) * overlap
        p2.y += math.cos(angle) * overlap

"""def GForce(a): 
        forceX=0
        forceY=0
        for x in my_particles: #loop through all particles
            if(x!=a): #exclude self from calculation
                b=x
                EPS = 3E4
                distancex = b.x-a.x
                distancey = b.y-a.y
                distanceSquared=distancex*distancex + distancey*distancey
                distance=math.sqrt(distanceSquared)
                F = (G * a.mass * b.mass) / (distanceSquared+(EPS*EPS))
                forceX+=F*distancex/distance
                forceY+=F*distancey/distance
        return [forceX,forceY]"""


class Particle(object):
    def __init__(self, position , size, mass):
        self.x,self.y = position
        self.size = size
        self.mass = mass
        self.color = (0,0,225)
        self.thickness = 1
        self.speed = 0
        self.angle = 0
        self.velocityX=0
        self.velocityY=0
        self.drag = (self.mass/(self.mass + mass_of_air)) ** self.size

    

    
    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), self.size, self.thickness)
    
    


    def move(self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        #gravityForces= math.atan2(self.angle,self.speed)
        self.velocityX+=self.angle
        self.velocityY+=self.speed
        self.x+=self.velocityX*timescale
        self.y+=self.velocityY*timescale
        print(self.x)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        
        



    def bounce(self):
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        
        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi -self.angle
            self.speed *= elasticity

number_of_particles = 3
my_particles = []

""" for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size,width - size)
    y = random.randint(size, height - size)

    particle = Particle((x,y),size,10000)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi * 2)
    my_particles.append(particle) """

SUN = Particle((450,300),43,100*timescale)
my_particles.append(SUN)
#61,155,072,000 meters from sun
#61 pixels from sun

mercury = Particle((511,300),10,.00001*timescale)
#orbital speed = 47360 m/s
mercury.velocityY-=1*timescale
my_particles.append(mercury)
#6.67408 × 10-11 m3 kg-1 s-2 gravitational constant
#.0000000000667408
#6.
selected_particle = None
running = True

for n in range(number_of_particles):
    size = random.randint(10,20)
    density = random.randint(1,20)
    x = random.randint(size, width - size)
    y = random.randint(size, height - size)
    
    particle = Particle((x,y), size, 10000)#density * size ** 2)
    particle.color = (200 - density * 10, 200 - density * 10, 255)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_particle = findParticles(my_particles, mouseX, mouseY)
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        dx = mouseX - selected_particle.x
        dy = mouseY - selected_particle.y 
        selected_particle.angle = math.atan2(dy, dx) + 0.5*math.pi
        selected_particle.speed = math.hypot(dx, dy) * 0.1


    screen.fill(background_color)

    for i, particle in enumerate(my_particles):
        particle.move()
        particle.bounce()
        for particle2 in my_particles[i+1:]:
            collide(particle, particle2)
        particle.display()


    pygame.display.flip()




