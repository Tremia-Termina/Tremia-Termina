# 游戏设置

#若数值设置不合法，将自动调整为默认值

#难度设置
#基础难度（最小1）
base_difficulty = 1

#难度增加时间间隔（单位：秒）
difficulty_increase_interval = 10

#最大难度（最大100）
max_difficulty = 10

#进入Boss关卡的分数
enter_bossFight = 1



#玩家属性
#最大生命值（最小1）
max_health = 3

#移动速度
up_speed = 5
down_speed = 5
left_speed = 5
right_speed = 5

#无敌时间（单位：秒）
invincibleSeconds = 1

#导弹冷却（单位：秒）
missile_cooldown = 1

#三发射击持续时间（单位：秒）
triple_shoot_duration = 100



#子弹属性
#移动速度
bullet_speed = 10
bullet_leftSpeed = 5
bullet_rightSpeed = 5



#敌机属性
#移动速度
enemyMinSpeed = 1
enemyMaxSpeed = 3

#Boss生命值
boss_health = 100

#Boss移动速度
boss_leftSpeed = 3
boss_rightSpeed = 3

#Boss子弹属性
boss_bullet_minSpeed = 1
boss_bullet_maxSpeed = 3
boss_shootChance = 0.05



#增益属性
#移动速度
boostMinSpeed = 1
boostMaxSpeed = 3

#出现概率
boostAppearChance = 0.1



#动画属性
#持续时间（单位：秒）
explosionDelaySeconds = 0.5



def is_float(num):
    return bool(isinstance(num, float))



if base_difficulty < 0 or is_float(base_difficulty):
    base_difficulty = 1

if difficulty_increase_interval < 0:
    difficulty_increase_interval = 10

if max_difficulty > 100 or is_float(max_difficulty):
    max_difficulty = 20



if max_health < 0 or is_float(max_health):
    max_health = 3

if up_speed < 0 or up_speed > 100:
    up_speed = 5
if down_speed < 0 or down_speed > 100:
    down_speed = 5
if left_speed < 0 or left_speed > 100:
    left_speed = 5
if right_speed < 0 or right_speed > 100:
    right_speed = 5

if invincibleSeconds < 0:
    invincibleSeconds = 1

if missile_cooldown < 0:
    missile_cooldown = 1

if triple_shoot_duration < 0:
    triple_shoot_duration = 10



if bullet_speed < 0 or bullet_speed > 100:
    bullet_speed = 10
if bullet_leftSpeed < 0 or bullet_leftSpeed > 100:
    bullet_leftSpeed = 5
if bullet_rightSpeed < 0 or bullet_rightSpeed > 100:
    bullet_rightSpeed = 5



if enemyMinSpeed < 0:
    enemyMinSpeed = 1
if enemyMaxSpeed < 0:
    enemyMaxSpeed = 3
if enemyMinSpeed >= enemyMaxSpeed:
    enemyMinSpeed = 1
    enemyMaxSpeed = 3

if boss_health < 0 or is_float(boss_health):
    boss_health = 100
if boss_leftSpeed < 0 or boss_leftSpeed > 100:
    boss_leftSpeed = 3
if boss_rightSpeed < 0 or boss_rightSpeed > 100:
    boss_rightSpeed = 3

if boss_bullet_minSpeed < 0:
    boss_bullet_minSpeed = 1
if boss_bullet_maxSpeed < 0:
    boss_bullet_maxSpeed = 3
if boss_bullet_minSpeed >= boss_bullet_maxSpeed:
    boss_bullet_minSpeed = 1
    boss_bullet_maxSpeed = 3

if boss_shootChance < 0 or boss_shootChance > 1:
    boss_shootChance = 0.05



if boostMinSpeed < 0:
    boostMinSpeed = 1
if boostMaxSpeed < 0:
    boostMaxSpeed = 3
if boostMinSpeed >= boostMaxSpeed:
    boostMinSpeed = 1
    boostMaxSpeed = 3

if boostAppearChance < 0:
    boostAppearChance = 0.1



if explosionDelaySeconds < 0:
    explosionDelaySeconds = 0.5

def difficulty_setting():
    return base_difficulty, difficulty_increase_interval, max_difficulty, enter_bossFight

def player_setting():
    return max_health, up_speed, down_speed, left_speed, right_speed, invincibleSeconds, missile_cooldown, triple_shoot_duration

def bullet_setting():
    return bullet_speed, bullet_leftSpeed, bullet_rightSpeed

def enemy_setting():
    return enemyMinSpeed, enemyMaxSpeed, boss_health, boss_leftSpeed, boss_rightSpeed, boss_bullet_minSpeed, boss_bullet_maxSpeed, boss_shootChance

def boost_setting():
    return boostMinSpeed, boostMaxSpeed, boostAppearChance

def animation_setting():
    return explosionDelaySeconds