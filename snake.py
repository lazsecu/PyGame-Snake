import pygame
import sys
import random
import time

pygame.init()


width = 400
height = 400
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
background_color = (0, 0, 0)
pygame.display.set_caption('Snek')
screen = pygame.display.set_mode([width, height])

clock = pygame.time.Clock()
game_exit = False

font = pygame.font.SysFont(None, 25)

def snake(snakelist):
    for XnY in snakelist:
        pygame.draw.rect(screen, green, (XnY[0], XnY[1], 10, 10))
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [200, 200])

def game_loop():
    game_exit = False
    lead_x = 200
    lead_y = 200
    lead_x_change = 0
    lead_y_change = 0
    snakelist = []
    snakelength = 1



    randAppleX = round(random.randrange(0, width - 10)/10.0) * 10.0
    randAppleY = round(random.randrange(0, height - 10)/10.0) * 10.0
    game_over = False
    while not game_exit:
        while game_over == True:
            screen.fill(white)
            message_to_screen("Game over", red)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -10
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = 10
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -10
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = 10
                    lead_x_change = 0


        if lead_x >= 400 or lead_x< 0 or lead_y >= 400 or lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change


        screen.fill(background_color)
        pygame.draw.rect(screen, red, [randAppleX, randAppleY, 10, 10])
        pygame.draw.rect(screen, green, (lead_x, lead_y, 10, 10))

        snakehead= []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist) > snakelength:
            del snakelist[0]
        for eachSegment in snakelist[:-1]:
            if eachSegment == snakehead:
                game_over = True
        snake(snakelist)
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, width - 10)/10.0) * 10.0
            randAppleY = round(random.randrange(0, height - 10)/10.0) * 10.0
            snakelength += 1

        clock.tick(10)

game_loop()
