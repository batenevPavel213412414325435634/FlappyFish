import pygame
import sys
import random


class FlappyFish:
    def __init__(self):

        self.screen = pygame.display.set_mode((500, 808))
        self.fish = pygame.Rect(55, 50, 50, 50)
        self.background = pygame.image.load("assets/background.png").convert()
        self.fishSprites = [pygame.image.load("assets/fish1.png").convert_alpha(),
                            pygame.image.load("assets/fish1.png").convert_alpha(),
                            pygame.image.load("assets/fishdead.png")]
        self.wallUp = pygame.image.load("assets/bottom.png").convert_alpha()
        self.wallDown = pygame.image.load("assets/top.png").convert_alpha()
        self.gap = 130
        self.wallx = 450
        self.fishY = 750
        self.jump = 0
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False
        self.sprite = 0
        self.counter = 0
        self.offset = random.randint(-150, 150)

    def updateWalls(self):
        self.wallx -= 3
        if self.wallx < -80:
            self.wallx = 450
            self.counter += 1
            self.offset = random.randint(-150, 150)

    def fishUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.fishY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.fishY += self.gravity
            self.gravity += 0.2
        self.fish[1] = self.fishY
        upRect = pygame.Rect(self.wallx, 360 + self.gap - self.offset + 10, self.wallUp.get_width() - 10,
                             self.wallUp.get_height())
        downRect = pygame.Rect(self.wallx, 0 - self.gap - self.offset - 10, self.wallDown.get_width() - 10,
                               self.wallDown.get_height())
        if upRect.colliderect(self.fish):
            self.dead = True
        if downRect.colliderect(self.fish):
            self.dead = True
        if not 0 < self.fish[1] < 720:
            self.fish[1] = 50
            self.fishY = 250
            self.dead = False
            self.counter = 0
            self.wallx = 400
            self.offset = random.randint(-150, 150)
            self.gravity = 5

    def run(self):

        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("Comic Sans MS", 65)
        while True:

            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
                    self.jump = 12
                    self.gravity = 5
                    self.jumpSpeed = 10

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.wallUp, (self.wallx, 360 + self.gap - self.offset))
            self.screen.blit(self.wallDown, (self.wallx, 0 - self.gap - self.offset))
            self.screen.blit(font.render(str(self.counter), -1, (255, 255, 255)), (200, 50))
            if self.dead:
                self.sprite = 2
            elif self.jump:
                self.sprite = 1
            self.screen.blit(self.fishSprites[self.sprite], (70, self.fishY))
            if not self.dead:
                self.sprite = 1

            self.updateWalls()
            self.fishUpdate()
            pygame.display.update()


if __name__ == "__main__":
    FlappyFish().run()
