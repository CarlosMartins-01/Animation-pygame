import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.movement = 'stopped'

        self.sprites = []
        self.current_sprite = 0

        self.image = pg.image.load('Assets/mario_idle.png')

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # jumping
        if self.movement == 'jumping':
            self.sprites.append(pg.image.load('Assets/Jump/1.png'))
            self.sprites.append(pg.image.load('Assets/Jump/2.png'))

            self.current_sprite += 0.10
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]

        # walking
        if self.movement == 'walking':
            self.sprites.append(pg.image.load('Assets/Walk/1.png'))
            self.sprites.append(pg.image.load('Assets/Walk/2.png'))
            self.sprites.append(pg.image.load('Assets/Walk/3.png'))

            self.current_sprite += 0.25

            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]

        # running
        if self.movement == 'running':
            self.sprites.append(pg.image.load('Assets/Run/1.png'))
            self.sprites.append(pg.image.load('Assets/Run/2.png'))
            self.sprites.append(pg.image.load('Assets/Run/3.png'))

            self.current_sprite += 0.25

            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]

        # stopped
        if self.movement == 'stopped':
            self.sprites.clear()
            self.current_sprite = 0

            self.image = pg.image.load('Assets/mario_idle.png')
