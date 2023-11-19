import pygame as py

class Button:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.height = 70
        self.width = width

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def isClicked(self):
        mouse_x, mouse_y = py.mouse.get_pos()
        if (self.x <= mouse_x <= self.x + self.width) and (self.y <= mouse_y <= self.y + self.height):
            return True
        else:
            return False