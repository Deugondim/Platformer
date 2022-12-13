import pygame

from support import import_folder


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.5
        if type == 'jump':
            # get the particle for jump in folder
            self.frames = import_folder(
                'graphics/character/dust_particles/jump')
        if type == 'land':
            # get the particle for land in folder
            self.frames = import_folder(
                'graphics/character/dust_particles/land')
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        # partile animation
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self, x_shift):
        # sends the update
        self.animate()
        self.rect.x += x_shift
