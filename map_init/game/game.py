import pygame as pg
import sys
from .world import World
from .setting import TILE_SIZE
from .utils import draw_text
from .camera import Camera
from .gamehud import *


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        # world
        self.world = World(40, 40, self.width, self.height)
        # camera
        self.camera = Camera(self.width, self.height)
        # hud
        self.hudup = Hudupper(0, 0)
        self.hudleft = Hudbigleft(self.width-24, self.height+25)
        self.hudstick = Hudstick(self.width-24, 24)
        self.infofps = InfoShow(
            self.width*0.5, 2, f"fps={round(self.clock.get_fps())}", 18, (255, 255, 255))
        self.infopop = InfoShow(
            self.width*0.6, 2, f"Pop    xxxx", 18, (255, 255, 255))

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        self.camera.movement()
        # for event in pg.event.get():
        #     if event.type == pg.QUIT:
        #         pg.quit()
        #         sys.exit()
        #     self.camera.movement()

    def update(self):
        pass

    def draw(self):

        self.screen.fill((0, 0, 0))
        self.screen.blit(self.world.land_tile,
                         (self.camera.scroll.x, self.camera.scroll.y))

        for x in range(self.world.grid_lx):
            for y in range(self.world.grid_ly):

                #   2D grid

                # sq = self.world.world[x][y]["cart_rect"]
                # rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                # pg.draw.rect(self.screen, (0, 0, 255), rect, 2)

                render_pos = self.world.world[x][y]["render_pos"]

#                   different tiles
#
                if self.world.world[x][y]["tile"]["name"] != "":
                    # tile = self.world.world[x][y]["tile"]
                    name_tile = self.world.world[x][y]["tile"]["name"]
                    offset = self.world.world[x][y]["tile"]["offset"]
                    self.screen.blit(self.world.tiles[name_tile], (
                        render_pos[0]+self.world.land_tile.get_width() *
                        0.5 + self.camera.scroll.x,
                        render_pos[1]+self.world.land_tile.get_height()*0 - offset + self.camera.scroll.y))


#
#                   2.5D grid

                p = self.world.world[x][y]["iso_poly"]
                p = [(x + self.world.land_tile.get_width() *
                      0.5 + self.camera.scroll.x, y + self.world.land_tile.get_height()*0+self.camera.scroll.y) for x, y in p]
                pg.draw.polygon(self.screen, (0, 0, 0), p, 1)
        self.hudleft.draw(self.screen)
        self.hudstick.draw(self.screen)
        self.hudup.draw(self.screen)
        self.infofps.draw(self.screen)
        self.infopop.draw(self.screen)

        # draw_text(
        #     self.screen,
        #     f"fps={round(self.clock.get_fps())}",
        #     25,
        #     (0, 0, 0),
        #     (10, 10)

        # )

        pg.display.flip()
