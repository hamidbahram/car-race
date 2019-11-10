import pygame  # pygame.org
import time
import random

pygame.init()

# width and height for game window
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

# colors  w3schools.com
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.display.set_caption('race car')

clock = pygame.time.Clock()

carimg = pygame.image.load('Bug.png.png')

# to get off the right, the size of the car decreases with the width of the screen  LINE 60
car_width = 48

def stuff_dodged(count):
    font = pygame.font.SysFont(None , 25)
    text = font.render('score : '+str(count) , True , red)
    gameDisplay.blit(text,(0,0))


def stuff(stuff_x, stuff_y, stuff_width, stuff_height, color):
    pygame.draw.rect(gameDisplay, color, [stuff_x, stuff_y, stuff_width, stuff_height])


# blit = for forward this image
def car(x, y):
    gameDisplay.blit(carimg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 110)
    textSurf, textRact = text_objects(text, largetext)
    textRact.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textSurf, textRact)
    pygame.display.update()

    time.sleep(2)
    game_loop()


def crash():
    message_display("YOU CRASHD")


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    #for make rect
    stuff_start_x = random.randrange(0, display_width)
    stuff_start_y = -600
    stuff_speed = 7
    stuff_width = 100
    stuff_height = 100

    dodged = 0
    

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # gameExit = True
                pygame.quit()
                quit()
            # print(event)   

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        # fill = fill the color in  background
        gameDisplay.fill(white)

        # stuff_x , stuff_y , stuff_width , stuff_height , color
        stuff(stuff_start_x, stuff_start_y, stuff_width, stuff_height, red)
        stuff_start_y += stuff_speed
        
        stuff_dodged(dodged)

        car(x, y)

        # if the car bigger than the size, close the program
        if x > display_width - car_width or x < 0:
            crash()
        # loop rect
        if stuff_start_y > display_height:
            stuff_start_y = 0 - stuff_height
            stuff_start_x = random.randrange(0, display_width)
            dodged += 1
            stuff_speed += 1
            
            # if (dodged % 5 == 0):
            #     stuff_speed += 2

        if y < stuff_start_y + stuff_height:
            if x > stuff_start_x and x < stuff_start_x + stuff_width or x + car_width > stuff_start_x and x + car_width < stuff_start_x + stuff_width:
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()