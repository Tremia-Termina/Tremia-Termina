import math
# 计算速度函数
def calc_speed(target_pos, source_pos, target_speed, bullet_speed):
    dx = target_pos[0] - source_pos[0]
    dy = target_pos[1] - source_pos[1]
    if dx > 0:
        theta = (math.pi - math.asin((-target_speed) / (bullet_speed * math.sqrt(1 + (dy / dx) ** 2))) - math.atan2(dy, -dx))
        return bullet_speed * math.cos(theta), bullet_speed * math.sin(theta) * -1
    elif dx < 0:
        theta = (math.pi - math.asin((-target_speed) / (bullet_speed * math.sqrt(1 + (dy / dx) ** 2))) - math.atan2(dy, dx))
        return bullet_speed * math.cos(theta) * -1, bullet_speed * math.sin(theta) * -1
    else:
        return 0, bullet_speed