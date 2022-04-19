import pygame.font

import assetManager
import utils
import gameplayService

import GUIManager

import sceneGame
import sceneMenu
import sceneGameover

class SceneLoader:

    def __init__(self):
        self.gameState=""

        self.myAssetManager = None
        self.myUtils=None
        self.myGameplayService = None
        self.myGUIManager=None

        self.mySceneGame=sceneGame.SceneGame()
        self.mySceneMenu=sceneMenu.SceneMenu()
        self.mySceneGameover=sceneGameover.SceneGameover()


    def load(self,pScreen):
        self.myAssetManager=assetManager.AssetManager()
        self.myUtils=utils.Utils()
        self.myGUIManager=GUIManager.GUI()

        #add images
        self.myAssetManager.addImage("images/tiles/tiles.png")


            ###player###
        self.myAssetManager.addImage("images/player/idle.png")
        self.myAssetManager.addImage("images/player/jump.png")
        self.myAssetManager.addImage("images/player/ladder.png")
        self.myAssetManager.addImage("images/player/move.png")
        self.myAssetManager.addImage("images/player/rope.png")


            ###enemy###
        self.myAssetManager.addImage("images/enemy/idle.png")
        self.myAssetManager.addImage("images/enemy/move.png")
        self.myAssetManager.addImage("images/enemy/ladder.png")
        self.myAssetManager.addImage("images/enemy/rope.png")

        self.myAssetManager.addImage("images/objects/paintBuckets.png")
        self.myAssetManager.addImage("images/objects/cleMolette.png")

            ####BG###
        self.myAssetManager.addImage("images/BG/bgMenu.png")
        self.myAssetManager.addImage("images/BG/bgGameover.png")

        ###add sounds
        self.myAssetManager.addSound("sounds/musics/game-over-danijel-zambo-main-version-02-03-1394.mp3")

        self.myAssetManager.addSound("sounds/FGBS(7).ogg")
        self.myAssetManager.addSound("sounds/FGBS(11).ogg")

        self.myGameplayService=gameplayService.GameplayService()

        self.myGameplayService.setScreen(pScreen)
        self.myGameplayService.setUtils(self.myUtils)
        self.myGameplayService.setGUIManager(self.myGUIManager)
        self.myGameplayService.setAssetManager(self.myAssetManager)


    def init(self,pGameState):
        self.gameState=pGameState

        self.myGUIManager.totalDelete()

        if self.gameState=="menu":
            self.mySceneMenu.load(self.myGameplayService,self)
        elif self.gameState=="gameplay":
            self.mySceneGame.load(self.myGameplayService, self)
        elif self.gameState=="gameover":
            self.mySceneGameover.load(self.myGameplayService, self)


    def update(self,dt):

        if self.gameState == "menu":
            self.mySceneMenu.update(dt)
        elif self.gameState == "gameplay":
            self.mySceneGame.update(dt)
        elif self.gameState == "gameover":
            self.mySceneGameover.update(dt)

        self.myGUIManager.update(dt)


    def draw(self):

        if self.gameState == "menu":
            self.mySceneMenu.draw()
        elif self.gameState == "gameplay":

            self.mySceneGame.draw()
            self.myGUIManager.draw(self.myGameplayService.screen)

        elif self.gameState == "gameover":
            self.mySceneGameover.draw()

    def keypressed(self,pKey):

        if self.gameState == "menu":
            self.mySceneMenu.keypressed(pKey)
        elif self.gameState == "gameplay":
            self.mySceneGame.keypressed(pKey)
        elif self.gameState == "gameover":
            self.mySceneGameover.keypressed(pKey)


    def mousepressed(self,pBtn,pPos):

        if self.gameState == "menu":
            print("mousepressedMenu")
        elif self.gameState == "gameplay":
            print("mousepressedGame")
        elif self.gameState == "gameover":
            print("mousepressedGameover")


    def mousemove(self,pPos):

        if self.gameState == "menu":
            print("mousemoveMenu")
        elif self.gameState == "gameplay":
            print("mousemoveGame")
        elif self.gameState == "gameover":
            print("movemoveGameover")