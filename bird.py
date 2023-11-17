class Bird:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.height = 100 ## FIX
        self.width = 50 ## FIX
        self.vel = 0

    def updateBird(self, distance):
        self.y += distance
        if self.y < 0:
            self.y = 0

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    