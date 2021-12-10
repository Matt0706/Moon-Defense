import pygame
from color import *
import MoonDefense


def menu():
    pygame.init()
    size = [MoonDefense.SCREEN_WIDTH, MoonDefense.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Moon Defense")
    pygame.mouse.set_visible(True)

    start_button = pygame.Rect(100, 300, 325, 100)
    help_button = pygame.Rect(100, 420, 325, 100)
    font = pygame.font.SysFont("serif", 72)
    startFont = pygame.font.SysFont("Serif", 64)
    nameFont = pygame.font.SysFont("Serif", 50)
    titleTxt = font.render("Moon Defense", True, WHITE)
    startTxt = startFont.render("Start Game", True, WHITE)
    nameTxt = nameFont.render("by Matthew Medina", True, BLACK)
    helpTxt = startFont.render("Help", True, WHITE)
    pygame.mixer.music.load("sounds/slowgrind.wav")
    pygame.mixer.music.set_volume(.25)
    pygame.mixer.music.play(-1)
    helpscreen = pygame.image.load("images/help.jpg").convert()

    titleBackground = pygame.image.load("images/titlescreen.jpg").convert()
    while True:
        screen.fill(WHITE)
        screen.blit(titleBackground, [-200, -200])
        pygame.draw.rect(screen, GREY, start_button)
        pygame.draw.rect(screen, GREY, help_button)
        screen.blit(titleTxt, [100, 100])
        screen.blit(startTxt, [110, 310])
        screen.blit(nameTxt, [700, 525])
        screen.blit(helpTxt, [110, 430])
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()
        if start_button.collidepoint((mx, my)) and click:
            break
        if help_button.collidepoint((mx, my)) and click:
            click = False
            while not click:
                screen.fill(WHITE)
                screen.blit(helpscreen, [0, 0])
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        click = True
        pygame.display.flip()
