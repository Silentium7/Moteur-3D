from math import sqrt, radians, degrees, cos, sin, acos, asin
from random import randint
import pygame
from time import sleep


class Surface :
    
    def __init__(self, screen, points, distance_a_l_ecran, name, velocity):
        
        self.points_screen = [[1,1],[1,1],[1,1]]
        self.velocity = velocity
        self.points = points
        self.distance_a_l_ecran = distance_a_l_ecran
        self.name = name
        self.x_screen = screen.get_width()/2
        self.y_screen = screen.get_height()/2
        self.distance_a_l_ecran = distance_a_l_ecran
        self.distance = 1
        self.alpha = 0
        self.vitesse_turn = 0.1
        
        
    def move_forward(self):
        for i in range(len(self.points)) :
            self.points[i][2] -= self.velocity
    def move_backward(self):
        for i in range(len(self.points)) :
            self.points[i][2] += self.velocity
    def move_right(self):
        for i in range(len(self.points)) :
            self.points[i][0] -= self.velocity
    def move_left(self):
        for i in range(len(self.points)) :
            self.points[i][0] += self.velocity
    def move_up(self):
        for i in range(len(self.points)) :
            self.points[i][1] += self.velocity
    def move_down(self):
        for i in range(len(self.points)) :
            self.points[i][1] -= self.velocity
        
    def turn_right(self, screen):
        for i in range(len(self.points)) :
            if self.points[i][2] > 0 :
                self.distance_x_z = sqrt((self.points[i][0]**2)+(self.points[i][2]**2))
                self.alpha = acos(self.points[i][0]/self.distance_x_z)
                self.points[i][0] = self.distance_x_z*cos(self.alpha - self.vitesse_turn)
                self.points[i][2] = self.distance_x_z*sin(self.alpha - self.vitesse_turn)
            
            else :
                self.distance_x_z = sqrt((self.points[i][0]**2)+(self.points[i][2]**2))
                self.alpha = -acos(self.points[i][0]/self.distance_x_z)
                self.points[i][0] = self.distance_x_z*cos(self.alpha - self.vitesse_turn)
                self.points[i][2] = self.distance_x_z*sin(self.alpha - self.vitesse_turn)
    def turn_left(self, screen):
        for i in range(len(self.points)) :
            if self.points[i][2] > 0 :
                self.distance_x_z = sqrt((self.points[i][0]**2)+(self.points[i][2]**2))
                self.alpha = acos(self.points[i][0]/self.distance_x_z)
                self.points[i][0] = self.distance_x_z*cos(self.alpha + self.vitesse_turn)
                self.points[i][2] = self.distance_x_z*sin(self.alpha + self.vitesse_turn)
            else :
                self.distance_x_z = sqrt((self.points[i][0]**2)+(self.points[i][2]**2))
                self.alpha = -acos(self.points[i][0]/self.distance_x_z)
                self.points[i][0] = self.distance_x_z*cos(self.alpha + self.vitesse_turn)
                self.points[i][2] = self.distance_x_z*sin(self.alpha + self.vitesse_turn)
    
    def draw(self, screen):
        
        self.old_points = self.points_screen
        self.points_screen = []
        
        for i in range(len(self.points)) :
            self.distance = sqrt((abs(self.points[i][0]+0)**2)+(abs(self.points[i][2]+0)**2))
            self.distance = sqrt((abs(self.distance)**2)+(abs(self.points[i][1]+0)**2))
            
            self.x_screen = (self.points[i][0]*self.distance_a_l_ecran)/(self.points[i][2])*100+screen.get_width()/2
            self.y_screen = (self.points[i][1]*self.distance_a_l_ecran)/(self.points[i][2])*100+screen.get_height()/2
            self.points_screen.append([self.x_screen, self.y_screen])
        
        # print(self.points_screen)
        
        afficher = True
        
        for i in range(len(self.points_screen)) :
            if int(abs(self.points_screen[i][0])) > 10000 or int(abs(self.points_screen[i][1])) > 10000: afficher = False
        
        compteur = 0
        for i in self.points :
            if i[2] < 0 : compteur += 1
        if compteur == 3 :
            afficher = False
        
                
        for i in range(len(self.points)) :
            self.distance_x_z = sqrt((self.points[i][0]**2)+(self.points[i][2]**2))
            self.alpha = acos(self.points[i][0]/self.distance_x_z)
            if self.points[i][2] < 0 or radians(-90) > self.alpha > radians(90) :
                self.points_screen[i] = [-self.points_screen[i][0] + screen.get_width(), -self.points_screen[i][1] + screen.get_width()]

    
        
        if afficher : pygame.draw.polygon(screen, (0,0,255), self.points_screen)
        

