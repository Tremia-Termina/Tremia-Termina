import pygame
import random
def check_hits(lasers, enemies, explosion_sound, explosions, Sprite, explosion_sprite, enter_bossFight, boostAppearChance, difficulties, DecreaseDifficulty, screen_width, heals, Heal, shoots, TripleShoot, player, max_health, current_time, count, bossFight, difficulty, toggle_triple_shoot, triple_shoot_start_time, invincibleSeconds):
    bullet_hits = pygame.sprite.groupcollide(lasers, enemies, True, True)
    for hit in bullet_hits:
        explosion_sound.play()
        explosions.add(Sprite(explosion_sprite, hit.rect.topleft))
        count += 1
        if count >= enter_bossFight:
            bossFight = True
        if random.randrange(100) < boostAppearChance * 100:
            key = random.randrange(1, 4)
            if key == 1:
                difficulties.add(DecreaseDifficulty((random.randrange(screen_width - 64), 0)))
            elif key == 2:
                heals.add(Heal((random.randrange(screen_width - 64), 0)))
            elif key == 3:
                shoots.add(TripleShoot((random.randrange(screen_width - 64), 0)))

    difficulties_hits = pygame.sprite.spritecollide(player, difficulties, True)
    for hit in difficulties_hits:
        difficulty = max(difficulty - 1, 1)

    heals_hits = pygame.sprite.spritecollide(player, heals, True)
    for hit in heals_hits:
        player.health = min(player.health + 1, max_health)

    shoots_hits = pygame.sprite.spritecollide(player, shoots, True)
    for hit in shoots_hits:
        toggle_triple_shoot = True
        triple_shoot_start_time = current_time
    
    enemy_hits = pygame.sprite.spritecollide(player, enemies, True)
    if enemy_hits:
        if not player.invincible:
            player.health -= 1
            player.invincible = True
            player.invincibility_timer = pygame.time.get_ticks() + (1000 * invincibleSeconds)
        else:
            pass
    
    return count, bossFight, difficulty, player.health, toggle_triple_shoot, triple_shoot_start_time, player.invincible, player.invincibility_timer

def boss_check_hits(bossSummoned, player, enemies, invincibleSeconds, boss, lasers, bossBullets, bosses):
    if bossSummoned:
        enemy_hits = pygame.sprite.spritecollide(player, bossBullets, True)
        if enemy_hits:
            if not player.invincible:
                player.health -= 1
                player.invincible = True
                player.invincibility_timer = pygame.time.get_ticks() + (1000 * invincibleSeconds)
        else:
            pass

        bosses_hits = pygame.sprite.spritecollide(player, bosses, True)
        if bosses_hits:
            if not player.invincible:
                player.health -= 10
                player.invincible = True
                player.invincibility_timer = pygame.time.get_ticks() + (1000 * invincibleSeconds)

        boss_hits = pygame.sprite.spritecollide(boss, lasers, True)
        for hit in boss_hits:
            boss.health -= 1
        
        return player.health, player.invincible, player.invincibility_timer, boss.health