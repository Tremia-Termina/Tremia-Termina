import random
import math
import pygame

from tutorial import show_tutorial
from settings import difficulty_setting, player_setting, enemy_setting, bullet_setting, boost_setting, animation_setting
from calc_speed import calc_speed
from createClasses import createSprite, createPlayer, createBullet, createBulletLeft, createBulletRight, createBossBullet, createMissile, createEnemy, createBoss, createDecreaseDifficulty, createHeal, createTripleShoot
from createGroups import createGroups
from loadSprites import load_sprite_svg, load_sprite_png, load_sound
from updates import update
from checkHits import check_hits, boss_check_hits
from postGame import GameOver, BossDefeated
from showInfo import showInfo
from drawEntities import drawEntities
from playerInfoUpdate import playerInfoUpdate

pygame.init()
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Plane Game")
font = pygame.font.Font("TrajanPro-Regular.otf", 20)

# 导入设置
base_difficulty, difficulty_increase_interval, max_difficulty, enter_bossFight = difficulty_setting()
max_health, up_speed, down_speed, left_speed, right_speed, invincibleSeconds, missile_cooldown, triple_shoot_duration = player_setting()
bullet_speed, bullet_leftSpeed, bullet_rightSpeed = bullet_setting()
enemyMinSpeed, enemyMaxSpeed, boss_health, boss_leftSpeed, boss_rightSpeed, boss_bullet_minSpeed, boss_bullet_maxSpeed, boss_shootChance = enemy_setting()
boostMinSpeed, boostMaxSpeed, boostAppearChance = boost_setting()
explosionDelaySeconds = animation_setting()

# 导入素材
bullet_sprite = load_sprite_svg("bullet", 1)
boss_bullet_sprite = load_sprite_png("bossBullet", 1)
missile_sprite = load_sprite_png("missile", 1)
enemy_sprite = load_sprite_svg("enemy", 1)
explosion_sprite = load_sprite_svg("explosion", 1)
player_sprite = load_sprite_svg("player", 1)
game_over_sprite = load_sprite_png("gameOver", 1)
decreaseDifficulty_sprite = load_sprite_png("decreaseDifficulty", 1.5)
heal_sprite = load_sprite_png("heal", 1.5)
tripleShoot_sprite = load_sprite_png("tripleShoot", 1.5)
boss_sprite = load_sprite_svg("enemy", 3)
explosion_sound = load_sound("sound")

# 创建类
Sprite = createSprite(explosionDelaySeconds)
Player = createPlayer(Sprite, player_sprite, max_health, up_speed, down_speed, left_speed, right_speed, screen_width, screen_height)
player = Player((screen_width / 2, screen_height - 64))
Bullet = createBullet(Sprite, bullet_sprite, bullet_speed)
BulletLeft = createBulletLeft(Sprite, bullet_sprite, bullet_speed, bullet_leftSpeed)
BulletRight = createBulletRight(Sprite, bullet_sprite, bullet_speed, bullet_rightSpeed)
BossBullet = createBossBullet(Sprite, boss_bullet_sprite, boss_bullet_minSpeed, boss_bullet_maxSpeed)
class Missile(Sprite):
    def __init__(self, sprite, position):
        super().__init__(missile_sprite, position)
        self.speed_x = missile_speed_x
        self.speed_y = missile_speed_y
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y -= self.speed_y
        if self.rect.bottom < 0:
            self.kill()
Enemy = createEnemy(Sprite, enemy_sprite, enemyMinSpeed, enemyMaxSpeed, screen_height, player)
Boss = createBoss(Sprite, boss_sprite, boss_health, boss_leftSpeed, boss_rightSpeed, screen_width)
DecreaseDifficulty = createDecreaseDifficulty(Sprite, decreaseDifficulty_sprite, boostMinSpeed, boostMaxSpeed, screen_height)
Heal = createHeal(Sprite, heal_sprite, boostMinSpeed, boostMaxSpeed, screen_height)
TripleShoot = createTripleShoot(Sprite, tripleShoot_sprite, boostMinSpeed, boostMaxSpeed, screen_height)

# 创建组
enemies, bosses, difficulties, heals, shoots, lasers, bossBullets, explosions = createGroups()

