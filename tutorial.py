import pygame
import os
import time
import random
import math
from loadSprites import load_sprite_png

def show_tutorial(screen, font, screen_width, screen_height):
    running = True
    game_started = False
    tutorial1 = False
    tutorial2 = False
    tutorial3 = False
    tutorial4 = False
    tutorial5 = False
    tutorial6 = False

    decreaseDifficulty_sprite = load_sprite_png("decreaseDifficulty", 1.5)

    heal_sprite = load_sprite_png("heal", 1.5)

    tripleShoot_sprite = load_sprite_png("tripleShoot", 1.5)

    while running and (not game_started):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and not game_started:
                    game_started = True
                elif event.key == pygame.K_t and not tutorial1 and not game_started:
                    tutorial1 = True
                elif event.key == pygame.K_SPACE and not game_started and tutorial1:
                    tutorial1 = False
                    tutorial2 = True
                elif event.key == pygame.K_SPACE and not game_started and tutorial2:
                    tutorial2 = False
                    tutorial3 = True
                elif event.key == pygame.K_SPACE and not game_started and tutorial3:
                    tutorial3 = False
                    tutorial4 = True
                elif event.key == pygame.K_SPACE and not game_started and tutorial4:
                    tutorial4 = False
                    tutorial5 = True
                elif event.key == pygame.K_SPACE and not game_started and tutorial5:
                    tutorial5 = False
                    tutorial6 = True
                elif event.key == pygame.K_SPACE and not game_started and tutorial6:
                    tutorial6 = False
                    game_started = True
    
        if not game_started:
            screen.fill((0, 0, 0))
            if (not tutorial1) and (not tutorial2) and (not tutorial3) and (not tutorial4) and (not tutorial5) and (not tutorial6):
                start_text1 = font.render("Press T for tutorial", True, (255, 255, 255))
                start_rect1 = start_text1.get_rect(center = (screen_width / 2, screen_height / 2 - 20))
                screen.blit(start_text1, start_rect1)

                start_text2 = font.render("Press S to skip tutorial", True, (255, 255, 255))
                start_rect2 = start_text2.get_rect(center = (screen_width / 2, screen_height / 2 + 20))
                screen.blit(start_text2, start_rect2)

            if tutorial1:
                tutorial1_text1 = font.render("Movement:", True, (255, 255, 255))
                tutorial1_rect1 = tutorial1_text1.get_rect(center = (screen_width / 2, screen_height / 2 - 30))
                screen.blit(tutorial1_text1, tutorial1_rect1)

                tutorial1_text2 = font.render("Use UP, DOWN, LEFT, RIGHT to move", True, (255, 255, 255))
                tutorial1_rect2 = tutorial1_text2.get_rect(center = (screen_width / 2, screen_height / 2 + 30))
                screen.blit(tutorial1_text2, tutorial1_rect2)

                tutorial1_text3 = font.render("Press SPACE to continue", True, (255, 255, 255))
                tutorial1_rect3 = tutorial1_text3.get_rect(center = (screen_width / 2, screen_height / 2 + 310))
                screen.blit(tutorial1_text3, tutorial1_rect3)

            if tutorial2:
                tutorial2_text1 = font.render("Attack:", True, (255, 255, 255))
                tutorial2_rect1 = tutorial2_text1.get_rect(center = (screen_width / 2, screen_height / 2 - 200))
                screen.blit(tutorial2_text1, tutorial2_rect1)

                tutorial2_text2 = font.render("Press SPACE, Z, X to shoot in", True, (255, 255, 255))
                tutorial2_rect2 = tutorial2_text2.get_rect(center = (screen_width / 2, screen_height / 2 - 120))
                screen.blit(tutorial2_text2, tutorial2_rect2)

                tutorial2_text3 = font.render("Straight Up/Upper Left/Upper Right", True, (255, 255, 255))
                tutorial2_rect3 = tutorial2_text3.get_rect(center = (screen_width / 2, screen_height / 2 - 90))
                screen.blit(tutorial2_text3, tutorial2_rect3)

                tutorial2_text4 = font.render("Press M to launch a Missile", True, (255, 255, 255))
                tutorial2_rect4 = tutorial2_text4.get_rect(center = (screen_width / 2, screen_height / 2 - 10))
                screen.blit(tutorial2_text4, tutorial2_rect4)

                tutorial2_text5 = font.render("Missiles aim at nearest enemy", True, (255, 255, 255))
                tutorial2_rect5 = tutorial2_text5.get_rect(center = (screen_width / 2, screen_height / 2 + 20))
                screen.blit(tutorial2_text5, tutorial2_rect5)

                tutorial_text6 = font.render("but default to have a 1 second cooldown", True, (255, 255, 255))
                tutorial_rect6 = tutorial_text6.get_rect(center = (screen_width / 2, screen_height / 2 + 50))
                screen.blit(tutorial_text6, tutorial_rect6)

                tutorial2_text7 = font.render("Missile accuracy decreases", True, (255, 255, 255))
                tutorial2_rect7 = tutorial2_text7.get_rect(center = (screen_width / 2, screen_height / 2 + 80))
                screen.blit(tutorial2_text7, tutorial2_rect7)

                tutorial2_text8 = font.render("as you are farther from your enemy", True, (255, 255, 255))
                tutorial2_rect8 = tutorial2_text8.get_rect(center = (screen_width / 2, screen_height / 2 + 110))
                screen.blit(tutorial2_text8, tutorial2_rect8)

                tutorial2_text9 = font.render("Missiles do not target Boss", True, (255, 255, 255))
                tutorial2_rect9 = tutorial2_text9.get_rect(center = (screen_width / 2, screen_height / 2 + 190))
                screen.blit(tutorial2_text9, tutorial2_rect9)

                tutorial2_text10 = font.render("Press SPACE to continue", True, (255, 255, 255))
                tutorial2_rect10 = tutorial2_text10.get_rect(center = (screen_width / 2, screen_height / 2 + 310))
                screen.blit(tutorial2_text10, tutorial2_rect10)

            if tutorial3:
                tutorial3_text1 = font.render("Hitpoints:", True, (255, 255, 255))
                tutorial3_rect1 = tutorial3_text1.get_rect(center = (screen_width / 2, screen_height / 2 - 200))
                screen.blit(tutorial3_text1, tutorial3_rect1)

                tutorial3_text2 = font.render("Upon hit, you lose 1 HP", True, (255, 255, 255))
                tutorial3_rect2 = tutorial3_text2.get_rect(center = (screen_width / 2, screen_height / 2 - 120))
                screen.blit(tutorial3_text2, tutorial3_rect2)

                tutorial3_text3 = font.render("and enter a 1 second invincibility frame", True, (255, 255, 255))
                tutorial3_rect3 = tutorial3_text3.get_rect(center = (screen_width / 2, screen_height / 2 - 90))
                screen.blit(tutorial3_text3, tutorial3_rect3)

                tutorial3_text4 = font.render("by default", True, (255, 255, 255))
                tutorial3_rect4 = tutorial3_text4.get_rect(center = (screen_width / 2, screen_height / 2 - 60))
                screen.blit(tutorial3_text4, tutorial3_rect4)

                tutorial3_text5 = font.render("For every enemy failed to defeat", True, (255, 255, 255))
                tutorial3_rect5 = tutorial3_text5.get_rect(center = (screen_width / 2, screen_height / 2))
                screen.blit(tutorial3_text5, tutorial3_rect5)

                tutorial3_text6 = font.render("you lose 1 HP as well", True, (255, 255, 255))
                tutorial3_rect6 = tutorial3_text6.get_rect(center = (screen_width / 2, screen_height / 2 + 30))
                screen.blit(tutorial3_text6, tutorial3_rect6)
                
                tutorial3_text7 = font.render("but do not enter invincibility frame", True, (255, 255, 255))
                tutorial3_rect7 = tutorial3_text7.get_rect(center = (screen_width / 2, screen_height / 2 + 60))
                screen.blit(tutorial3_text7, tutorial3_rect7)

                tutorial3_text8 = font.render("Press SPACE to continue", True, (255, 255, 255))
                tutorial3_rect8 = tutorial3_text8.get_rect(center = (screen_width / 2, screen_height / 2 + 310))
                screen.blit(tutorial3_text8, tutorial3_rect8)

            if tutorial4:
                tutorial4_text1 = font.render("Difficulty:", True, (255, 255, 255))
                tutorial4_rect1 = tutorial4_text1.get_rect(center = (screen_width / 2, screen_height / 2 - 200))
                screen.blit(tutorial4_text1, tutorial4_rect1)

                tutorial4_text2 = font.render("Difficulty defaults to:", True, (255, 255, 255))
                tutorial4_rect2 = tutorial4_text2.get_rect(center = (screen_width / 2, screen_height / 2 - 120))
                screen.blit(tutorial4_text2, tutorial4_rect2)

                tutorial4_text3 = font.render("start from 1", True, (255, 255, 255))
                tutorial4_rect3 = tutorial4_text3.get_rect(center = (screen_width / 2, screen_height / 2 - 90))
                screen.blit(tutorial4_text3, tutorial4_rect3)

                tutorial4_text4 = font.render("increase by 1 every 10 seconds", True, (255, 255, 255))
                tutorial4_rect4 = tutorial4_text4.get_rect(center = (screen_width / 2, screen_height / 2 - 60))
                screen.blit(tutorial4_text4, tutorial4_rect4)

                tutorial4_text5 = font.render("and be capped at 20", True, (255, 255, 255))
                tutorial4_rect5 = tutorial4_text5.get_rect(center = (screen_width / 2, screen_height / 2 - 30))
                screen.blit(tutorial4_text5, tutorial4_rect5)

                tutorial4_text6 = font.render("Some magic may reduce difficulty", True, (255, 255, 255))
                tutorial4_rect6 = tutorial4_text6.get_rect(center = (screen_width / 2, screen_height / 2 + 60))
                screen.blit(tutorial4_text6, tutorial4_rect6)

                tutorial4_text7 = font.render("Press SPACE to continue", True, (255, 255, 255))
                tutorial4_rect7 = tutorial4_text7.get_rect(center = (screen_width / 2, screen_height / 2 + 310))
                screen.blit(tutorial4_text7, tutorial4_rect7)

            if tutorial5:
                tutorial5_text1 = font.render("Boosts:", True, (255, 255, 255))
                tutorial5_rect1 = tutorial5_text1.get_rect(center = (screen_width / 2, screen_height / 2 - 200))
                screen.blit(tutorial5_text1, tutorial5_rect1)

                tutorial5_text2 = font.render("Each time you defeat an enemy", True, (255, 255, 255))
                tutorial5_rect2 = tutorial5_text2.get_rect(center = (screen_width / 2, screen_height / 2 - 120))
                screen.blit(tutorial5_text2, tutorial5_rect2)

                tutorial5_text3 = font.render("there is a chance to spawn a boost", True, (255, 255, 255))
                tutorial5_rect3 = tutorial5_text3.get_rect(center = (screen_width / 2, screen_height / 2 - 90))
                screen.blit(tutorial5_text3, tutorial5_rect3)

                screen.blit(decreaseDifficulty_sprite, (screen_width / 2 - 160, screen_height / 2 - 41.5))
                
                tutorial5_text4 = font.render("decreases difficulty by 1", True, (255, 255, 255))
                tutorial5_rect4 = tutorial5_text4.get_rect(center = (screen_width / 2 + 20, screen_height / 2 - 30))
                screen.blit(tutorial5_text4, tutorial5_rect4)

                tutorial5_text6 = font.render("to a minimum of 1", True, (255, 255, 255))
                tutorial5_rect6 = tutorial5_text6.get_rect(center = (screen_width / 2, screen_height / 2))
                screen.blit(tutorial5_text6, tutorial5_rect6)

                screen.blit(heal_sprite, (screen_width / 2 - 110, screen_height / 2 + 49))

                tutorial5_text7 = font.render("heals you for 1", True, (255, 255, 255))
                tutorial5_rect7 = tutorial5_text7.get_rect(center = (screen_width / 2 + 10, screen_height / 2 + 60))
                screen.blit(tutorial5_text7, tutorial5_rect7)

                tutorial5_text8 = font.render("to a maximum of your max health", True, (255, 255, 255))
                tutorial5_rect8 = tutorial5_text8.get_rect(center = (screen_width / 2, screen_height / 2 + 90))
                screen.blit(tutorial5_text8, tutorial5_rect8)

                screen.blit(tripleShoot_sprite, (screen_width / 2 - 157.5, screen_height / 2 + 137.5))

                tutorial5_text9 = font.render("lets you shoot 3 bullets", True, (255, 255, 255))
                tutorial5_rect9 = tutorial5_text9.get_rect(center = (screen_width / 2 + 10, screen_height / 2 + 150))
                screen.blit(tutorial5_text9, tutorial5_rect9)

                tutorial5_text10 = font.render("for 10 seconds", True, (255, 255, 255))
                tutorial5_rect10 = tutorial5_text10.get_rect(center = (screen_width / 2, screen_height / 2 + 180))
                screen.blit(tutorial5_text10, tutorial5_rect10)

                tutorial5_text11 = font.render("Press SPACE to continue", True, (255, 255, 255))
                tutorial5_rect11 = tutorial5_text11.get_rect(center = (screen_width / 2, screen_height / 2 + 310))
                screen.blit(tutorial5_text11, tutorial5_rect11)
            
            if tutorial6:
                tutorial6_text1 = font.render("Boss:", True, (255, 255, 255))
                tutorial6_rect1 = tutorial6_text1.get_rect(center = (screen_width / 2, screen_height / 2 - 200))
                screen.blit(tutorial6_text1, tutorial6_rect1)

                tutorial6_text2 = font.render("Upon defeating", True, (255, 255, 255))
                tutorial6_rect2 = tutorial6_text2.get_rect(center = (screen_width / 2, screen_height / 2 - 120))
                screen.blit(tutorial6_text2, tutorial6_rect2)

                tutorial6_text3 = font.render("a certain number of enemies", True, (255, 255, 255))
                tutorial6_rect3 = tutorial6_text3.get_rect(center = (screen_width / 2, screen_height / 2 - 90))
                screen.blit(tutorial6_text3, tutorial6_rect3)

                tutorial6_text4 = font.render("a boss will spawn", True, (255, 255, 255))
                tutorial6_rect4 = tutorial6_text4.get_rect(center = (screen_width / 2, screen_height / 2 - 60))
                screen.blit(tutorial6_text4, tutorial6_rect4)

                tutorial6_text5 = font.render("Boss also attacks you", True, (255, 255, 255))
                tutorial6_rect5 = tutorial6_text5.get_rect(center = (screen_width / 2, screen_height / 2 + 20))
                screen.blit(tutorial6_text5, tutorial6_rect5)

                tutorial6_text6 = font.render("Defeat the boss to win", True, (255, 255, 255))
                tutorial6_rect6 = tutorial6_text6.get_rect(center = (screen_width / 2, screen_height / 2 + 100))
                screen.blit(tutorial6_text6, tutorial6_rect6)

                tutorial6_text7 = font.render("Press SPACE to start", True, (255, 255, 255))
                tutorial6_rect7 = tutorial6_text7.get_rect(center = (screen_width / 2, screen_height / 2 + 310))
                screen.blit(tutorial6_text7, tutorial6_rect7)
        pygame.display.flip()