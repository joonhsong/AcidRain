import pygame
import random
import os
import sys
from button import Button
from pygame import mixer

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (128, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Acid Rain")
clock = pygame.time.Clock()

BG = pygame.image.load("rain.png")

mixer.music.load('bgm.wav')
mixer.music.play(-1)


def get_font(size): 
    return pygame.font.Font("font.ttf", size)

def play():
    dictionary = [  "dog", "cat", "horse", "fish", "fox",
                    "cared", "python", "draws", "eagle", "beetle",
                    "ramen", "hurt", "champaign", "beaver", "dolphin",
                    "codable", "illinois", "chicago", "tiger", "lion",    # Easy
                    "computer", "science", "sakanaya", "yogi", "arirang", 
                    "miaza", "grainger", "brewlab", "county", "cravings", 
                    "panda", "subway", "kams", "redlion", "murphys",
                    "chipotle", "bbq", "legends", "urbana", "circlek",   # Meduim
                    "toyko", "seoul", "beverage", "beer", "beijing",
                    "berlin", "soju", "effected", "egresses", "feedbags", 
                    "gabfests", "grabbers", "refracts", "reverter", "scarcest",
                    "c++", "programming", "milano", "football", "soccer", # Med-Hard
                    "basketball", "baseball", "chicken", "kitchen", "bichon",
                    "russia", "korea", "japan", "usa", "feedbags", 
                    "gabfests", "grabbers", "refracts", "reverter", "scarcest",
                    "serrates", "tattered", "warcraft", "wattages", "zareebas", # Hard
                    "we are codable", "everyone can code", "double dark chocolate", "mario party", "super stars",
                    "play station 5", "play station 4", "play station 3", "play station 2", "play station 1",
                    "extravagate", "readdressed", "reaggregate", "resegregate", "revegetated",
                    "sassafrases", "stagecrafts", "stavesacres", "tradecrafts", "wastewaters"   # Extreme
                ]
    #(index 0~19): Easy (index 20~39): Medium (index 40~59): Hard (index 60~79): Extreme
    rand_1 = True
    rand_2 = True
    rand_3 = True
    rand_4 = True
    rand_5 = True
    level = 0
    level_clear = False
    miss = 0
    gameOver = False
    word_count = 0
    user_text = ''
    input_rect = pygame.Rect(450, 660, 120, 30)
    color_active = pygame.Color('white')
    color_passive = pygame.Color('blue')
    color = color_passive
    active = False
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    w5 = 0

    word_set = set()

    while True:
        clock.tick(30)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0,0))
        # PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        myFont = pygame.font.SysFont("arial", 25, False, True)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
        if active:
            color = color_active
        else:
            color = color_passive

        input_rect.w = 300 #max(100, text_surface.get_width()+20)
        input_rect.h = 38
        input_rect.centerx = 640
        pygame.draw.rect(SCREEN, color, input_rect)
        text_surface = myFont.render(user_text, True, BLACK)
        SCREEN.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        print(user_text)    # to cheack input
        
        if rand_1 == True:
            w1 = dictionary[random.randrange(10*level, 40+10*level)]
            while w1 in word_set:
                w1 = dictionary[random.randrange(10*level, 40+10*level)]
            word_set.add(w1)

            word_1 = myFont.render(w1, True, WHITE)
            #   level 0: randrange(0, 20)   level 1: randrange(10, 30)  level 2: randrange(20, 40)
            #   level 3: randrange(30, 50)   level 4: randrange(40, 60)   level 5: randrange(50, 70)
            #   level 6: randrange(60, 79)
            #   randrange(10*level, 20+10*level) level start with 0
            text_Rect = word_1.get_rect()
            text_Rect.x = 10
            text_Rect.y = 10
            word_1_x = random.randrange(0, 150)
            word_1_y = 0
            speed_1 = random.randrange(1+level, 4+level)
            rand_1 = False
        
        if rand_2 == True:
            w2 = dictionary[random.randrange(10*level, 40+10*level)]
            while w2 in word_set:
                w2 = dictionary[random.randrange(10*level, 40+10*level)]
            word_set.add(w2)
            word_2 = myFont.render(w2, True, WHITE)
            text_Rect = word_2.get_rect()
            text_Rect.x = 10
            text_Rect.y = 10
            word_2_x = random.randrange(200, 350)
            word_2_y = 0
            speed_2 = random.randrange(1+level, 4+level)
            rand_2 = False

        if rand_3 == True:
            w3 = dictionary[random.randrange(10*level, 40+10*level)]
            while w3 in word_set:
                w3 = dictionary[random.randrange(10*level, 40+10*level)]
            word_set.add(w3)
            word_3 = myFont.render(w3, True, WHITE)
            text_Rect = word_3.get_rect()
            text_Rect.x = 10
            text_Rect.y = 10
            word_3_x = random.randrange(400, 550)
            word_3_y = 0
            speed_3 = random.randrange(1+level, 4+level)
            rand_3 = False

        if rand_4 == True:
            w4 = dictionary[random.randrange(10*level, 40+10*level)]
            while w4 in word_set:
                w4 = dictionary[random.randrange(10*level, 40+10*level)]
            word_set.add(w4)
            word_4 = myFont.render(w4, True, WHITE)
            text_Rect = word_4.get_rect()
            text_Rect.x = 10
            text_Rect.y = 10
            word_4_x = random.randrange(600, 750)
            word_4_y = 0
            speed_4 = random.randrange(1+level, 4+level)
            rand_4 = False

        if rand_5 == True:
            w5 = dictionary[random.randrange(10*level, 40+10*level)]
            while w5 in word_set:
                w5 = dictionary[random.randrange(10*level, 40+10*level)]
            word_set.add(w5)
            word_5 = myFont.render(w5, True, WHITE)
            text_Rect = word_5.get_rect()
            text_Rect.x = 10
            text_Rect.y = 10
            word_5_x = random.randrange(800, 950)
            word_5_y = 0
            speed_5 = random.randrange(1+level, 4+level)
            rand_5 = False

        SCREEN.blit(word_1, (word_1_x, word_1_y))
        SCREEN.blit(word_2, (word_2_x, word_2_y))
        SCREEN.blit(word_3, (word_3_x, word_3_y))
        SCREEN.blit(word_4, (word_4_x, word_4_y))
        SCREEN.blit(word_5, (word_5_x, word_5_y))
        
        word_1_y += speed_1
        word_2_y += speed_2
        word_3_y += speed_3
        word_4_y += speed_4
        word_5_y += speed_5

        if user_text == w1:
            rand_1 = True
            word_count += 1
            user_text = ''
            word_set.remove(w1)
        if user_text == w2:
            rand_2 = True
            word_count += 1
            user_text = ''
            word_set.remove(w2)
        if user_text == w3:
            rand_3 = True
            word_count += 1
            user_text = ''
            word_set.remove(w3)
        if user_text == w4:
            rand_4 = True
            word_count += 1
            user_text = ''
            word_set.remove(w4)
        if user_text == w5:
            rand_5 = True
            word_count += 1
            user_text = ''
            word_set.remove(w5)

        if word_1_y >= 620:
            rand_1 = True
            miss += 1
        if word_2_y >= 620:
            rand_2 = True
            miss += 1
        if word_3_y >= 620:
            rand_3 = True
            miss += 1
        if word_4_y >= 620:
            rand_4 = True
            miss += 1
        if word_5_y >= 620:
            rand_5 = True
            miss += 1

        if level_clear == True:
            level += 1
            miss = 0
            level_clear = False

        if word_count != 0 and word_count % 20 == 0:
            level_clear = True
        
        if gameOver == True:
            break

        ph_level = [7.0, 6.7, 6.3, 6.0, 5.7, 5.3, 5.0, 4.7, 4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.3, 0]
        
        curr_ph = ph_level[miss]

        if curr_ph == 0:
            gameOver = True

        myFont = pygame.font.SysFont("arial", 20, True, True)
        level_Title = myFont.render("LEVEL: ", True, WHITE)
        level_Rect = level_Title.get_rect()
        level_Rect.x = 1100
        level_Rect.y = 10
        SCREEN.blit(level_Title, level_Rect)

        level_Title2 = myFont.render(str((level)), True, WHITE)
        level_Rect2 = level_Title2.get_rect()
        level_Rect2.x = 1200
        level_Rect2.y = 10
        SCREEN.blit(level_Title2, level_Rect2)

        word_Title = myFont.render("Word Count: ", True, WHITE)
        level_Rect = word_Title.get_rect()
        level_Rect.x = 1100
        level_Rect.y = 35
        SCREEN.blit(word_Title, level_Rect)

        word_Title2 = myFont.render(str((word_count)), True, WHITE)
        level_Rect2 = word_Title2.get_rect()
        level_Rect2.x = 1250
        level_Rect2.y = 35
        SCREEN.blit(word_Title2, level_Rect2)

        ph_Level = myFont.render("PH Level: ", True, WHITE)
        level_Rect = ph_Level.get_rect()
        level_Rect.x = 1100
        level_Rect.y = 60
        SCREEN.blit(ph_Level, level_Rect)

        ph_text = myFont.render(str((curr_ph)), True, WHITE)
        level_Rect2 = ph_text.get_rect()
        level_Rect2.x = 1220
        level_Rect2.y = 60
        SCREEN.blit(ph_text, level_Rect2)

        ph_visual = pygame.Rect(1100, 140, 70, 420)
        pygame.draw.rect(SCREEN, WHITE, ph_visual)
        pygame.draw.rect(SCREEN, BLACK, ph_visual, 5)

        pygame.draw.line(SCREEN, (200, 0, 0), [1100, 140 + miss * 20], [1210, 140 + miss * 20], 5)

        # pygame.draw.line(SCREEN, BLUE, [0, 645], [1280, 645], width=5)

        ph_7 = myFont.render("7.0", True, WHITE)
        level_Rect = ph_7.get_rect()
        level_Rect.x = 1230
        level_Rect.y = 130
        SCREEN.blit(ph_7, level_Rect)

        ph_6 = myFont.render("6.0", True, WHITE)
        level_Rect = ph_7.get_rect()
        level_Rect.x = 1230
        level_Rect.y = 190
        SCREEN.blit(ph_6, level_Rect)

        ph_5 = myFont.render("5.0", True, WHITE)
        level_Rect = ph_7.get_rect()
        level_Rect.x = 1230
        level_Rect.y = 250
        SCREEN.blit(ph_5, level_Rect)

        ph_4 = myFont.render("4.0", True, WHITE)
        level_Rect = ph_7.get_rect()
        level_Rect.x = 1230
        level_Rect.y = 310
        SCREEN.blit(ph_4, level_Rect)

        ph_3 = myFont.render("3.0", True, WHITE)
        level_Rect = ph_7.get_rect()
        level_Rect.x = 1230
        level_Rect.y = 370
        SCREEN.blit(ph_3, level_Rect)

        ph_2 = myFont.render("2.0", True, WHITE)
        level_Rect = ph_7.get_rect()
        level_Rect.x = 1230
        level_Rect.y = 430
        SCREEN.blit(ph_2, level_Rect)

        ph_1 = myFont.render("1.0", True, WHITE)
        level_Rect = ph_7.get_rect()
        level_Rect.x = 1230
        level_Rect.y = 490
        SCREEN.blit(ph_1, level_Rect)

        ph_0 = myFont.render("0.0", True, WHITE)
        level_Rect = ph_7.get_rect()
        level_Rect.x = 1230
        level_Rect.y = 550
        SCREEN.blit(ph_0, level_Rect)

        pygame.display.update()
    
    myFont_1 = pygame.font.SysFont("arial", 50, True, True)
    endText = myFont_1.render("GAME OVER",True, RED)
    endText_rect = endText.get_rect()
    endText_rect.center = (640, 100) 

    endText1 = myFont_1.render("Total Word Count: "+str((word_count))+"", True, GREEN)
    endText1_rect = endText1.get_rect()
    endText1_rect.center = (640, 150)

    endText2 = myFont_1.render("Press ESC to Quit", True, BLUE)
    endText2_rect = endText2.get_rect()
    endText2_rect.center = (640, 200)

    while gameOver:
        SCREEN.blit(endText, endText_rect)
        SCREEN.blit(endText1, endText1_rect)
        SCREEN.blit(endText2, endText2_rect)
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_menu()
    
