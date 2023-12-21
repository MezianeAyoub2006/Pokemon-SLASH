class GameObject:
    
    def __init__(self, game, z_pos=0):
        self.game = game
        self.tags = ["@game_object"]
        self.z_pos = z_pos
        self.erased = False

    def kill(self):
        self.erased = True

    def update(self, scene):
        pass