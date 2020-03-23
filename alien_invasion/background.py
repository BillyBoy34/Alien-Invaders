# 12/16/2019

import pygame


class Background():

    def __init__(self, screen):
        """Initiate attributes for the background."""
        self.screen = screen

        # Get background image and rect of screen and image
        background_img = "C:/Users/husza/PycharmProjects/Notebooks and TIY/TIY/TIY PG 298/images/spacebg3.bmp"
        self.image = pygame.image.load(background_img)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Set image rect equal to the screen rect.
        self.rect = self.screen_rect

    def blitme(self):
        """Draw the background image"""
        self.screen.blit(self.image, self.rect)








































































































