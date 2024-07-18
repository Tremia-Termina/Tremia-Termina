import pygame
def createGroups():
    enemies = pygame.sprite.Group()
    bosses = pygame.sprite.Group()
    difficulties = pygame.sprite.Group()
    heals = pygame.sprite.Group()
    shoots = pygame.sprite.Group()
    lasers = pygame.sprite.Group()
    bossBullets = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    return enemies, bosses, difficulties, heals, shoots, lasers, bossBullets, explosions