import random

class Pipe:
    def __init__(self, x = 400):
        self.topImage = 'images/topPipe2.png'
        self.bottomImage = 'images/bottomPipe2.png'
        self.X = x
        self.bottomY = random.randint(250, 650)
        self.topY = self.bottomY - 800

    def getTopImage(self):
        return self.topImage

    def getBottomImage(self):
        return self.bottomImage
    
    def getX(self):
        return self.X
    
    def getTopY(self):
        return self.topY
    
    def getBottomY(self):
        return self.bottomY
    
    def movePipes(self):
        self.X -= 5
        if self.X < -100:
            self.X = 600
            self.bottomY = random.randint(250, 650)
            self.topY = self.bottomY - 800