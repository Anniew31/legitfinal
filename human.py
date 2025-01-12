import pygame

class Human:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("personright.png")
        self.image_size = self.image.get_size()
        scale_size = (55, 37)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 1

    def move_direction(self, direction):
        if direction == "right":
            self.image = pygame.image.load("personright.png")
            self.image_size = self.image.get_size()
            scale_size = (55, 37)
            self.image = pygame.transform.scale(self.image, scale_size)
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            if (self.rect.left < 680):
                self.x = self.x + self.delta*1.5

        if direction == "left":
            if (self.rect.left > 0):
                self.x = self.x - self.delta
            self.image = pygame.image.load("personleft.png")
            self.image_size = self.image.get_size()
            scale_size = (60, 40)
            self.image = pygame.transform.scale(self.image, scale_size)
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

        if direction == "up":
            if (self.rect.top > 0):
                self.y = self.y - self.delta/1.25
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "down":
            if (self.rect.top < 450):
                self.y = self.y + self.delta/1.25
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def grow_human(self, points):
        self.image_size = self.image.get_size()
        scale_size = (.01 * points, .01 * points)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])