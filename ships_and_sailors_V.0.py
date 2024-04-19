# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:16:44 2024

@author: cough
"""

#if state of ship is 1 then move ship to location of the tile (under tile probably)

import simpleGE, pygame

class Ship(simpleGE.Sprite):

    def __init__(self, scene, color=(0, 0, 255)):
        super().__init__(scene)
        self.colorRect(color, (16,16))   
        self.position = (32,32)
        self.stateName = ["unselected", "selected"]
        
        self.UNSELECTED = 0
        self.SELECTED = 1

        self.setState(self.UNSELECTED)  
        
        self.attack_stat = 10  
        self.health_stat = 100  
        
    
    def setState(self, state):
        self.state = state
        
    def process(self):
        if self.clicked:
            newState = self.state + 1
            if newState > 1:
                newState = 0
            self.setState(newState)    
            print(self.state)
            
        
    
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.setCaption("Ships and Sailors")
        self.screenWidth = 800
        self.screenHeight = 600
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        
        self.tileset = []
        self.ship = []  
        
        self.ROWS = 40 
        self.COLS = 51
        
        self.loadMap()
        
        patrolBoat = Ship(self)
        enemyPatrolBoat = Ship(self, color=(255, 0, 0))
        
        self.ship.append(patrolBoat)
        self.ship.append(enemyPatrolBoat)
        
        patrolBoat.position = (32, 32)
        enemyPatrolBoat.position = (64, 64)

        
        
        
        self.sprites = [self.tileset, self.ship]  



    def loadMap(self):
      map = [
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      ]
    
      for row in range(self.ROWS):
        self.tileset.append([])
        for col in range(self.COLS):
            currentVal = map[row][col]
            newTile = Tile(self)  
            newTile.setState(currentVal)
            xPos = 0 + (16 * col)
            yPos = 0 + (16 * row)
            newTile.x = xPos
            newTile.y = yPos
            self.tileset.append(newTile)



class Instructions(simpleGE.Scene):
    def __init__(self, screenWidth, screenHeight):
        super().__init__()

        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
            "Welcome to Ships and Sailors!",
            "Click a ship, and then another grid square to move.",
            "Click a ship,",
            "and then on a square with an enemy ship to attack!",
            "Defeat all the enemy ships to win!",
            "Good Luck!"
        ]
        self.instructions.size = (700,500)
        self.screenHeight = 600
        self.screenWidth = 800
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.instructions.center = (400, 300)
        self.instructions.font = pygame.font.Font("Top Secret Stamp.ttf", 30)
        self.setCaption("How to Play") 
        
        self.btnMenu = simpleGE.Button()
        self.btnMenu.text = "Menu"
        self.btnMenu.center = (400, 575)

        self.sprites = [self.instructions, self.btnMenu]
        
    def process(self):

        if self.btnMenu.clicked:
            self.response = "Menu"
            self.stop()

class LblTitle(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Ships and Sailors"
        self.center = (400, 50)
        self.size = (600, 100)
        self.fgColor = (150,170,255)
        self.font = pygame.font.Font("Top Secret Stamp.ttf", 70)
        self.clearBack = True

class LblOutput(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (320, 25)
        self.text = "current tile: "
        self.fgColor = "white"
        self.bgColor = "black"
        self.clearBack = True
        
class Menu(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        pygame.init()
        scene = simpleGE.Scene()
        scene.setCaption("Menu")  
        self.screenWidth = 800
        self.screenHeight = 640
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.setImage("BG-Navy.jpg", autoSize = True)

        self.groups = []

        self.response = "Menu"
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play (up)"
        self.btnPlay.center = (150, 600)
        self.btnPlay.bgColor = (0,100,180)
        self.btnPlay.size = (200,30)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit (down)"
        self.btnQuit.center = (650, 600)
        self.btnQuit.bgColor = (0,100,180)
        self.btnQuit.size = (200,30)
        
        self.btnHowToPlay = simpleGE.Button()
        self.btnHowToPlay.text = "How to Play"
        self.btnHowToPlay.center = (400, 600)
        self.btnHowToPlay.bgColor = (0,100,180)
        self.btnHowToPlay.size = (200,30)
        
        self.lblTitle = LblTitle()
        self.sprites = [self.btnQuit,
                        self.btnPlay,
                        self.btnHowToPlay,
                        self.lblTitle]
        
    def process(self):

        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
        if self.btnHowToPlay.clicked:
            self.response = "How"
            self.stop()

        if self.isKeyPressed(pygame.K_UP):
            self.response = "Play"
            self.stop()
        if self.isKeyPressed(pygame.K_DOWN):
            self.response = "Quit"
            self.stop()


class Tile(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = [
            pygame.image.load("Water.png")]
        
        self.setSize(16, 16)
        self.WATER = 0
        self.state = self.WATER

    def setState(self, state):
        self.state = state
        self.copyImage(self.images[state])
        
    def process(self):
        if self.clicked:
            if self.scene.ship[0].state == 1:
                maxDistance = 16
                distance = self.scene.ship[0].distanceTo(self.position)
                if distance <= maxDistance:
                    self.scene.ship[0].state = 0 #add each ship instance to [0] as [0,1,2] etc.
                    self.scene.ship[0].position = self.position
                else:
                    print("Out of Range")
            print(self.position)
            
            

def main():
    keepGoing = True
    while keepGoing:
        menu = Menu()
        menu.start()
        
        if menu.response == "How":
            instructions = Instructions(menu.screenWidth, menu.screenHeight)
            instructions.start()
            if instructions.response == "Menu":
                continue
        if menu.response == "Play":    
            game = Game()
            game.start()
        elif menu.response == "Quit":
            keepGoing = False
        else:
            keepGoing = False

            
if __name__ == "__main__":
    main()
    