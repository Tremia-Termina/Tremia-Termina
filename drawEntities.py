import pygame
def drawEntities(player, lasers, enemies, explosions, difficulties, heals, shoots, screen, bossSummoned, boss, bossBullets):
    for entity in [player] + list(lasers) + list(enemies) + list(explosions) + list(difficulties) + list(heals) + list(shoots):
        screen.blit(entity.image, entity.rect)
    if bossSummoned:
        for entity in [boss] + list(bossBullets):
            screen.blit(entity.image, entity.rect)