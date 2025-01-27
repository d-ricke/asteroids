import pygame
import random 
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_ACCEL

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = "white"
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
        #pygame.draw.circle(screen, self.position, color, width=2)

    def update(self, dt):
        self.position += self.velocity * dt 
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return ()
        else:
            deflection = random.uniform(20,50)
            angle1 = self.velocity.rotate(deflection)
            angle2 = self.velocity.rotate(-deflection)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            x,y = self.position
            asteroid = Asteroid(x,y,new_radius)
            asteroid2 = Asteroid(x,y,new_radius)
            asteroid.velocity = angle1 * ASTEROID_SPLIT_ACCEL
            asteroid2.velocity = angle2 * ASTEROID_SPLIT_ACCEL

            asteroid.add(*self.containers)
            asteroid2.add(*self.containers)

        