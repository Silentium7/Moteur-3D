import pygame
pygame.init()

from point import Point
from surface import Surface

taille_screen = [1200,600]

pygame.display.set_caption("Moteur 3D")
screen = pygame.display.set_mode(taille_screen, pygame.RESIZABLE)
pygame.mouse.set_visible(False)

distance_a_l_ecran = 3
velocity_move = 0.05
size_cursor = 2
elements = []


# cube
elements.append(Point(screen, (0,0,0+20), distance_a_l_ecran, 0, "point"))
elements.append(Point(screen, (0,0,5+20), distance_a_l_ecran, 0, "point"))
elements.append(Point(screen, (0,5,0+20), distance_a_l_ecran, 0, "point"))
elements.append(Point(screen, (0,5,5+20), distance_a_l_ecran, 0, "point"))
elements.append(Point(screen, (5,0,0+20), distance_a_l_ecran, 0, "point"))
elements.append(Point(screen, (5,0,5+20), distance_a_l_ecran, 0, "point"))
elements.append(Point(screen, (5,5,0+20), distance_a_l_ecran, 0, "point"))
elements.append(Point(screen, (5,5,5+20), distance_a_l_ecran, 0, "point"))

# surface
points_surface = [[20,5,20], [15,5,20], [17.5,0,20]]
points_surface = [[0,0,20],[0,0,25],[0,5,25],[0,5,20]]
# triangle
triangle = Surface(screen, points_surface, distance_a_l_ecran, "surface", velocity_move)
elements.append(triangle)


# 3 points de ma surface
elements.append(Point(screen, points_surface[0], distance_a_l_ecran, 1, "point"))
elements.append(Point(screen, points_surface[1], distance_a_l_ecran, 1, "point"))
elements.append(Point(screen, points_surface[2], distance_a_l_ecran, 1, "point"))


running = True
while running :
    
    # remplie le screen de noir
    screen.fill(0)
    # gère les déplacements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z] :
        for i in elements :
            if i.name == "surface" : i.move_forward()
            else : i.z -= velocity_move
    elif keys[pygame.K_s] :
        for i in elements :
            if i.name == "surface" : i.move_backward()
            else : i.z += velocity_move
    if keys[pygame.K_q] :
        for i in elements :
            if i.name == "surface" : i.move_left()
            else : i.x += velocity_move
    elif keys[pygame.K_d] :
        for i in elements :
            if i.name == "surface" : i.move_right()
            else : i.x -= velocity_move
    if keys[pygame.K_SPACE] :
        for i in elements :
            if i.name == "surface" : i.move_up()
            else : i.y += velocity_move
    elif keys[pygame.K_LSHIFT] :
        for i in elements :
            if i.name == "surface" : i.move_down()
            else : i.y -= velocity_move
    elif keys[pygame.K_LSHIFT] :
        for i in elements :
            if i.name == "surface" : i.move_forward()
            else : i.y -= velocity_move
    
    # gère les mouvements de cam
    pos_x = pygame.mouse.get_pos()[0] - screen.get_width()/2
    if pos_x < 0 :
        pygame.mouse.set_pos((screen.get_width()/2, screen.get_height()/2))
        for i in elements : i.turn_right(screen)
    elif pos_x > 0 :
        pygame.mouse.set_pos((screen.get_width()/2, screen.get_height()/2))
        for i in elements : i.turn_left(screen)
    
    
    # dessine les points
    for i in elements : i.draw(screen)
    # dessine le curseur
    pygame.draw.rect(screen, (255,255,255), [screen.get_width()/2,screen.get_height()/2, size_cursor,size_cursor])
    pygame.draw.rect(screen, (255,255,255), [screen.get_width()/2-size_cursor,screen.get_height()/2-size_cursor, size_cursor,size_cursor])
    
    # actualise le screen
    pygame.display.flip()
    
    # si on quitte  la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()