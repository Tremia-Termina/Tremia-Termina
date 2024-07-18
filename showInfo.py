import pygame
def showInfo(player, max_health, font, screen, missile_on_cooldown, missile_cooldown, current_time, last_missile_time, difficulty, count, toggle_triple_shoot, triple_shoot_duration, triple_shoot_start_time, bossSummoned, boss_health, boss):
    if player.health > (max_health * 2) / 3:
        health_surface = font.render(f"HP: {player.health}", True, (0, 255, 0))
        screen.blit(health_surface, (10, 10))
    elif player.health > max_health / 3:
        health_surface = font.render(f"HP: {player.health}", True, (255, 255, 0))
        screen.blit(health_surface, (10, 10))
    else:
        health_surface = font.render(f"HP: {player.health}", True, (255, 0, 0))
        screen.blit(health_surface, (10, 10))
    if missile_on_cooldown:
        missile_cooldown_display = missile_cooldown * 1000 - current_time + last_missile_time
        missile_cooldown_display /= 1000.0
        missile_cooldown_surface = font.render(f"Missile: {missile_cooldown_display:.1f}s", True, (255, 0, 0))
        screen.blit(missile_cooldown_surface, (10, 30))
    else:
        missile_ready_surface = font.render("Missile: READY", True, (0, 255, 0))
        screen.blit(missile_ready_surface, (10, 30))
    difficulty_surface = font.render(f"Difficulty: {difficulty}", True, (255, 255, 255))
    screen.blit(difficulty_surface, (10, 50))
    score_surface = font.render(f"Score: {count}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 70))
    if toggle_triple_shoot:
        triple_shoot_remaining = triple_shoot_duration - (current_time - triple_shoot_start_time) / 1000
        triple_active_surface = font.render(f"Triple Shoot: {triple_shoot_remaining:.1f}s", True, (0, 255, 0))
        screen.blit(triple_active_surface, (10, 90))
    else:
        triple_inactive_surface = font.render("Triple Shoot: INACTIVE", True, (255, 0, 0))
        screen.blit(triple_inactive_surface, (10, 90))
    if bossSummoned:
        if boss.health > (boss_health * 2) / 3:
            boss_health_surface = font.render(f"Boss Health: {boss.health}", True, (0, 255, 0))
            screen.blit(boss_health_surface, (10, 110))
        elif boss.health > boss_health / 3:
            boss_health_surface = font.render(f"Boss Health: {boss.health}", True, (255, 255, 0))
            screen.blit(boss_health_surface, (10, 110))
        else:
            boss_health_surface = font.render(f"Boss Health: {boss.health}", True, (255, 0, 0))
            screen.blit(boss_health_surface, (10, 110))
    pygame.display.flip()