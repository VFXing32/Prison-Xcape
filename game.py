import pygame
import sys
import math
import random
from scripts.utils import load_image , load_images , Animation
from scripts.entities import PhysicsEntity , Player
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds
from scripts.particle import Particle


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Prison Xcape")
        self.screen = pygame.display.set_mode((640, 480))

        #stretching screen
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False , False]

        self.assets = {
            'decore': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds'),
            'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
            'player/run': Animation(load_images('entities/player/run'), img_dur=6),
            'player/jump': Animation(load_images('entities/player/jump')),
            'player/slide': Animation(load_images('entities/player/slide')),
            'player/wall_slide': Animation(load_images('entities/player/wall_slide')),
            'particle/particle': Animation(load_images('particles/particle'), img_dur= 6 , loop=False),

        }

        self.clouds = Clouds(self.assets['clouds'], count=16)

        self.player = Player(self,(50,50),(8,15))

        self.tilemap = Tilemap(self ,tile_size=16)

        self.particles = []
        
        self.scroll = [0, 0]

    def run(self):
        while True:
            # self.display.fill((14 , 219 , 248))
            self.display.blit(self.assets['background'],(0,0))

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width()/4 - self.scroll[0]) 
            self.scroll[1] += (self.player.rect().centery - self.display.get_height()/2 - self.scroll[1])
            render_scroll = (int(self.scroll[0]),int (self.scroll[1]))

            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)

            self.tilemap.render(self.display, offset=render_scroll)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)

            # print(self.tilemap.physics_rects_around(self.player.pos))
            for particle in self.particles.copy():
                kill = particle.update()
                particle.render(self.display, offset=render_scroll)
                if kill:
                    self.particles.remove(particle)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.jump()
                    if event.key == pygame.K_x:
                        self.player.dash()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            #Strechting screen            
            self.screen.blit(pygame.transform.scale(self.display ,self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()
