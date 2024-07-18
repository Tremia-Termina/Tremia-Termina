import random
def update(player, difficulty, enemies, Enemy, screen_width, bossSummoned, boss, bossBullets, difficulties, heals, shoots, lasers, explosions):
    player.update()
    if random.randrange(100) < difficulty:
        enemies.add(Enemy((random.randrange(screen_width - 64), 0)))
    enemies.update()
    if bossSummoned:
        boss.update()
        bossBullets.update()
    difficulties.update()
    heals.update()
    shoots.update()
    lasers.update()
    explosions.update()