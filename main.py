import math
import random
import pygame
import sys

# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Tutorial")

clock = pygame.time.Clock()





class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.x = 400
        self.y = 575
        self.radius = 25
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA, 32) 
        self.image = self.image.convert_alpha()
        self.colors = [(128, 128, 128, 128), (255, 0, 0, 128), (0, 255, 0, 128), (0, 0, 255, 128), (255, 255, 0, 128), (255, 0, 255, 128), (0, 255, 255, 128), (255, 255, 255, 128)]
        self.color = (128, 128, 128, 128)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.rect_center = (self.x, self.y)
        # self.deltax = 0
        self.deltay = 0
        self.index = 0
        self.grounded = True

    def move(self, t1mer, up):
        if up == True and self.grounded == True:
            print("AAAA")
            if t1mer >275:
                t1mer = 275
            for life in range(t1mer):
            
                print(t1mer)
                self.deltay -=2

            self.y += self.deltay
            self.rect_center = (self.x, self.y)
            self.rect = self.image.get_rect(center = (self.x, self.y))
            t1mer = 0
        
        
            self.grounded = False


    def gravity(self):
        if self.grounded == False:
            self.y += 1
            self.rect_center = (self.x, self.y)
            self.rect = self.image.get_rect(center = (self.x, self.y))
            
        if self.y >= 575:
            self.grounded = True
            self.y = 575
            self.deltay = 0




    def change_color(self, left, right):
        length = len(self.colors)

        if left == True:
            self.index -= 1
            self.index = self.index%length

            self.color = self.colors[self.index]
            pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

        elif right == True:
            self.index += 1
            self.index = self.index%length

            self.color = self.colors[self.index]
            pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)






















player = Ball()


objects = pygame.sprite.Group()

objects.add(player)




count = 0
counter = 0
var = False
running = True
while running:
    count +=1

    
    for event in pygame.event.get(): # pygame.event.get()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                var = True
                

            if event.key == pygame.K_LEFT:
                player.change_color(True, False)
            if event.key == pygame.K_RIGHT:
                player.change_color(False, True)


        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            var = False
            player.move(counter, True)
            counter = 0


        if event.type == pygame.QUIT:
            running = False

    if var == True:
        counter +=1

    keys = pygame.key.get_pressed()

    player.gravity()

    if keys[pygame.K_UP]:
        pass

    if keys[pygame.K_LEFT]:
        pass

    if keys[pygame.K_RIGHT]:
        pass



    






    screen.fill((0, 0, 0, 0))

    objects.draw(screen)

    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()
