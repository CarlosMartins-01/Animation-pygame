import pygame as pg
import sys

from player import Player

clock = pg.time.Clock()
pg.init()

# screen dimensions
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 240

pg.display.set_caption('Animation - pg')
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# sprites
all_sprites = pg.sprite.Group()

player = Player(0 , 0)
all_sprites.add(player)

# loop
while True:

    # handle inputs
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_UP:
                player.movement = 'jumping'
            if event.key == pg.K_RIGHT:
                player.movement = 'walking'
            if event.key == pg.K_SPACE:
                player.movement = 'running'

        if event.type == pg.KEYUP:

            if event.key == pg.K_UP:
                player.movement = 'stopped'
            if event.key == pg.K_RIGHT:
                player.movement = 'stopped'
            if event.key == pg.K_SPACE:
                player.movement = 'stopped'

    # draw
    screen.blit(pg.image.load('Assets/background.png'), (0, 0))
    all_sprites.draw(screen)

    # update
    all_sprites.update()
    pg.display.flip()
    clock.tick(60)
