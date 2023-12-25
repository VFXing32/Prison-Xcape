import pygame

class PhysicsEntity:
    def __init__(self, game,e_type ,pos ,size):
        self.game = game
        self.e_type = e_type
        self.pos = list(pos)
        self.size = size
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        