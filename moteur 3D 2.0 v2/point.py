from math import sqrt, sin, cos, asin, acos, pi
import pygame

class Point :
    
    def __init__(self, coos, vitesse_mouv, vitesse_turn, distance_a_l_ecran, original_size):
        self.coos = coos
        self.x = self.coos[0]
        self.y = self.coos[1]
        self.z = self.coos[2]
        self.vitesse_mouv = vitesse_mouv
        self.vitesse_turn = vitesse_turn
        self.distance_a_l_ecran = distance_a_l_ecran
        
        self.color = (0,255,255)
        self.original_size = original_size
        
        self.x_screen = 0
        self.y_screen = 0
    
    def update_data(self, screen) :
        self.distance_xyz = sqrt((abs(self.x+0)**2)+(abs(self.z+0)**2))
        self.distance_xyz = sqrt((abs(self.distance_xyz)**2)+(abs(self.y+0)**2))
        self.point_screen_size = self.original_size/self.distance_xyz
        
        self.distance_xz = sqrt((self.x**2)+(self.z**2))
        self.alpha_x = asin(self.x/self.distance_xz)
        self.x_screen = screen.get_width()/2 + self.alpha_x*screen.get_width()*0.4
        
        self.distance_yz = sqrt((self.y**2)+(self.z**2))
        self.alpha_y = asin(self.y/self.distance_yz)
        self.y_screen = screen.get_height()/2 + self.alpha_y*screen.get_width()*0.4
    
    def turn_right(self) :
        if self.z >= 0 :
            self.distance_xz = sqrt((self.x**2)+(self.z**2))
            self.alpha = acos(self.x/self.distance_xz)
            self.x = self.distance_xz*cos(self.alpha - self.vitesse_turn)
            self.z = self.distance_xz*sin(self.alpha - self.vitesse_turn)
        
        else :
            self.distance_xz = sqrt((self.x**2)+(self.z**2))
            self.alpha = -acos(self.x/self.distance_xz)
            self.x = self.distance_xz*cos(self.alpha - self.vitesse_turn)
            self.z = self.distance_xz*sin(self.alpha - self.vitesse_turn)
        
    def turn_left(self) :
        if self.z >= 0 :
            self.distance_xz = sqrt((self.x**2)+(self.z**2))
            self.alpha = acos(self.x/self.distance_xz)
            self.x = self.distance_xz*cos(self.alpha + self.vitesse_turn)
            self.z = self.distance_xz*sin(self.alpha + self.vitesse_turn)
        else :
            self.distance_xz = sqrt((self.x**2)+(self.z**2))
            self.alpha = -acos(self.x/self.distance_xz)
            self.x = self.distance_xz*cos(self.alpha + self.vitesse_turn)
            self.z = self.distance_xz*sin(self.alpha + self.vitesse_turn)
    def turn_up(self) : pass
    def turn_down(self) : pass
    
    def move_forward(self) : self.z -= self.vitesse_mouv
    def move_backward(self) : self.z += self.vitesse_mouv
    def move_right(self) : self.x -= self.vitesse_mouv
    def move_left(self) : self.x += self.vitesse_mouv
    def move_up(self) : self.y += self.vitesse_mouv
    def move_down(self) : self.y -= self.vitesse_mouv
    
    def draw(self, screen) :
        self.update_data(screen)
        if self.z >= 0 :
            pygame.draw.circle(screen, self.color, [self.x_screen, self.y_screen], self.point_screen_size)