clock = pygame.time.Clock()
running = True
tutorial_shown = False
game_started = False
game_over = False
count = 0
last_missile_time = 0
missile_on_cooldown = False
last_difficulty_increase_time = pygame.time.get_ticks()
difficulty = base_difficulty
toggle_triple_shoot = False
triple_shoot_start_time = 0
bossFight = False
bossSummoned = False
bossDefeated = False
boss = None
while running:
    clock.tick(60)
    game_started = True
    current_time = pygame.time.get_ticks()
    if(current_time - last_difficulty_increase_time > difficulty_increase_interval * 1000):
        last_difficulty_increase_time = current_time
        difficulty = min(difficulty + 1, max_difficulty)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if event.key == pygame.K_SPACE and game_started and (not toggle_triple_shoot):
                lasers.add(Bullet(bullet_sprite, (player.rect.centerx - 7, player.rect.top)))
            elif event.key == pygame.K_SPACE and game_started and toggle_triple_shoot:
                lasers.add(Bullet(bullet_sprite, (player.rect.centerx - 18, player.rect.top)))
                lasers.add(Bullet(bullet_sprite, (player.rect.centerx + 4, player.rect.top)))
                lasers.add(Bullet(bullet_sprite, (player.rect.centerx - 7, player.rect.top)))
            elif event.key == pygame.K_z:
                lasers.add(BulletLeft(bullet_sprite, (player.rect.centerx - 7, player.rect.top)))
            elif event.key == pygame.K_x:
                lasers.add(BulletRight(bullet_sprite, (player.rect.centerx - 7, player.rect.top)))
            elif event.key == pygame.K_m:
                if enemies:
                    closest_enemy = min(enemies.sprites(), key=lambda e: math.hypot(e.rect.centerx - player.rect.centerx, e.rect.centery - player.rect.centery))
                else:
                    closest_enemy = None
                if closest_enemy:
                    if (current_time - last_missile_time) >= missile_cooldown * 1000:
                        last_missile_time = current_time
                        missile_on_cooldown = True
                        missile_speed_x, missile_speed_y = calc_speed(closest_enemy.rect.center, player.rect.center, closest_enemy.speed, bullet_speed)
                        lasers.add(Missile(missile_sprite, (player.rect.centerx, player.rect.centery)))

    screen.fill((0, 0, 0))

    if (not tutorial_shown):
        tutorial_shown = True
        show_tutorial(screen, font, screen_width, screen_height)
        last_difficulty_increase_time = pygame.time.get_ticks()

    if bossFight and (not bossSummoned):
        bossSummoned = True
        boss = Boss((screen_width / 2, 0))

    if bossSummoned:
        if random.randrange(100) < boss_shootChance * 100:
            bossBullets.add(BossBullet(bullet_sprite, (boss.rect.centerx, boss.rect.centery)))
        if boss.health <= 0:
            running = False
            bossDefeated = True

    update(player, difficulty, enemies, Enemy, screen_width, bossSummoned, boss, bossBullets, difficulties, heals, shoots, lasers, explosions)

    count, bossFight, difficulty, player.health, toggle_triple_shoot, triple_shoot_start_time, player.invincible, player.invincibility_timer = check_hits(lasers, enemies, explosion_sound, explosions, Sprite, explosion_sprite, enter_bossFight, boostAppearChance, difficulties, DecreaseDifficulty, screen_width, heals, Heal, shoots, TripleShoot, player, max_health, current_time, count, bossFight, difficulty, toggle_triple_shoot, triple_shoot_start_time, invincibleSeconds)
    
    if bossSummoned:
        player.health, player.invincible, player.invincibility_timer, boss.health = boss_check_hits(bossSummoned, player, enemies, invincibleSeconds, boss, lasers, bossBullets, bosses)
    
    missile_on_cooldown, toggle_triple_shoot, running, game_over = playerInfoUpdate(current_time, last_missile_time, missile_cooldown, missile_on_cooldown, triple_shoot_start_time, triple_shoot_duration, toggle_triple_shoot, player, running, game_over)
    
    drawEntities(player, lasers, enemies, explosions, difficulties, heals, shoots, screen, bossSummoned, boss, bossBullets)
    
    showInfo(player, max_health, font, screen, missile_on_cooldown, missile_cooldown, current_time, last_missile_time, difficulty, count, toggle_triple_shoot, triple_shoot_duration, triple_shoot_start_time, bossSummoned, boss_health, boss)
    pygame.display.flip()

if game_over:
    GameOver(game_over, screen, game_over_sprite, screen_width, screen_height, font, count)

if bossDefeated:
    BossDefeated(bossDefeated, count, boss_health, screen, font, screen_width, screen_height)

pygame.quit()