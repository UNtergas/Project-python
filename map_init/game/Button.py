import pygame
from .const import font1


class Button:

    def __init__(self,  x, y, width, height, image, text=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text = text

    def show(self, screen):
        if self.text != "":
            font = pygame.font.SysFont(font1, 60)
            text = font.render(self.text, 1, (0, 0, 0), (225, 225, 225))
            rect_text = pygame.Rect(
                self.x, self.y, text.get_width(), text.get_height())
            screen.blit(text, (rect_text))
        else:
            screen.blit(pygame.transform.scale(
                self.image, (self.width, self.height)), self.rect)

    # def customshow(self, width, height, screen):
    #     if self.text != "":
    #         font = pygame.font.SysFont(font1, 60)
    #         text = font.render(self.text, 1, (0, 0, 0), (225, 225, 225))
    #         rect_text = pygame.Rect(
    #             self.x, self.y, text.get_width(), text.get_height())
    #         screen.blit(text, (rect_text))
    #     else:
    #         screen.blit(pygame.transform.scale(
    #             self.image, (width, height)), self.rect)

    def MouseonButton(self, posMouse):
        if (posMouse[0] > self.x and posMouse[0] < self.x + self.width):
            if (posMouse[1] > self.y and posMouse[1] < self.y + self.height):
                print("ok")
                return True
        return False
