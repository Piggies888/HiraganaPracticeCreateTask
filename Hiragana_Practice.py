# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:02:39 2021

@author: Aryeh
"""
import sys
import random
import pygame
pygame.init()
global index;
score = 0;
#japImage = pygame.image.load();




hiraganaChar = ['Japanese Hiragana/01_a.png','Japanese Hiragana/02_i.png','Japanese Hiragana/03_u.png','Japanese Hiragana/04_e.png','Japanese Hiragana/05_o.png','Japanese Hiragana/06_ka.png','Japanese Hiragana/07_ki.png','Japanese Hiragana/08_ku.png','Japanese Hiragana/09_ke.png','Japanese Hiragana/10_ko.png','Japanese Hiragana/11_sa.png','Japanese Hiragana/12_shi.png','Japanese Hiragana/13_su.png','Japanese Hiragana/14_se.png','Japanese Hiragana/15_so.png','Japanese Hiragana/16_ta.png','Japanese Hiragana/17_chi.png','Japanese Hiragana/18_tsu.png','Japanese Hiragana/19_te.png','Japanese Hiragana/20_to.png','Japanese Hiragana/21_na.png','Japanese Hiragana/22_ni.png','Japanese Hiragana/23_nu.png','Japanese Hiragana/24_ne.png','Japanese Hiragana/25_no.png','Japanese Hiragana/26_ha.png','Japanese Hiragana/27_hi.png','Japanese Hiragana/28_fu.png','Japanese Hiragana/29_he.png','Japanese Hiragana/30_ho.png','Japanese Hiragana/31_ma.png','Japanese Hiragana/32_mi.png','Japanese Hiragana/33_mu.png','Japanese Hiragana/34_me.png','Japanese Hiragana/35_mo.png','Japanese Hiragana/36_ya.png','Japanese Hiragana/37_yu.png','Japanese Hiragana/38_yo.png','Japanese Hiragana/39_ra.png','Japanese Hiragana/40_ri.png','Japanese Hiragana/41_ru.png','Japanese Hiragana/42_re.png','Japanese Hiragana/43_ro.png','Japanese Hiragana/44_wa.png','Japanese Hiragana/45_wo.png','Japanese Hiragana/46_n.png'];

r = random
Black = (0,0,0)
White = (255,255,255)
isRunning = True
font = pygame.font.SysFont("C:\Windows\Fonts\Yu Gothic", 50)

input_box = pygame.Rect(100,100,140,32);
EngText = ''


def promptText(index):
   
    japImage = pygame.image.load(hiraganaChar[index])
    letter = screen.blit(japImage,(0,0))
    
    
    #return japImage
    #print(japText)



    
            #add input box code
# inputText():
 #   EngText = '';

  # color_inactive = pygame.Color('lightskyblue3')
    #color_active = pygame.Color('dodgerblue2')
    #color = color_inactive
    #active = False
    #return EngText;
#inputText()
#Screen
text = ''
def scoreDisplay(score):
    score_surf = font.render("Score:" + str(score), True, (133,133,133))
    scoreBox = score_surf.get_rect()
    scoreBox.center = (500,500)
    screen.blit(score_surf,scoreBox)
startup = 1;
def inputBox():
     text_surf = font.render(text, True, (255, 0, 0))
     textBox = text_surf.get_rect()
     textBox.center = (350,350)
     screen.blit(text_surf, textBox)
     #pygame.display.flip()

def correctLogic(index,text,score):
    if index == 0:
        Ans = 'a';
    elif index == 1:
        Ans = 'i'
    elif index == 2:
        Ans = 'u'
    elif index == 3:
        Ans = 'e'
    elif index == 4:
        Ans = 'o'
    elif index == 5:
        Ans = 'ka'
    elif index == 6:
        Ans = 'ki'

    elif index == 7 :
        Ans = 'ku'

    elif index ==  8:
        Ans = 'ke'

    elif index ==  9:
        Ans = 'ko'

    elif index ==  10:
        Ans = 'sa'

    elif index ==  11:
        Ans = 'shi'

    elif index == 12 :
        Ans = 'su'

    elif index == 13 :
        Ans = 'se'

    elif index ==  14:
        Ans = 'so'

    elif index == 15:
        Ans = 'ta'

    elif index == 16 :
        Ans = 'chi'

    elif index == 17 :
        Ans = 'tsu'

    elif index ==  18:
        Ans = 'te'

    elif index == 19 :
        Ans = 'to'

    elif index == 20 :
        Ans = 'na'

    elif index == 21 :
        Ans = 'ni'

    elif index == 22 :
        Ans = 'nu'

    elif index ==  23:
        Ans = 'ne'

    elif index == 24 :
        Ans = 'no'
    elif index == 25 :
        Ans = 'ha'

    elif index == 26 :
        Ans = 'hi'

    elif index ==  27:
        Ans = 'fu'

    elif index == 28 :
        Ans = 'he'

    elif index == 29 :
        Ans = 'ho'

    elif index ==  30:
        Ans = 'ma'

    elif index ==  31:
        Ans = 'mi'

    elif index ==  32:
        Ans = 'mu'

    elif index == 33 :
        Ans = 'me'

    elif index ==  34:
        Ans = 'mo'

    elif index == 35 :
        Ans = 'ya'

    elif index == 36 :
        Ans = 'yu'

    elif index ==  37:
        Ans = 'yo'

    elif index == 38 :
        Ans = 'ra'

    elif index == 39 :
        Ans = 'ri'

    elif index == 40 :
        Ans = 'ru'

    elif index == 41 :
        Ans = 're'

    elif index == 42 :
        Ans = 'ro'

    elif index == 43 :
        Ans = 'wa'

    elif index == 44 :
        Ans = 'wo'

    elif index == 45 :
        Ans = 'n'






    print(Ans)
    print(text)
    if Ans == text:
        increase = True;
    else:
        return
    return increase;

while isRunning == True:
    
    if startup == 1:
        size = (700, 700);
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Hiragana Practice")
        screen.fill(White)
        startup = 0;
    #japletter = pygame.image.load('JapHe.png.png')
    #screen.blit(japletter,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                scoreDisplay(score)
                x = r.randint(0,len(hiraganaChar) - 1)
                index = x;
                
                
                promptText(index)
                text = ''
                pygame.display.flip()
                
            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            else:
                #print(event.unicode)
                
                text = text + event.unicode
                if (correctLogic(index,text,score)):
                    score = score + 1;
                    print(score)
                    scoreDisplay(score)
                promptText(index)
                inputBox()
                pygame.display.flip()
                screen.fill(White)
               # screen.blit(japImage,(0,0))
                #print(text)
                
                
                
    
    
    
    
    

    
    
    




pygame.quit()

