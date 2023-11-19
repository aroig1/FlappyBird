class Scoreboard:
    def __init__(self):
        self.score = 0
        self.best = 65 # Aidan's Score
        self.medals = ['images/bronzeMedal.png', 'images/silverMedal.png']
        self.template = 'images/scoreboard.png'

    def addPoint(self):
        self.score += 1

    def updateBest(self):
        if self.score > self.best:
            self.best = self.score
    
    def getBest(self):
        return self.best
    
    def getScore(self):
        return self.score
    
    def setScore(self, score):
        self.score = score
    
    def getTemplate(self):
        return self.template

    def getMedal(self):
        if self.score < 10:
            return None
        elif self.score < 20:
            return self.medals[0]
        elif self.score < 30:
            return self.medals[1]