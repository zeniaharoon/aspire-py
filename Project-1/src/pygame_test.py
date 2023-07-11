'''
Author: Zenia Haroon

Date: 7/10/23

Draws primitive shapes, imports a sprite, and takes user input to control it
'''
import pygame
import math

imp = pygame.image.load("d660e1277aab7c268b718b4572f88389.jpg")

pygame.init()

#Clock
clock = pygame.time.Clock()
dt = 0

#RGB colors
BLACK = (0,0,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
GREEN = (0,255,0)
PURPLE = (255,0,255)
RED = (255,0,0)
WHITE = (255,255,255)

wn_width = 500
wn_height = 400
wn = pygame.display.set_mode((wn_width, wn_height))
pygame.display.set_caption("Pygame testing")
player_pos = pygame.Vector2(wn_width/2,wn_height/2)

#while loop
state = True
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    wn.fill(WHITE)

    #Line
    startX = 0; startY = 270; endX = wn_width; endY = 150; width = 5
    pygame.draw.line(wn, BLACK, (startX, startY), (endX, endY))

    #Filled rectangle
    X = 100; Y = 120; width = 50; height = 30
    pygame.draw.rect(wn, RED, (X,Y, width, height))

    #Open rectangle
    X = 250; Y = 240; width = 50; height = 30; linewidth = 3
    pygame.draw.rect(wn, RED, (X, Y, width, height), linewidth)    

    #Filled square
    X = 300; Y = 80; width = 50; height = 50
    pygame.draw.rect(wn, GREEN, (X, Y, width, height))

    #Filled circle
    X = 200; Y = 150; radius = 20
    pygame.draw.circle(wn, BLUE, (X,Y), radius)

    #Open circle
    X = 200; Y = 300; radius = 20; width = 3
    pygame.draw.circle(wn, BLUE, (X,Y), radius, width)

    #Filled elipse
    X = 350; Y = 260; width = 60; height = 40
    pygame.draw.ellipse(wn, PURPLE, (X,Y, width, height))

    #Arc. This is an elliptical arc
    X = 100; Y = 260; width = 60; height = 40; startAngle = 0; endAngle = math.pi/2; lineWidth = 5
    pygame.draw.arc(wn, GREEN, (X,Y, width, height), startAngle, endAngle, lineWidth)

    #Open triangle
    X1 = 200; Y1 = 100; X2 = 120; Y2 = 200; X3 = 280; Y3 = 180; width = 5
    pygame.draw.polygon(wn, CYAN, [[X1,Y1], [X2, Y2], [X3, Y3]], width)    
    
    wn.blit(imp,player_pos)
    pygame.display.update()
    dt = clock.tick(30)/1000

    pygame.display.flip()


pygame.quit()
quit()
