import pygame
import main

#init screen
screen=pygame.display.set_mode((1024,600))
pygame.display.set_caption("RunnerColor")

#init font
pygame.font.init()

#init mixer(for the sounds)
pygame.mixer.init()


bRun=True
lastUpdate=pygame.time.get_ticks()
clock=pygame.time.Clock()


def init():
    global screen

    main.load(screen)
    run()


def run():
    global bRun
    global lastUpdate

    #gameloop
    while bRun:

        # calcul deltatime
        now = pygame.time.get_ticks()
        dt = (now - lastUpdate) /1000
        lastUpdate = now

        screen.fill([0,0,0])

        main.update(dt)
        main.draw()
        pygame.display.update()


        #events
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                bRun=False
                pygame.quit()
                quit()

            elif event.type==pygame.MOUSEBUTTONDOWN:
                main.mousepressed(pygame.mouse.get_pressed(3),pygame.mouse.get_pos())

            elif event.type==pygame.MOUSEMOTION:
                main.mousemove(pygame.mouse.get_pos())

            elif event.type==pygame.KEYDOWN:
                keys=pygame.key.get_pressed()
                main.keypressed(keys)


        clock.tick(60)


init()
