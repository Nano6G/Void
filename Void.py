import sys
import pygame
import time
import os
import random
import time
import math

#Colour constants
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 155, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
lighter_blue = (0, 128, 255)
darker_blue = (0, 0, 153)
bright_green = (0, 255, 0)
grey = (128, 128, 128)
grey2 = (219, 219, 219)
teal = (0, 255, 213)
dark_green = (0, 82, 5)
orange = (255, 119, 0)
lighter_green = (67, 183, 91)
purple = (122, 29, 114)
pink = (247, 32, 228)
colour_list = [green, grey, bright_green, lighter_blue, teal, dark_green, orange, lighter_green, purple, pink]

pygame.init()
pygame.font.init()
pygame.display.init()

os.environ["SDL_VIDEO_CENTERED"]="1"
screen_w = 600
screen_h = 600
fps = 60
screen = pygame.display.set_mode([screen_w, screen_h])
pygame.display.set_caption("A Void")
clock = pygame.time.Clock()
score_font = pygame.font.SysFont('glegoo', 48)
gameover_font = pygame.font.SysFont('glegoo', 60)

light = pygame.image.load('circle.png')

class Player():
    def __init__(self):
        self.x = 300
        self.y = 300
        self.movex = 0
        self.movey = 0
        self.xy = [self.x, self.y]
        self.w = 16
        self.h = 16
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.speed = 8
        self.colour = red
    def control_x(self, direction):
        self.movex = self.speed*direction
    def control_y(self, direction):
        self.movey = self.speed*direction
    def draw(self):
        #self.player = pygame.draw.rect(screen, self.colour, [self.x, self.y, self.w, self.h], 0)
        #self.circle = pygame.draw.circle(screen, grey2, self.player.center, 150, 0)
        self.player = pygame.draw.rect(screen, self.colour, [self.x, self.y, self.w, self.h], 0)
    def update_keys(self):
        self.x += self.movex
        self.y += self.movey
        self.xy = [self.x, self.y]
    def update_mouse(self):
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.xy = [self.x, self.y]
        
class Enemy():
    def __init__(self):
        self.movex = random.uniform(-4, 4)
        self.movey = random.uniform(-4, 4)
        self.velocity = math.sqrt(self.movex**2 + self.movey**2)
        if self.movex > 0:
            self.x = random.randint(-100, 0)
        elif self.movex < 0:
            self.x = random.randint(600, 700)
        elif self.movex == 0:
            self.x = random.randint(0, 600)
        if self.movey > 0:
            self.y = random.randint(0, 250)
        elif self.movey < 0:
            self.y = random.randint(350, 600)
        elif self.movey == 0:
            self.y = random.randint(0, 600)
        #self.colour = (255, 255-(255*self.velocity/12), 0)
        width_and_height = random.randint(30, 40)
        self.width = width_and_height
        self.height = width_and_height
        self.colour = (random.randint(40, 255), random.randint(0, 255), random.randint(0, 255))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect2 = pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height], 0)
    def draw(self):
        self.rect2 = pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height], 0)
    def update(self, score):
        self.x += self.movex
        self.y += self.movey
        self.rect.x += self.movex
        self.rect.y += self.movey
        mouse = pygame.mouse.get_pos()
        if self.rect2.colliderect(player_obj.player):
            
            gameover_text = "Game Over"
            gameovertext = gameover_font.render(gameover_text, 1, lighter_blue, 150)
            gameover_rect = gameovertext.get_rect()
            gameover_rect.center = (screen_w/2, (screen_h/2)-25)
            screen.blit(gameovertext, gameover_rect)

            score_text = "Score: {0:.0f}".format(score)
            scoretext = gameover_font.render(score_text, 1, lighter_blue, 150)
            scoretext_rect = scoretext.get_rect()
            scoretext_rect.center = (screen_w/2, (screen_h/2)+25)
            screen.blit(scoretext, scoretext_rect)
        
            pygame.display.update()
            time.sleep(1.5)
            play()
            
                                         

def generate():
    for x in range(0, 1200):
            enemy_x = Enemy()
            enemies.append(enemy_x)

def play():
    global player_obj
    global enemies
    player_obj = Player()
    count = 0
    enemies = []
    generate()
    second_timer = 0
    max_second_timer = 60
    pygame.mouse.set_visible(False)
    while count < 1000:
        screen.fill(white)
        milliseconds = clock.tick(fps)

        player_obj.draw()
        
        #Primary loop for input handling.
        for event in pygame.event.get():
            if event.type == pygame.display.quit:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Handles the pressing of a key
            if event.type == pygame.KEYDOWN:
                if event.key == ord("r"):
                    generate()
                    play()
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player_obj.control_x(-1)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player_obj.control_x(1)
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player_obj.control_y(1)
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player_obj.control_y(-1)
            #Handles releasing of a key
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player_obj.control_x(0)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player_obj.control_x(0)
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player_obj.control_y(0)
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player_obj.control_y(0)
            if event.type == pygame.MOUSEMOTION:
                player_obj.update_mouse()
                
        player_obj.update_keys()
                
        if second_timer % max_second_timer == 0:
            count += 1

        if player_obj.x >= 600 - player_obj.w:
            player_obj.x = 600 - player_obj.w
        if player_obj.x <= 0:
            player_obj.x = 0
        if player_obj.y >= 600 - player_obj.h:
            player_obj.y = 600 - player_obj.h
        if player_obj.y <= 0:
            player_obj.y = 0


        for x in range(0, count):
            if enemies[x].x > 700 or enemies[x].x < -200:
                del enemies[x]
            if enemies[x].y > 700 or enemies[x].y < -200:
                del enemies[x]
            #if player_obj.x - 150 < enemies[x].x < player_obj.x + 150:
                #if player_obj.y - 150 < enemies[x].y < player_obj.y + 150:
                    #enemies[x].draw()
            enemies[x].draw()
            enemies[x].update(count)
            
        filter1 = pygame.surface.Surface((600, 600))
        filter1.fill(white)
        filter1.blit(light, list(map(lambda x: x-252, player_obj.xy)))
        screen.blit(filter1, (0,0), special_flags=pygame.BLEND_RGBA_SUB)

        score_text = "{0:.0f}".format(count)
        scoretext = score_font.render(score_text, 1, red, 150)
        screen.blit(scoretext, (0,0))

        pygame.display.update()
        second_timer += 1
play()
