import pygame
import math
import random
from random import randint, choice

#Class
class Player(object):
    #Constructor
    def __init__(self,score=0,health=3,high_score=0,need_rules=True):
        self.score = score
        self.health = health
        self.high_score = high_score
        self.need_rules = need_rules

    #Update high_score?
    def update(self, points):
        self.score += points
        #Update High Score
        if self.score > self.high_score: self.high_score = self.score

class Fruit(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        self.type = type
        self.display_state = []
        self.is_popped = False
        self.image_index = 0.0
        
        #Add each Image
        if type == 'apple':
            self.display_state.append(pygame.image.load('./images/fruit/apple.png').convert_alpha())
        elif type == 'grape':
            self.display_state.append(pygame.image.load('./images/fruit/grape.png').convert_alpha())
        elif type == 'orange':
            self.display_state.append(pygame.image.load('./images/fruit/orange.png').convert_alpha())
        elif type == 'strawberry':
            self.display_state.append(pygame.image.load('./images/fruit/strawberry.png').convert_alpha())
        elif type == 'watermelon':
            self.display_state.append(pygame.image.load('./images/fruit/watermelon.png').convert_alpha())

        #Set First Image
        self.image = self.display_state[0]
        self.rect = self.image.get_rect(center = (random.randint(50,750), random.randint(-100,-20)))

        #Load in other images
        self.display_state.append(pygame.image.load('./images/fruit/popped1.png').convert_alpha())
        self.display_state.append(pygame.image.load('./images/fruit/popped2.png').convert_alpha())
        self.display_state.append(pygame.image.load('./images/fruit/popped3.png').convert_alpha())
        

    def update(self):
        self.rect.y += game_speed     
        self.destroy()
        if self.is_popped:
            self.image_index += 0.1
            #Kill the fruit
            if self.image_index >= 1.5:
                self.kill()
            elif self.image_index >= 1:
                self.image = self.display_state[3]

            elif self.image_index >= 0.5:
                self.image = self.display_state[2]


    def destroy(self):
        if self.rect.y > 650:
            player.health -= 1
            self.kill()
    
    def pop(self):
        self.is_popped = True
        self.image = self.display_state[1]

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.is_explode = False

        bomb = pygame.image.load('./images/bomb/bomb.png').convert_alpha()
        exp1 = pygame.image.load('./images/bomb/ka.png').convert_alpha()
        exp2 = pygame.image.load('./images/bomb/boom.png').convert_alpha()
        self.bomb_state = [bomb,exp1,exp2]
        self.image_index = 0.0

        self.image = self.bomb_state[0]
        self.rect = self.image.get_rect(center = (random.randint(50,750), random.randint(-100,-20)))
        
    def update(self):
        self.rect.y += game_speed
        self.destroy()

        if self.is_explode:
            self.image_index += 0.1
            #Kill the bomb
            if self.image_index >= 1.5:
                player.health -= 1
                self.kill()

            #Move Back to ka
            elif self.image_index >= 1:
                self.image = self.bomb_state[1]
            #Move to boom
            elif self.image_index >= 0.5:
                self.image = self.bomb_state[2]

    def destroy(self):
        if self.rect.y > 650:
            self.kill()

    def explode(self):
        self.image = self.bomb_state[1]
        self.is_explode = True


#FUNCTUIONS
def display_menu(player):
    #Red 'Fruit'
    title_surface1 = title_font.render('Fruit',False, (254,9,4))
    title_surface1 = pygame.transform.scale2x(title_surface1)
    title_rect1 = title_surface1.get_rect(topleft = (32, 257))
    screen.blit(title_surface1,title_rect1)

    #Red 'Popper'
    title_surface2 = title_font.render('Popper', False, (254,9,4))
    title_surface2 = pygame.transform.scale2x(title_surface2)
    title_rect2 = title_surface2.get_rect(topleft = (62,347))
    screen.blit(title_surface2,title_rect2)

    #Orange 'Fruit'
    title_surface3 = title_font.render('Fruit',False, (254,163,6))
    title_surface3 = pygame.transform.scale2x(title_surface3)
    title_rect3 = title_surface3.get_rect(topleft = (25, 250))
    screen.blit(title_surface3,title_rect3)

    #Orange 'Popper'
    title_surface4 = title_font.render('Popper', False, (254,163,6))
    title_surface4 = pygame.transform.scale2x(title_surface4)
    title_rect4 = title_surface4.get_rect(topleft = (55,340))
    screen.blit(title_surface4,title_rect4)

    #Draw a line
    pygame.draw.line(screen,(254,9,4),(24,454),(434,454),5)
    pygame.draw.line(screen,(254,163,6),(20,450),(430,450),5)

    #My Signature
    signature_surface1 = pixel_font.render('A Game by Reed Miller',False,(254,9,4))
    signature_rect1 = signature_surface1.get_rect(topleft = (42,472))
    screen.blit(signature_surface1,signature_rect1)

    signature_surface2 = pixel_font.render('A Game by Reed Miller',False,(254,163,6))
    signature_rect2 = signature_surface2.get_rect(topleft = (40,470))
    screen.blit(signature_surface2,signature_rect2)

    #Draw a button
    start_menu_surf = pixel_font.render('Press Any Button to Play',False,(254,9,4))
    start_menu_rect = start_menu_surf.get_rect(center = (400, 550))
    pygame.draw.rect(screen,(254,163,6),start_menu_rect, 16, 8)
    screen.blit(start_menu_surf,start_menu_rect)

    #Display High Score
    if(player.high_score != 0):
        high_score_surf = pixel_font.render(f'High Score: {player.high_score}',False,(254,9,4))
        high_score_rect = high_score_surf.get_rect(topright = (752,17))
        screen.blit(high_score_surf,high_score_rect)
        high_score_surf = pixel_font.render(f'High Score: {player.high_score}',False,(254,163,6))
        high_score_rect = high_score_surf.get_rect(topright = (750,15))
        screen.blit(high_score_surf,high_score_rect)

def display_rules():
    #Rules title
    rules_title_surf = title_font.render('Game Rules',False,'Black')  
    rules_title_surf = pygame.transform.scale2x(rules_title_surf)
    rules_title_rect = rules_title_surf.get_rect(center = (400, 85))
    screen.blit(rules_title_surf,rules_title_rect)

    #Draw a line
    pygame.draw.line(screen,'Black',(50,125),(750,125),10)

    #Rule 1
    rule1_surf = text_font.render("1) Use your mouse and 'click' to pop the fruit",False,'Black')
    rule1_rect = rule1_surf.get_rect(center = (400,160))
    screen.blit(rule1_surf,rule1_rect)

    #Rule 2
    rule2_surf = text_font.render("2) You have 3 lives, DON'T let fruit go off screen",False,'Black')
    rule2_rect = rule2_surf.get_rect(center = (400,240))
    screen.blit(rule2_surf,rule2_rect)

    #Rule 3
    rule3_surf = text_font.render("3) DON'T click a bomb! That will cost you a life",False,'Black')
    rule3_rect = rule3_surf.get_rect(center = (400,320))
    screen.blit(rule3_surf,rule3_rect)

    #Rule 4
    rule4_surf = text_font.render("4) You get points for popping fruit, so get to it!",False,'Black')
    rule4_rect = rule4_surf.get_rect(center = (400,400))
    screen.blit(rule4_surf,rule4_rect)
    
    #Next Button
    cont_surf = text_font.render('Press Any Button to Play',False,'Black')
    cont_rect = cont_surf.get_rect(center = (400, 500))
    screen.blit(cont_surf,cont_rect)
    pygame.draw.line(screen,'Black',(220,530),(580,530),5)

def display_HUD(player):
    #Display First Heart
    heart_surf = pygame.image.load('./images/heart.png').convert_alpha()
    heart1_rect = heart_surf.get_rect(topleft = (5,7))
    screen.blit(heart_surf,heart1_rect)

    #Display Second Heart
    if player.health > 1:
        heart2_rect = heart_surf.get_rect(topleft = (65,7))
        screen.blit(heart_surf,heart2_rect)
    
    #Display Third Heart
    if player.health > 2:
        heart2_rect = heart_surf.get_rect(topleft = (125,7))
        screen.blit(heart_surf,heart2_rect)

    #Display Highscore & Score
    high_score_surf = text_font.render(f'High Score: {player.high_score}',False,(242,235,235))
    high_score_rect = high_score_surf.get_rect(topright = (780,40))
    screen.blit(high_score_surf,high_score_rect)

    score_surf = text_font.render(f'Score: {player.score}',False,(242,235,235))
    score_rect = score_surf.get_rect(topright = (780,10))
    screen.blit(score_surf,score_rect)

#Initilize Game
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Fruit Popper')
clock = pygame.time.Clock()
#Create the Player
player = Player()

#Create the Obstacle Groups
fruit_group = pygame.sprite.Group()
bomb_group = pygame.sprite.Group()

#Game States
running = True
game_state = 'Menu'            #Menu - Rules - Active 
game_speed = 5

#Timer
obstacle_timer = pygame.USEREVENT+ 1
pygame.time.set_timer(obstacle_timer, 1500)

#Import and Run Sounds
music = pygame.mixer.Sound('./audio/Background.mp3')
music.set_volume(0.5)
music.play(loops = -1)

click = pygame.mixer.Sound('./audio/click.mp3')
click.set_volume(0.5)

pop1 = pygame.mixer.Sound('./audio/pop1.mp3')
pop1.set_volume(0.7)
pop2 = pygame.mixer.Sound('./audio/pop2.mp3')
pop2.set_volume(0.7)
pop3 = pygame.mixer.Sound('./audio/pop3.mp3')
pop3.set_volume(0.7)

explosion = pygame.mixer.Sound('./audio/Explosion.mp3')
explosion.set_volume(0.6)

#Fonts
pixel_font = pygame.font.Font('./font/Pixeltype.ttf',50) 
title_font = pygame.font.Font('./font/Title.ttf',50)
text_font = pygame.font.Font('./font/Text.ttf',25)

#MAIN GAME SURFACES/RECTS
background_surface = pygame.image.load('./images/dojo.png').convert()

#MENU SCREEN SURFACES/RECTS
menu_surface = pygame.image.load('./images/menu.png').convert()

#Main Loop
while running:
    #Event Loop
    for event in pygame.event.get():
        #Game is Quit
        if event.type == pygame.QUIT:
            running = False

        #Active Game Input
        if game_state == 'Active':
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Pop Sound Effect
                r = random.randint(0,2)
                if r == 0: pop1.play()
                if r == 1: pop2.play()
                if r == 2: pop3.play()

                #Check for collision
                for fruit in fruit_group:
                    if fruit.rect.collidepoint(event.pos):
                        player.update(20)
                        fruit.pop()
                        #Speed Up game
                        if player.score % 200 == 0:
                           game_speed += 1

                #Now Check for Bomb collision
                for bomb in bomb_group:
                    if bomb.rect.collidepoint(event.pos):
                        bomb.explode()
                        explosion.play()


        #Adding obstacles
        if game_state == 'Active' and event.type == obstacle_timer:
            if random.randint(0,7):
                fruit_group.add(Fruit(choice(['apple','orange','grape','strawberry','watermelon'])))
            else:
                bomb_group.add(Bomb())

                
        #Menu Screen Input
        elif game_state == 'Menu':
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                click.play()
                #Kill All Fruits
                for fruit in fruit_group:
                    fruit.kill()
                #Kill All bombs
                for bomb in bomb_group:
                    bomb.kill()

                if player.need_rules: game_state = 'Rules'
                else: 
                    game_state = 'Active'
                    player.score = 0
                    player.health = 3
                    game_speed = 5


        #Rules 
        elif game_state == 'Rules':
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                click.play()
                game_state = 'Active'
                player.need_rules = False
                player.score = 0
                player.health = 3
                game_speed = 5

    #Main Game
    if game_state == 'Active':
        screen.blit(background_surface,(0,0))
        display_HUD(player)

        #Draw Obstacles
        fruit_group.draw(screen)
        fruit_group.update()
        bomb_group.draw(screen)
        bomb_group.update()
    
    #Menu
    elif game_state == 'Menu':
        screen.blit(menu_surface,(0,0))
        display_menu(player)

    #Rules
    else:
        screen.fill((14,148,117))
        display_rules()


    #Check Player Health
    if player.health < 1:
        game_state = 'Menu'

    pygame.display.update()
    clock.tick(60)      #Set fps to 60

#Quit Game
pygame.quit()