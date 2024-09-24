import pyxel 




class Joueur1:
    def __init__(self):
    self.x=20
    self.y=pyxel.height/2
    self.width=10
    self.height=30
    self.vitesse=4



def update(self):
    if pyxel.btn(pyxel.KEY_A) == True:
        self.y=self.y-self.vitesse
    elif pyxel.btn(pyxel.key_Q) == True:
        self.y=self.y+self.vitesse


def draw(self):
    pyxel.rect(self.x, self.y, self.width, self.height, 7)

class Game:
    def __init__(self) -> None:
        pyxel.init(160, 120, 'Bougnoule', 120)
        pyxel.run(self.update, self.draw)
    
    def update(self):
        pass
    def draw(self):
        pass

Game()


