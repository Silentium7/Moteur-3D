import pygame
pygame.init()

from point import Point
from surface import Surface

taille_screen = [600,600]

pygame.display.set_caption("Moteur 3D")
screen = pygame.display.set_mode(taille_screen, pygame.RESIZABLE)
pygame.mouse.set_visible(False)

distance_a_l_ecran = 1
vitesse = 0.01
vitesse_turn = 0.04

size_points = 10

elements = []

elements.append(Point([1,0,2], vitesse, vitesse_turn, distance_a_l_ecran, size_points))
# """
taille_cube = 1
elements.append(Point([1,0,2 + taille_cube], vitesse, vitesse_turn, distance_a_l_ecran, size_points))
elements.append(Point([1,0 + taille_cube,2], vitesse, vitesse_turn, distance_a_l_ecran, size_points))
elements.append(Point([1,0 + taille_cube,2 + taille_cube], vitesse, vitesse_turn, distance_a_l_ecran, size_points))
elements.append(Point([1 + taille_cube,0,2], vitesse, vitesse_turn, distance_a_l_ecran, size_points))
elements.append(Point([1 + taille_cube,0,2 + taille_cube], vitesse, vitesse_turn, distance_a_l_ecran, size_points))
elements.append(Point([1 + taille_cube,0 + taille_cube,2], vitesse, vitesse_turn, distance_a_l_ecran, size_points))
elements.append(Point([1 + taille_cube,0 + taille_cube,2 + taille_cube], vitesse, vitesse_turn, distance_a_l_ecran, size_points))
# """

elements.append(Surface([[1,0,2],[1,0,2 + taille_cube],[1,0 + taille_cube,2]], vitesse, vitesse_turn, distance_a_l_ecran))

running = True
while running :
    
    # remplie le screen de noir
    screen.fill(0)
    
    # gère les déplacements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z] :
        for i in elements : i.move_forward()
    elif keys[pygame.K_s] :
        for i in elements : i.move_backward()
    if keys[pygame.K_d] :
        for i in elements : i.move_right()
    elif keys[pygame.K_q] :
        for i in elements : i.move_left()
    if keys[pygame.K_SPACE] :
        for i in elements : i.move_up()
    elif keys[pygame.K_LSHIFT] :
        for i in elements : i.move_down()
    
    # mouvements de cam sur l'axe y
    pos_x = pygame.mouse.get_pos()[0] - screen.get_width()/2
    if pos_x < 0 :
        pygame.mouse.set_pos((screen.get_width()/2, screen.get_height()/2))
        for i in elements : i.turn_right()
    elif pos_x > 0 :
        pygame.mouse.set_pos((screen.get_width()/2, screen.get_height()/2))
        for i in elements : i.turn_left()
    """
    elements.append(Point([1 + taille_cube,0,2], vitesse, vitesse_turn, distance_a_l_ecran, size_points))
    elements.append(Point([1 + taille_cube,0,2 + taille_cube], vitesse, vitesse_turn, distance_a_l_ecran, size_points))
    elements.append(Point([1 + taille_cube,0 + taille_cube,2], vitesse, vitesse_turn, distance_a_l_ecran, size_points))
    elements.append(Point([1 + taille_cube,0 + taille_cube,2 + taille_cube], vitesse, vitesse_turn, distance_a_l_ecran, size_points))
    """
    
    # pygame.draw.polygon(screen, (0,0,255), [(elements[0].x_screen, elements[0].y_screen),(elements[1].x_screen, elements[1].y_screen),(elements[2].x_screen, elements[2].y_screen)])
    
    
    # dessine les elements
    for i in elements : i.draw(screen)
    
    # actualise le screen
    pygame.display.flip()
    
    # si on quitte  la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()