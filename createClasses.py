import pygame
import time
import random

def createSprite(explosionDelaySeconds):
    class Sprite(pygame.sprite.Sprite):
        def __init__(self, sprite, position=(20, 20)):
            super().__init__()
            self.image = sprite
            self.rect = self.image.get_rect()
            self.rect.topleft = position
            self.start_time = time.time()
        def update(self):
            if time.time() - self.start_time > explosionDelaySeconds:
                self.kill()
    return Sprite

def createPlayer(Sprite, player_sprite, max_health, up_speed, down_speed, left_speed, right_speed, screen_width, screen_height):
    class Player(Sprite):
        def __init__(self, position):
            super().__init__(player_sprite, position)
            self.lasers = pygame.sprite.Group()
            self.health = max_health
            self.invincible = False
            self.invincibility_timer = 0
        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.rect.y -= up_speed
            if keys[pygame.K_DOWN]:
                self.rect.y += down_speed
            if keys[pygame.K_LEFT]:
                self.rect.x -= left_speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += right_speed
            self.rect.x = max(0, min(screen_width - self.rect.width, self.rect.x))
            self.rect.y = max(0, min(screen_height - self.rect.height, self.rect.y))
    return Player

def createBullet(Sprite, bullet_sprite, bullet_speed):
    class Bullet(Sprite):
        def __init__(self, sprite, position):
            super().__init__(bullet_sprite, position)
            self.speed = bullet_speed
        def update(self):
            self.rect.y -= self.speed
            if self.rect.bottom < 0:
                self.kill()
    return Bullet

def createBulletLeft(Sprite, bullet_sprite, bullet_speed, bullet_leftSpeed):
    class BulletLeft(Sprite):
        def __init__(self, sprite, position):
            super().__init__(bullet_sprite, position)
            self.speed = bullet_speed
            self.speed_x = bullet_leftSpeed
        def update(self):
            self.rect.y -= self.speed
            self.rect.x -= self.speed_x
            if self.rect.bottom < 0:
                self.kill()
    return BulletLeft

def createBulletRight(Sprite, bullet_sprite, bullet_speed, bullet_rightSpeed):
    class BulletRight(Sprite):
        def __init__(self, sprite, position):
            super().__init__(bullet_sprite, position)
            self.speed = bullet_speed
            self.speed_x = bullet_rightSpeed
        def update(self):
            self.rect.y -= self.speed
            self.rect.x += self.speed_x
            if self.rect.bottom < 0:
                self.kill()
    return BulletRight

def createBossBullet(Sprite, boss_bullet_sprite, boss_bullet_minSpeed, boss_bullet_maxSpeed):
    class BossBullet(Sprite):
        def __init__(self, sprite, position):
            super().__init__(boss_bullet_sprite, position)
            self.speed_x = random.uniform(boss_bullet_minSpeed, boss_bullet_maxSpeed)
            key = random.randrange(1, 3)
            if key == 2:
                self.speed_x *= -1
            self.speed_y = random.uniform(boss_bullet_minSpeed, boss_bullet_maxSpeed)
        def update(self):
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            if self.rect.bottom < 0:
                self.kill()
    return BossBullet

def createMissile(Sprite, missile_sprite, missile_speed_x, missile_speed_y):
    class Missile(Sprite):
        def __init__(self, sprite, position):
            super().__init__(missile_sprite, position)
            self.speed_x = missile_speed_x
            self.speed_y = missile_speed_y
        def update(self):
            self.rect.x+= self.speed_x
    return Missile

def createEnemy(Sprite, enemy_sprite, enemyMinSpeed, enemyMaxSpeed, screen_height, player):
    class Enemy(Sprite):
        def __init__(self, position):
            super().__init__(enemy_sprite, position)
            self.speed = random.uniform(enemyMinSpeed, enemyMaxSpeed)
        def update(self):
            self.rect.y += self.speed
            if self.rect.top > screen_height:
                if player.health > 0:
                    player.health -= 1
                self.kill()
    return Enemy

def createBoss(Sprite, boss_sprite, boss_health, boss_leftSpeed, boss_rightSpeed, screen_width):
    class Boss(Sprite):
        def __init__(self, position):
            super().__init__(boss_sprite, position)
            self.health = boss_health
            self.target = None
            self.speed = None
            self.new_target()
        def new_target(self):
            self.target = random.uniform(0, screen_width - self.rect.width)
            while True:
                self.speed = random.uniform(-boss_leftSpeed, boss_rightSpeed)
                if abs(self.speed) >= 0.5:
                    break
        def update(self):
            if self.health <= 0:
                self.kill()
            if self.rect.x != self.target:
                self.rect.x += self.speed
                if (self.speed > 0 and self.rect.x > self.target) or (self.speed < 0 and self.rect.x < self.target):
                    self.new_target()
            self.rect.x = max(0, min(screen_width - self.rect.width, self.rect.x))
    return Boss

def createDecreaseDifficulty(Sprite, decreaseDifficulty_sprite, boostMinSpeed, boostMaxSpeed, screen_height):
    class DecreaseDifficulty(Sprite):
        def __init__(self, position):
            super().__init__(decreaseDifficulty_sprite, position)
            self.speed = random.uniform(boostMinSpeed, boostMaxSpeed)
        def update(self):
            self.rect.y += self.speed
            if self.rect.top > screen_height:
                self.kill()
    return DecreaseDifficulty

def createHeal(Sprite, heal_sprite, boostMinSpeed, boostMaxSpeed, screen_height):
    class Heal(Sprite):
        def __init__(self, position):
            super().__init__(heal_sprite, position)
            self.speed = random.uniform(boostMinSpeed, boostMaxSpeed)

        def update(self):
            self.rect.y += self.speed
            if self.rect.top > screen_height:
                self.kill()
    return Heal

def createTripleShoot(Sprite, tripleShoot_sprite, boostMinSpeed, boostMaxSpeed, screen_height):
    class TripleShoot(Sprite):
        def __init__(self, position):
            super().__init__(tripleShoot_sprite, position)
            self.speed = random.uniform(boostMinSpeed, boostMaxSpeed)
        def update(self):
            self.rect.y += self.speed
            if self.rect.top > screen_height:
                self.kill()
    return TripleShoot