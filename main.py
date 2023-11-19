import pygame as py
from bird import Bird
from pipe import Pipe
from scoreboard import Scoreboard
from button import Button

class FlappyBird:
    def __init__(self):
        py.init()
        self.DaBird = Bird()
        self.screen = py.display.set_mode((500, 750))
        py.display.set_caption("Flappy Bird")
        self.logo = py.image.load('images/logo.png')
        self.birdImg = py.image.load('images/bird.png')
        self.background = py.image.load('images/background.png')

        self.scoreboard = Scoreboard()
        self.scoreTemplate = py.image.load(self.scoreboard.getTemplate())
        self.font = py.font.Font('fonts/square-deal.ttf', 100)
        self.startBtn = Button(50, 550, 166)
        self.startImg = py.image.load('images/start_btn.png')
        self.exitBtn = Button(300, 550, 143)
        self.exitImg = py.image.load('images/exit_btn.png')

        self.pipes1 = Pipe()
        self.topPipe1 = py.image.load(self.pipes1.getTopImage())
        self.bottomPipe1 = py.image.load(self.pipes1.getBottomImage())
        self.pipes2 = Pipe(self.pipes1.getX() + 350)
        self.topPipe2 = py.image.load(self.pipes2.getTopImage())
        self.bottomPipe2 = py.image.load(self.pipes2.getBottomImage())
        
        self.flyCount = 20
        self.gameRunning = False
        self.start = True
        self.end = False


    def runGame(self):
        self.gameRunning = True
        self.start = True
        self.end = False

        while self.gameRunning:
            py.time.delay(25)

            keys = py.key.get_pressed()

            # game over screen
            if self.end:
                self.endSequence()
                self.end = False
                self.start = True

            # start screen
            if self.start and self.gameRunning:
                self.startSequence()
                self.start = False
                self.flyCOunt = -15

            # Browser closed
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.gameRunning = False

            # collision / fell to bottom
            if self.DaBird.getY() > 750 or self.collision(): 
                self.end = True

            # jump
            if keys[py.K_SPACE] or py.mouse.get_pressed()[0]:
                self.flyCount = -15

            # Update Score
            if 0 < self.pipes1.getX() - self.DaBird.getX() <= 5 or 0 < self.pipes2.getX() - self.DaBird.getX() <= 5:
                self.scoreboard.addPoint()

            self.DaBird.updateBird(self.flyCount)
            self.flyCount += 2

            self.pipes1.movePipes()
            self.pipes2.movePipes()

            self.updateScreen()

        py.quit()

    def startSequence(self):
        self.flyCount = 20
        self.scoreboard.setScore(0)
        self.DaBird = Bird()
        self.pipes1 = Pipe()
        self.pipes2 = Pipe(self.pipes1.getX() + 350)

        keys = py.key.get_pressed()
        
        while not keys[py.K_SPACE] and not py.mouse.get_pressed()[0]:

            py.time.delay(25)

            keys = py.key.get_pressed()

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.gameRunning = False
                    return

            self.startScreen()

    def endSequence(self):
        keys = py.key.get_pressed()

        self.scoreboard.updateBest()
        
        while True:
            py.time.delay(25)

            keys = py.key.get_pressed()

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.gameRunning = False
                    return
                elif event.type == py.MOUSEBUTTONUP and self.exitBtn.isClicked():
                    self.gameRunning = False
                    return
                elif event.type == py.MOUSEBUTTONUP and self.startBtn.isClicked():
                    return
                        
            
            self.endScreen()
            

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

    def endScreen(self):
        # display background
        self.screen.blit(self.background, (0, 0))
        # display bird
        self.screen.blit(self.birdImg, (self.DaBird.getX(), self.DaBird.getY()))
        # display pipes
        self.updatePipes() 
        # display scoreboard
        self.screen.blit(self.scoreTemplate, (25, 150))
        # display medal
        if self.scoreboard.getMedal() != None:
            medal = py.image.load(self.scoreboard.getMedal())
            self.screen.blit(medal, (75, 350))
        # display score
        font = py.font.Font('fonts/square-deal.ttf', 55)
        text = font.render(str(self.scoreboard.getScore()), True, (255, 255, 255))
        self.screen.blit(text, (400, 345))
        # display best score
        text2 = font.render(str(self.scoreboard.getBest()), True, (255, 255, 255))
        self.screen.blit(text2, (400, 430))
        # Display buttons
        self.screen.blit(self.startImg, (self.startBtn.getX(), self.startBtn.getY()))
        self.screen.blit(self.exitImg, (self.exitBtn.getX(), self.exitBtn.getY()))

        py.display.update()

    def updateScreen(self):
        # display background
        self.screen.blit(self.background, (0, 0))
        # display bird
        self.screen.blit(self.birdImg, (self.DaBird.getX(), self.DaBird.getY()))
        # py.draw.rect(self.screen, (255, 0, 0), self.DaBird.getHitbox(), 2) # Comment / Uncomment to show Hitbox
        # display pipes
        self.updatePipes() 
        # display score
        text = self.font.render(str(self.scoreboard.getScore()), True, (255, 255, 255))
        self.screen.blit(text, (250, 100))

        py.display.update()

    def updatePipes(self):
        self.screen.blit(self.topPipe1, (self.pipes1.getX(), self.pipes1.getTopY()))
        self.screen.blit(self.bottomPipe1, (self.pipes1.getX(), self.pipes1.getBottomY()))
        self.screen.blit(self.topPipe2, (self.pipes2.getX(), self.pipes2.getTopY()))
        self.screen.blit(self.bottomPipe2, (self.pipes2.getX(), self.pipes2.getBottomY()))

        # Comment / Uncomment to show Hitboxes
        # py.draw.rect(self.screen, (255, 0, 0), self.pipes1.getTopHitbox(), 2)
        # py.draw.rect(self.screen, (255, 0, 0), self.pipes1.getBottomHitbox(), 2)
        # py.draw.rect(self.screen, (255, 0, 0), self.pipes2.getTopHitbox(), 2)
        # py.draw.rect(self.screen, (255, 0, 0), self.pipes2.getBottomHitbox(), 2)

    def collision(self):
        birdHitbox = self.DaBird.getHitbox()
        topPipe1Hitbox = self.pipes1.getTopHitbox()
        bottomPipe1Hitbox = self.pipes1.getBottomHitbox()
        topPipe2Hitbox = self.pipes2.getTopHitbox()
        bottomPipe2Hitbox = self.pipes2.getBottomHitbox()

        ## PIPE 1
        # Check front edge
        if (birdHitbox[0] + birdHitbox[2] >= topPipe1Hitbox[0]) and (birdHitbox[0] + birdHitbox[2] <= topPipe1Hitbox[0] + topPipe1Hitbox[2]):
            # check top pipe
            if (birdHitbox[1] <= topPipe1Hitbox[1] + topPipe1Hitbox[3]):
                return True
            # check bottom pipe
            if (birdHitbox[1] + birdHitbox[3] >= bottomPipe1Hitbox[1]):
                return True
        # Check back edge
        if (birdHitbox[0] >= topPipe1Hitbox[0]) and (birdHitbox[0] <= topPipe1Hitbox[0] + topPipe1Hitbox[2]):
            if (birdHitbox[1] <= topPipe1Hitbox[1] + topPipe1Hitbox[3]):
                return True
            # check bottom pipe
            if (birdHitbox[1] + birdHitbox[3] >= bottomPipe1Hitbox[1]):
                return True

        ## PIPE 2
        if (birdHitbox[0] + birdHitbox[2] >= topPipe2Hitbox[0]) and (birdHitbox[0] + birdHitbox[2] <= topPipe2Hitbox[0] + topPipe2Hitbox[2]):
            # check top pipe
            if (birdHitbox[1] <= topPipe2Hitbox[1] + topPipe2Hitbox[3]):
                return True
            # check bottom pipe
            if (birdHitbox[1] + birdHitbox[3] >= bottomPipe2Hitbox[1]):
                return True
        # Check back edge
        if (birdHitbox[0] >= topPipe2Hitbox[0]) and (birdHitbox[0] <= topPipe2Hitbox[0] + topPipe2Hitbox[2]):
            if (birdHitbox[1] <= topPipe2Hitbox[1] + topPipe2Hitbox[3]):
                return True
            # check bottom pipe
            if (birdHitbox[1] + birdHitbox[3] >= bottomPipe2Hitbox[1]):
                return True


if __name__ == '__main__':
    game = FlappyBird()
    game.runGame()