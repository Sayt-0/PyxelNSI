import pyxel 

class Joueur2:
    def __init__(self):
        self.x=pyxel.width-20
        self.y=pyxel.height/2
        self.width=10
        self.high=30
        self.vitesse=2
    

    def update(self):
            if pyxel.btn(pyxel.KEY_UP)==True:
                self.y=self.y-self.vitesse
            elif pyxel.btn(pyxel.KEY_DOWN)==True:
                self.y=self.y+self.vitesse



    def draw(self):
            pyxel.rect(self.x,self.y,self.width,self.high,7)

    def collision(self,balle):
        if balle.x + balle.width/2 >= self.x  and balle.x + balle.width/2 <= self.x + self.width and balle.y + balle.width/2 >= self.y and balle.y - balle.width/2 <= self.y+self.high:
            balle.angle = 180 - balle.angle + pyxel.rndi(-10,10)

class Joueur1:
    def __init__(self):
        self.x=20
        self.y=pyxel.height/2
        self.width=10
        self.high=30
        self.vitesse=2
    

    def update(self):
            if pyxel.btn(pyxel.KEY_A)==True:
                self.y=self.y-self.vitesse
            elif pyxel.btn(pyxel.KEY_Q)==True:
                self.y=self.y+self.vitesse



    def draw(self):
            pyxel.rect(self.x,self.y,self.width,self.high,7)

    def collision(self,balle):
        if balle.x - balle.width/2 <= self.x + self.width and balle.x + balle.width/2 >= self.x and balle.y + balle.width >= self.y and balle.y - balle.width/2 <= self.y+self.high:
            balle.angle = 180 - balle.angle + pyxel.rndi(-10,10)


class balle:
    def __init__(self) -> None:
          self.x=pyxel.width/2
          self.y=pyxel.height/2
          self.width=6
          self.height=6
          self.angle=pyxel.rndi(-70,70)+180*pyxel.rndi(0,1)
          self.vitesse=0.5
          self.game_over=False

    def update(self):
         if self.game_over==False:
            self.x=self.x+self.vitesse*pyxel.cos(self.angle)
            self.y=self.y-self.vitesse*pyxel.sin(self.angle)
            if self.y <= self.height - self.width/2 or self.y >= pyxel.height - self.width + self.width/2:
                self.angle = -1*self.angle
            if self.x - self.width/2 < 0:
                self.game_over=True
            if self.x + self.width /2 > pyxel.width:
                self.game_over=True
    def draw(self):
         pyxel.circ(self.x,self.y,self.width/2,7)





class Game:
    def __init__(self):
        pyxel.init(160, 120, fps=120, title='dddd')
        self.j1 = Joueur1()
        self.j2 = Joueur2()
        self.b = balle()
        self.angle=pyxel.rndi(-70,70)+180*pyxel.rndi(0,1)
        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.j1.update()
        self.j2.update()
        self.b.update()
        self.j1.collision(self.b)
        self.j2.collision(self.b)
    def draw(self):
        pyxel.cls(0)
        self.j1.draw()
        self.j2.draw()
        self.b.draw()


Game()


