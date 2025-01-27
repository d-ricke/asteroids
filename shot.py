import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot (CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0,0)
    
    def draw(self, screen):
        color = "white"
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
        #pygame.draw.circle(screen, self.position, color, width=2)

    def update(self, dt):
        self.position += self.velocity * dt 
