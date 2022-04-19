class GameplayService:

    def __init__(self):
        self.screen=None
        self.assetManager=None
        self.utils=None
        self.GuiManager=None

        self.objectManager=None
        self.enemyManager=None

        self.currentMap=None
        self.currentLevel=1
        self.maxLevel = 3
        self.nbCoin=0


    def setScreen(self,pScreen):
        self.screen=pScreen


    def setAssetManager(self,pAssetManager):
        self.assetManager=pAssetManager


    def setGUIManager(self,pGuiManager):
        self.GuiManager=pGuiManager


    def setUtils(self,pUtils):
        self.utils=pUtils


    def setObjectManager(self,pObjectManager):
        self.objectManager=pObjectManager


    def setMap(self,pMap):
        self.currentMap=pMap


    def setEnemyManager(self,pEnemyManager):
        self.enemyManager=pEnemyManager