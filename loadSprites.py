import pygame

def load_sprite_svg(name, amplifier):
    path = f"{name}.svg"
    loaded_sprite = pygame.image.load(path)
    width, height = loaded_sprite.get_size()
    width *= amplifier
    height *= amplifier
    return pygame.transform.scale(loaded_sprite, (width, height))

def load_sprite_png(name, amplifier):
    path = f"{name}.png"
    loaded_sprite = pygame.image.load(path)
    width, height = loaded_sprite.get_size()
    width *= amplifier
    height *= amplifier
    return pygame.transform.scale(loaded_sprite, (width, height))

def load_sound(name):
    path = f"{name}.wav"
    return pygame.mixer.Sound(path)