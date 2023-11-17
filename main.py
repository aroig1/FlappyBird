import pygame as py
from bird import Bird
from pipe import Pipe

class FlappyBird:
    def __init__(self):
        py.init()
        self.DaBird = Bird()
        self.screen = py.display.set_mode((500, 750))
        py.display.set_caption("Flappy Bird")
        self.logo = py.image.load('images/logo.png')
        self.birdImg = py.image.load('images/bird.png')
        self.background = py.image.load('images/background.png')

        self.pipes1 = Pipe()
        self.topPipe1 = py.image.load(self.pipes1.getTopImage())
        self.bottomPipe1 = py.image.load(self.pipes1.getBottomImage())
        self.pipes2 = Pipe(self.pipes1.getX() + 350)
        self.topPipe2 = py.image.load(self.pipes2.getTopImage())
        self.bottomPipe2 = py.image.load(self.pipes2.getBottomImage())
        
        self.flyCount = 20
        

    def runGame(self):
        gameRunning = True
        start = True
        end = False

        while gameRunning:
            py.time.delay(25)

            keys = py.key.get_pressed()

            if end:
                self.endSequence()
                end = False
                start = True

            if start:
                self.startSequence()
                start = False

            for event in py.event.get():
                if event.type == py.QUIT:
                    gameRunning = False

            if self.DaBird.getY() > 750: 
                end = True

            if keys[py.K_SPACE]:
                self.flyCount = -20

            self.DaBird.updateBird(self.flyCount)
            self.flyCount += 2

            self.pipes1.movePipes()
            self.pipes2.movePipes()

            self.updateScreen()

        py.quit()

    def startSequence(self):
        self.flyCount = 20

        keys = py.key.get_pressed()
        
        while not keys[py.K_SPACE]:

            py.time.delay(25)

            keys = py.key.get_pressed()

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()

            self.startScreen()

    def endSequence(self):
        pass

    def startScreen(self):
        # display background
        self.screen.blit(self.background, (0, 0))
        # display bird
        self.screen.blit(self.birdImg, (self.DaBird.getX(), self.DaBird.getY()))
        # display pipes
        self.updatePipes() 
        # add logo
        self.screen.blit(self.logo, (50, 100))

        py.display.update()

    def updateScreen(self):
        # display background
        self.screen.blit(self.background, (0, 0))
        # display bird
        self.screen.blit(self.birdImg, (self.DaBird.getX(), self.DaBird.getY()))
        # display pipes
        self.updatePipes() 

        py.display.update()

    def updatePipes(self):
        self.screen.blit(self.topPipe1, (self.pipes1.getX(), self.pipes1.getTopY()))
        self.screen.blit(self.bottomPipe1, (self.pipes1.getX(), self.pipes1.getBottomY()))
        self.screen.blit(self.topPipe2, (self.pipes2.getX(), self.pipes2.getTopY()))
        self.screen.blit(self.bottomPipe2, (self.pipes2.getX(), self.pipes2.getBottomY()))

if __name__ == '__main__':
    game = FlappyBird()
    game.runGame()