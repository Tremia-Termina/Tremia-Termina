import pygame
def GameOver(game_over, screen, game_over_sprite, screen_width, screen_height, font, count):
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_over = False
        screen.fill((0, 0, 0))
        screen.blit(game_over_sprite, (screen_width / 2 - 99, screen_height / 2 - 28))

        exit_surface = font.render("Press ESC to exit", True, (255, 255, 255))
        exit_rect = exit_surface.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
        screen.blit(exit_surface, exit_rect)

        score_surface = font.render(f"Total Score: {count}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(screen_width / 2, screen_height / 2 + 100))
        screen.blit(score_surface, score_rect)
        pygame.display.flip()

def BossDefeated(bossDefeated, count, boss_health, screen, font, screen_width, screen_height):
    count += boss_health
    while bossDefeated:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bossDefeated = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                bossDefeated = False
        screen.fill((0, 0, 0))
        victory_surface = font.render("You Win!", True, (255, 255, 255))
        victory_rect = victory_surface.get_rect(center=(screen_width / 2, screen_height / 2 - 30))
        screen.blit(victory_surface, victory_rect)
        exit_surface = font.render("Press Escape to exit", True, (255, 255, 255))
        exit_rect = exit_surface.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
        screen.blit(exit_surface, exit_rect)
        score_surface = font.render(f"Total Score: {count}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(screen_width / 2, screen_height / 2 + 100))
        screen.blit(score_surface, score_rect)
        pygame.display.flip()