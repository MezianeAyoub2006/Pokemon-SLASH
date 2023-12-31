from engine import *

TILESETS = {
    "main_tileset" : load_sprite("tilesets/main.png", (32, 32))
}

SPRITES = {
    "player_walk_cycle" :  scale_animations(load_animation('player/walk_sprite.png', (32, 32), 3), (64, 64)),
    "pokemons" : scale_image_list(load_sprite("pokemons/overworld.png", (64, 128)), (128, 256))
}

OTHER = {
    "shadow" : pygame.transform.scale(load_image("player/shadow.png"), (64, 64))
}