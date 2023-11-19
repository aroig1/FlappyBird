class Bird:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.hitbox = (self.x + 40, self.y, 90, 50)

    def updateBird(self, distance):
        self.y += distance
        if self.y < 0:
            self.y = 0
        self.hitbox = (self.x + 10, self.y + 4, 70, 45)

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getHitbox(self):
        return self.hitbox

    