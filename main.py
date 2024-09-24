import pyxel 

class Game:
    def __init__(self) -> None:
        pyxel.init(160, 120)
        pyxel.run(self.update, self.draw)
    
    def update(self):
        pass
    def draw(self):
        pass

Game()