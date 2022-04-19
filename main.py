import pygame
import sceneLoader

screen=None
mySceneLoader=sceneLoader.SceneLoader()

def load(pScreen):
    global screen
    screen=pScreen

    mySceneLoader.load(screen)
    mySceneLoader.init("menu")


def update(dt):
    mySceneLoader.update(dt)


def draw():
    mySceneLoader.draw()


def keypressed(pKey):

    if pKey[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

    mySceneLoader.keypressed(pKey)


def mousepressed(pBtn,pPos):
    mySceneLoader.mousepressed(pBtn, pPos)


def mousemove(pPos):
    mySceneLoader.mousemove(pPos)