def options():
    while True:
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0,0))

        ##OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        ##OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        ##SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        ##OPTIONS_CHARACTER = Button(image=pygame.image.load("button.png"), pos=(640, 250), 
                            ##text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_ON = Button(image=pygame.image.load("button.png"), pos=(640, 100), 
                            text_input="BGM ON", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_OFF = Button(image=pygame.image.load("button.png"), pos=(640, 250), 
                            text_input="BGM OFF", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_CREDITS = Button(image=pygame.image.load("button.png"), pos=(640, 400), 
                            text_input="CREDITS", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BACK = Button(image=pygame.image.load("button.png"), pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_ON.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_ON.update(SCREEN)
        OPTIONS_OFF.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_OFF.update(SCREEN)
        OPTIONS_CREDITS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_CREDITS.update(SCREEN)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_ON.checkForInput(OPTIONS_MOUSE_POS):
                    mixer.music.play(-1)
                if OPTIONS_OFF.checkForInput(OPTIONS_MOUSE_POS):
                    mixer.music.stop()
                if OPTIONS_CREDITS.checkForInput(OPTIONS_MOUSE_POS):
                    credits()
        pygame.display.update()
        


def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        CREDITS_TEXT = get_font(40).render("CREDITS TO:", True, "Yellow")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)
        CREDITS_TEXT1 = get_font(30).render("Joon Song, Jasmine Song", True, "Yellow")
        CREDITS_RECT1 = CREDITS_TEXT.get_rect(center=(350, 200))
        SCREEN.blit(CREDITS_TEXT1, CREDITS_RECT1)
        CREDITS_TEXT2 = get_font(30).render("YunSu Han, SeungHwan Hong, Sean Park", True, "Yellow")
        CREDITS_RECT2 = CREDITS_TEXT.get_rect(center=(350, 300))
        SCREEN.blit(CREDITS_TEXT2, CREDITS_RECT2)
        CREDITS_TEXT3 = get_font(30).render("HeeSoo Lim, Donghyeon Jeong", True, "Yellow")
        CREDITS_RECT3 = CREDITS_TEXT.get_rect(center=(350, 400))
        SCREEN.blit(CREDITS_TEXT3, CREDITS_RECT3)

        CREDITS_BACK = Button(image=pygame.image.load("button.png"), pos=(640, 550), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
        CREDITS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    options()
        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("ACID RAIN", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("button.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("button.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("button.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

