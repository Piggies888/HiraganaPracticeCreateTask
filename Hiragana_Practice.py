# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:02:39 2021

@author: Aryeh
"""
import sys
import random
import pygame
pygame.init()

#japImage = pygame.image.load();


hiraganaChar = ['Japanese Hiragana/JapHe.png.png','Japanese Hiragana/JapHe.png.png'];
hiraganaChar = ['Japanese Hiragana/01_a.png','Japanese Hiragana/02_i.png','Japanese Hiragana/03_u.png','Japanese Hiragana/04_e.png','Japanese Hiragana/05_o.png','Japanese Hiragana/06_ka.png','Japanese Hiragana/07_ki.png','Japanese Hiragana/08_ku.png','Japanese Hiragana/09_ke.png','Japanese Hiragana/10_ko.png','Japanese Hiragana/11_sa.png','Japanese Hiragana/12_shi.png','Japanese Hiragana/13_su.png','Japanese Hiragana/14_se.png','Japanese Hiragana/15_so.png','Japanese Hiragana/16_ta.png','Japanese Hiragana/17_chi.png','Japanese Hiragana/18_tsu.png','Japanese Hiragana/19_te.png','Japanese Hiragana/20_to.png','Japanese Hiragana/21_na.png','Japanese Hiragana/22_ni.png','Japanese Hiragana/23_nu.png','Japanese Hiragana/24_ne.png','Japanese Hiragana/25_no.png','Japanese Hiragana/26_ha.png','Japanese Hiragana/27_hi.png','Japanese Hiragana/28_fu.png','Japanese Hiragana/29_he.png','Japanese Hiragana/30_ho.png','Japanese Hiragana/31_ma.png','Japanese Hiragana/32_mi.png','Japanese Hiragana/33_mu.png','Japanese Hiragana/34_me.png','Japanese Hiragana/35_mo.png','Japanese Hiragana/36_ya.png','Japanese Hiragana/37_yu.png','Japanese Hiragana/38_yo.png','Japanese Hiragana/39_ra.png','Japanese Hiragana/40_ri.png','Japanese Hiragana/41_ru.png','Japanese Hiragana/42_re.png','Japanese Hiragana/43_ro.png','Japanese Hiragana/44_wa.png','Japanese Hiragana/45_wo.png','Japanese Hiragana/46_n.png'];

r = random
Black = (0,0,0)
White = (255,255,255)
isRunning = True
font = pygame.font.SysFont("C:\Windows\Fonts\Yu Gothic", 50)

input_box = pygame.Rect(100,100,140,32);
EngText = ''
def promptText():
    
    index = r.randint(0,len(hiraganaChar) - 1)
    '''
    japText = str(hiraganaChar[index]);
    japTextCont = font.render(japText, True, Black)
    textRect = japTextCont.get_rect()
    textRect.center = (100,350)
    screen.blit(japTextCont,textRect)
    '''
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
startup = 1;
def inputBox():
     text_surf = font.render(text, True, (255, 0, 0))
     textBox = text_surf.get_rect()
     textBox.center = (350,350)
     screen.blit(text_surf, textBox)
     pygame.display.flip()

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
                screen.fill(White)
                promptText()
                text = ''
                pygame.display.flip()
                
            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            else:
                print(event.unicode)
                
                text = text + event.unicode
                inputBox()
                screen.fill(White)
               # screen.blit(japImage,(0,0))
                print(text)
                
    
    
    
    
    

    
    
    




pygame.quit()

