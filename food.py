import pygame
import random

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fishnum = random.randint(1, 9)
        self.direction = random.randint(1, 2)
        if self.direction == 1:
            self.image = pygame.image.load("food" + str(self.fishnum) + ".png")
        else:
            self.image = pygame.image.load("food" + str(self.fishnum) + "left.png")
        self.image_size = self.image.get_size()
        scale_size = (random.randint(30, 70), random.randint(20, 50))
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = random.randint(1, 3)/10

    def move(self):
        if (self.direction == 1):
            self.x = self.x + self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if (self.direction == 2):
            self.x = self.x - self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def check_real_collision(self, overlap):
        for i in range(0, overlap.size[0]):
            for j in range(0, overlap.size[1]):
                rgb = self.image.get_at((i, j))
                if rgb != (0, 0, 0, 0):
                    return True
        return False
