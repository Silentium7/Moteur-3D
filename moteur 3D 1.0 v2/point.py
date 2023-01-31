#---------------------------------------------------------------------------------------#
# CETTE PARTIE EST UNE PARTIE MODIFIEE, A LA FIN, LA REMPLACER PAR LE FICHIER DE LA V.1 #
#---------------------------------------------------------------------------------------#

from math import sqrt, radians, degrees, cos, sin, acos, asin
from random import randint
import pygame
from time import sleep


class Point :
    
    def __init__(self, screen, coos, distance_a_l_ecran, ID, name):
        
        self.id = ID
        self.name = name
        
        self.x = coos[0]
        self.y = coos[1]
        self.z = coos[2]
        
        self.x_screen = screen.get_width()/2
        self.y_screen = screen.get_height()/2
        
        self.distance_a_l_ecran = distance_a_l_ecran
        self.taille_originale = 50
        self.size = 0
        
        self.distance = 1
        self.alpha = 0
        self.vitesse_turn = 0.1
        
        if self.id == 0 : self.color = (0,255,255)
        elif self.id == 1 : self.color = (255,255,0)
        
        
        
    def turn_right(self, screen):
        if self.z >= 0 :
            self.distance_x_z = sqrt((self.x**2)+(self.z**2))
            self.alpha = acos(self.x/self.distance_x_z)
            self.x = self.distance_x_z*cos(self.alpha - self.vitesse_turn)
            self.z = self.distance_x_z*sin(self.alpha - self.vitesse_turn)
        else :
            self.distance_x_z = sqrt((self.x**2)+(self.z**2))
            self.alpha = -acos(self.x/self.distance_x_z)
            self.x = self.distance_x_z*cos(self.alpha - self.vitesse_turn)
            self.z = self.distance_x_z*sin(self.alpha - self.vitesse_turn)
    def turn_left(self, screen):
        if self.z >= 0 :
            self.distance_x_z = sqrt((self.x**2)+(self.z**2))
            self.alpha = acos(self.x/self.distance_x_z)
            self.x = self.distance_x_z*cos(self.alpha + self.vitesse_turn)
            self.z = self.distance_x_z*sin(self.alpha + self.vitesse_turn)
        else :
            self.distance_x_z = sqrt((self.x**2)+(self.z**2))
            self.alpha = -acos(self.x/self.distance_x_z)
            self.x = self.distance_x_z*cos(self.alpha + self.vitesse_turn)
            self.z = self.distance_x_z*sin(self.alpha + self.vitesse_turn)



    
    def draw(self, screen):
        
        self.distance = sqrt((abs(self.x+0)**2)+(abs(self.z+0)**2))
        self.distance = sqrt((abs(self.distance)**2)+(abs(self.y+0)**2))
        self.size = self.taille_originale/self.distance
        
        self.x_screen = (self.x*self.distance_a_l_ecran)/(self.z)*100+screen.get_width()/2
        self.y_screen = (self.y*self.distance_a_l_ecran)/(self.z)*100+screen.get_height()/2
        if self.z > 0 :
            pygame.draw.circle(screen, self.color, [self.x_screen, self.y_screen], self.size)
