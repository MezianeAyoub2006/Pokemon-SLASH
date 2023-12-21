import pygame, sys, os, time
from typing import *

class GameContext:
    
    def __init__(self, resolution:Tuple[int, int], flags:int=0, vsync:bool=False):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution, flags, vsync=vsync)
        self.clock = pygame.time.Clock()
        icon_path = os.path.join(__file__[:-10], "logo.png")
        pygame.display.set_caption("Blank Project", icon_path)
        pygame.display.set_icon(pygame.image.load(icon_path).convert_alpha())
        self.camera = [0, 0]
        self.dt = 1
        self.lt = time.perf_counter()

    def run(self, game_loop):
        while 1:
            self.delta_time()
            game_loop()
            pygame.display.flip()
            self.clock.tick(10000)

    def quit(self):
        pygame.quit()
        sys.exit()

    def delta_time(self):
        self.dt = time.perf_counter() - self.lt
        self.dt *= 60
        self.lt = time.perf_counter()

    def render_rect(self, rect, color, z_pos=None):
        if z_pos == None:
            pygame.draw.rect(self.screen, color, pygame.Rect(rect.x - self.camera[0], rect.y - self.camera[1], rect.w, rect.h))

    def draw(self, surface, position, z_pos=None):
        if z_pos == None:
            self.screen.blit(surface, position)

    def render(self, surface, position, z_pos=None):
        self.draw(surface, self.relative(position), z_pos)

    def set_caption(self, text):
        pygame.display.set_caption(text)

    def get_fps(self):
        return self.clock.get_fps()
    
    def get_dt(self):
        return self.dt
    
    def get_display_size(self):
        return self.screen.get_size()
    
    def relative(self, position):
        return [position[0] - self.camera[0], position[1] - self.camera[1]]

    def get_pressed(self):
        return pygame.key.get_pressed()

    def toggle_fullscreen(self):
        pygame.display.toggle_fullscreen()
