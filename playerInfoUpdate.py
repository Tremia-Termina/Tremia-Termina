import pygame

def playerInfoUpdate(current_time, last_missile_time, missile_cooldown, missile_on_cooldown, triple_shoot_start_time, triple_shoot_duration, toggle_triple_shoot, player, running, game_over):
    if current_time - last_missile_time >= missile_cooldown * 1000 and missile_on_cooldown:
        missile_on_cooldown = False

    if current_time - triple_shoot_start_time >= triple_shoot_duration * 1000:
        toggle_triple_shoot = False

    if player.invincible and pygame.time.get_ticks() > player.invincibility_timer:
        player.invincible = False

    if player.health <= 0:
        running = False
        game_over = True

    return missile_on_cooldown, toggle_triple_shoot, running, game_over