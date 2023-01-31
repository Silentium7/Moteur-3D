import pygame

class Surface:
    
    def __init__(self, points, vitesse_mouv, vitesse_turn, distance_a_l_ecran):
        self.points = points
        self.vitesse_mouv = vitesse_mouv
        self.vitesse_turn = vitesse_turn
        self.distance_a_l_ecran = distance_a_l_ecran
    
    def update_data(self, screen) :pass
    
    def turn_right(self) : pass
        
    def turn_left(self) : pass
    def turn_up(self) : pass
    def turn_down(self) : pass
    """
    def move_forward(self) : self.z -= self.vitesse_mouv
    def move_backward(self) : self.z += self.vitesse_mouv
    def move_right(self) : self.x -= self.vitesse_mouv
    def move_left(self) : self.x += self.vitesse_mouv
    def move_up(self) : self.y += self.vitesse_mouv
    def move_down(self) : self.y -= self.vitesse_mouv"""
    
    def draw(self, screen) :
        self.update_data(screen)
    
    