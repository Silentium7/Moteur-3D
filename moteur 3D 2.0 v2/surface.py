from math import sqrt, sin, cos, asin, acos, pi, radians, degrees
import pygame

class Surface :
    
    def __init__(self, coos, vitesse_mouv, vitesse_turn, distance_a_l_ecran):
        self.coos = coos
        self.vitesse_mouv = vitesse_mouv
        self.vitesse_turn = vitesse_turn
        self.distance_a_l_ecran = distance_a_l_ecran
        
        self.color = (0,0,255)
        
        self.points_screen = []
        print(self.coos)
    
    def update_data(self, screen) :
        self.points_screen = []
        for i in range (len(self.coos)) :            
            self.distance_xz = sqrt((self.coos[i][0]**2)+(self.coos[i][2]**2))
            self.alpha_x = asin(self.coos[i][0]/self.distance_xz)
            self.x_screen = screen.get_width()/2 + self.alpha_x*screen.get_width()*0.4
            
            self.distance_yz = sqrt((self.coos[i][1]**2)+(self.coos[i][2]**2))
            self.alpha_y = asin(self.coos[i][1]/self.distance_yz)
            self.y_screen = screen.get_height()/2 + self.alpha_y*screen.get_width()*0.4
            self.points_screen.append([self.x_screen,self.y_screen])
    
    def turn_right(self) :
        for i in range(len(self.coos)):
            if self.coos[i][2] >= 0 :
                self.distance_xz = sqrt((self.coos[i][0]**2)+(self.coos[i][2]**2))
                self.alpha = acos(self.coos[i][0]/self.distance_xz)
                self.coos[i][0] = self.distance_xz*cos(self.alpha - self.vitesse_turn)
                self.coos[i][2] = self.distance_xz*sin(self.alpha - self.vitesse_turn)
            
            else :
                self.distance_xz = sqrt((self.coos[i][0]**2)+(self.coos[i][2]**2))
                self.alpha = -acos(self.coos[i][0]/self.distance_xz)
                self.coos[i][0] = self.distance_xz*cos(self.alpha - self.vitesse_turn)
                self.coos[i][2] = self.distance_xz*sin(self.alpha - self.vitesse_turn)
        
    def turn_left(self) :
        for i in range(len(self.coos)):
            if self.coos[i][2] >= 0 :
                self.distance_xz = sqrt((self.coos[i][0]**2)+(self.coos[i][2]**2))
                self.alpha = acos(self.coos[i][0]/self.distance_xz)
                self.coos[i][0] = self.distance_xz*cos(self.alpha + self.vitesse_turn)
                self.coos[i][2] = self.distance_xz*sin(self.alpha + self.vitesse_turn)
            
            else :
                self.distance_xz = sqrt((self.coos[i][0]**2)+(self.coos[i][2]**2))
                self.alpha = -acos(self.coos[i][0]/self.distance_xz)
                self.coos[i][0] = self.distance_xz*cos(self.alpha + self.vitesse_turn)
                self.coos[i][2] = self.distance_xz*sin(self.alpha + self.vitesse_turn)
    
    def turn_up(self) : pass
    def turn_down(self) : pass
    
    def move_forward(self) :
        for i in range(len(self.coos)): self.coos[i][2] -= self.vitesse_mouv
    def move_backward(self) :
        for i in range(len(self.coos)): self.coos[i][2] += self.vitesse_mouv
    def move_right(self) :
        for i in range(len(self.coos)): self.coos[i][0] -= self.vitesse_mouv
    def move_left(self) :
        for i in range(len(self.coos)): self.coos[i][0] += self.vitesse_mouv
    def move_up(self) :
        for i in range(len(self.coos)): self.coos[i][1] += self.vitesse_mouv
    def move_down(self) :
        for i in range(len(self.coos)): self.coos[i][1] -= self.vitesse_mouv
    
    def draw(self, screen) :
        self.update_data(screen)
        
        afficher = True
        for i in range(len(self.coos)):
            if self.coos[i][2] < 0 : afficher = False
            """
            self.distance_x_z = sqrt((self.coos[i][0]**2)+(self.coos[i][2]**2))
            self.alpha = asin(self.coos[i][0]/self.distance_x_z)
            if i == 1 : print(degrees(self.alpha))
            if degrees(self.alpha) > 180-(90-72) : pass
                
                # print("ok")
            
                # self.points_screen[i] = [-self.points_screen[i][0] + screen.get_width(), -self.points_screen[i][1] + screen.get_width()]
            """
            # if self.ccos[]
        if afficher : pygame.draw.polygon(screen, self.color, self.points_screen)