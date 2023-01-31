import pygame
pygame.init()

from point import Point

taille_screen = [1200,600]

pygame.display.set_caption("Moteur 3D")
screen = pygame.display.set_mode(taille_screen, pygame.RESIZABLE)
pygame.mouse.set_visible(False)

distance_a_l_ecran = 3
velocity_move = 0.05
size_cursor = 2
points = []

# elements
for x in range(8):
    for z in range(8):
        points.append(Point(screen, (-6+2*x,2,2+2*z), distance_a_l_ecran, 0))
# cube
points.append(Point(screen, (0,0,0+20), distance_a_l_ecran, 1))
points.append(Point(screen, (0,0,5+20), distance_a_l_ecran, 1))
points.append(Point(screen, (0,5,0+20), distance_a_l_ecran, 1))
points.append(Point(screen, (0,5,5+20), distance_a_l_ecran, 1))
points.append(Point(screen, (5,0,0+20), distance_a_l_ecran, 1))
points.append(Point(screen, (5,0,5+20), distance_a_l_ecran, 1))
points.append(Point(screen, (5,5,0+20), distance_a_l_ecran, 1))
points.append(Point(screen, (5,5,5+20), distance_a_l_ecran, 1))


running = True
while running :
    
    # remplie le screen de noir
    screen.fill(0)
    # gère les déplacements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z] :
        for i in points : i.z -= velocity_move
    elif keys[pygame.K_s] :
        for i in points : i.z += velocity_move
    if keys[pygame.K_q] :
        for i in points : i.x += velocity_move
    elif keys[pygame.K_d] :
        for i in points : i.x -= velocity_move
    if keys[pygame.K_SPACE] :
        for i in points : i.y += velocity_move
    elif keys[pygame.K_LSHIFT] :
        for i in points : i.y -= velocity_move
    elif keys[pygame.K_LSHIFT] :
        for i in points : i.y -= velocity_move
    
    # gère les mouvements de cam
    pos_x = pygame.mouse.get_pos()[0] - screen.get_width()/2
    if pos_x < 0 :
        pygame.mouse.set_pos((screen.get_width()/2, screen.get_height()/2))
        for i in points : i.turn_right(screen)
    elif pos_x > 0 :
        pygame.mouse.set_pos((screen.get_width()/2, screen.get_height()/2))
        for i in points : i.turn_left(screen)
    
    # gère les mouvements de cam
    """
    pos_y = pygame.mouse.get_pos()[1] - screen.get_height()/2
    if pos_y < 0 :
        pygame.mouse.set_pos((screen.get_width()/2, screen.get_height()/2))
        for i in points : i.turn_up(screen)
    elif pos_y > 0 :
        pygame.mouse.set_pos((screen.get_width()/2, screen.get_height()/2))
        for i in points : i.turn_down(screen)"""
    
    
    # dessine les points
    for i in points : i.draw(screen)
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