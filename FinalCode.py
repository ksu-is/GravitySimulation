
import sys
import os
import math
import pygame
import random


pygame.init()
width = 900
height = 600
zoom=.06
sunlocationx=(width/2)/zoom
sunlocationy=(height/2)/zoom
background_color = (0,0,0)
elasticity = 0.75
timescale=5


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Solar System Simulation')
screen.fill(background_color)


class Particle(object):
    def __init__(self, position , size, mass):
        self.x,self.y = position
        self.size = size
        self.mass = mass
        self.color = (255,255,225)
        self.thickness = 1                                                           
        self.angle=random.randint(0, 360)
        self.orbitradius=100
        self.orbitratio=1 #ratio to earth orbit
        self.name="planet"

   
    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x*zoom),int(self.y*zoom)), int(self.size*zoom), int(self.thickness*zoom))

    def move(self):

        self.x=(self.orbitradius*(math.sin(math.radians(self.angle))))+(sunlocationx)
        self.y=(self.orbitradius*(math.cos(math.radians(self.angle))))+(sunlocationy)
        
        if(self.angle<360):
            self.angle+=self.orbitratio/timescale
        else:
            self.angle=0
        
        
my_particles = []

#865,370 mi
SUN = Particle((450,300),8,0)
SUN.orbitradius=0
SUN.name="Sun"
my_particles.append(SUN)

#3,031 mi
MER = Particle((450,300),1,0)
#distance 56,131,000 km
MER.orbitradius=56
MER.name="Mercury"
#88 days 365/88=4.14
MER.orbitratio=4.14
my_particles.append(MER)

#7520
VEN = Particle((450,300),1,0)
#distance 108,000,000 km
VEN.orbitradius=108
VEN.name="Venus"
#225
VEN.orbitratio=1.62
my_particles.append(VEN)

#7917
EAR = Particle((450,300),1,0)
#distance 150,000,000 km
EAR.orbitradius=150
EAR.name="Earth"
#365
EAR.orbitratio=1
my_particles.append(EAR)

#4212
MARS = Particle((450,300),1,0)
#distance 218,000,000 km
MARS.orbitradius=218
MARS.name="Mars"
#687
MARS.orbitratio=0.53
my_particles.append(MARS)

#86,881
JUP = Particle((450,300),3,0)
#distance 776,000,000 km
JUP.orbitradius=776
JUP.name="Jupiter"
#4332
JUP.orbitratio=0.084
my_particles.append(JUP)
#86,881

SAT = Particle((450,300),3,0)
#distance 1,496,500,000 km
SAT.orbitradius=1496
SAT.name="Saturn"
#10759
SAT.orbitratio=0.033
my_particles.append(SAT)

URA = Particle((450,300),3,0)
#distance 2,962,750,000 km
URA.orbitradius=2962
URA.name="Uranus"
#30688
URA.orbitratio=0.01189
my_particles.append(URA)

#15299
NEP = Particle((450,300),3,0)
#distance 4,478,000,000 km
NEP.orbitradius=4478
NEP.name="Neptune"
#60,182
NEP.orbitratio=0.006
my_particles.append(NEP)

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_MINUS:
                zoom*=2
                sunlocationx=(width/2)/zoom
                sunlocationy=(height/2)/zoom
            elif event.key == pygame.K_EQUALS:
                zoom/=2
                sunlocationx=(width/2)/zoom
                sunlocationy=(height/2)/zoom
            elif event.key == pygame.K_1:
                    timescale*=1.5
            elif event.key == pygame.K_2:
                    timescale/=1.5

    screen.fill(background_color)

    for i, particle in enumerate(my_particles):
        particle.move()
        particle.display()


    pygame.display.flip()




