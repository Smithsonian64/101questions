import pygame
import numpy
import time
import threading

screensize = (1920, 1080)
screen = pygame.display.set_mode(screensize)
backgroundcolor = pygame.Color(0, 0, 0, 0)
fps = 60
currentquestion = 0

questions = []
answers = []
correctanswers = []
threads = []

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

def main():




    screen.fill((0, 0, 0))
    pygame.display.update()

    framerate = 60
    cumulativetime = 0

    running = True

    lastframe = pygame.time.get_ticks()



    questionsfile = open("questions.txt", 'r')
    index = 0
    answerschunk = ['', '', '', '']
    for line in questionsfile:
        if index == 0:
            questions.append(line.replace('\n', ''))
            index += 1
            continue
        if 0 < index < 5:
            if line.find('*') != -1:
                correctanswers.append(line.replace("*", "").replace('\n', ''))
            answerschunk[index - 1] = line.replace('*', '').replace('\n', '')
            index += 1

        if index >= 5:
            answers.append((answerschunk[0], answerschunk[1], answerschunk[2], answerschunk[3]))
            index = 0

    print(questions)
    print(answers)
    print(correctanswers)
    t1 = threading.Thread(target=changetocolor, args=(pygame.Color(0, 0, 255), 0.25))
    t2 = threading.Thread(target=displayquestion, args=())
    threads.append(t1)
    threads.append(t2)
    while running:
        t = pygame.time.get_ticks()
        dt = (t - lastframe) / 1000.0
        cumulativetime += dt

        if len(threads) != 0:
            for thread in threads:
                if not thread.is_alive()
                thread.start()
                if not thread.is_alive():
                    print('dead')
                    threads.remove(thread)




        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

def changetocolor(color, duration=1):
    basecolor = backgroundcolor
    targetcolor = color

    baser = backgroundcolor.r
    baseg = backgroundcolor.g
    baseb = backgroundcolor.b

    targetr = targetcolor.r
    targetg = targetcolor.g
    targetb = targetcolor.b

    intervalr = (targetr - baser) / fps
    intervalg = (targetg - baseg) / fps
    intervalb = (targetb - baseb) / fps

    for i in range(0, fps):
        starttime = time.time_ns()
        while time.time_ns() - starttime < 16666667 * duration:
            pass
        baser += intervalr
        baseg += intervalg
        baseb += intervalb
        screen.fill((int(numpy.ceil(baser)), int(numpy.ceil(baseg)), int(numpy.ceil(baseb))))
    print(baser, baseg, baseb)

def displayquestion():
    questionblock = font.render(questions[currentquestion], False, (0, 0, 0))
    while True > 0:
        pass
    print('hello')
    screen.blit(questionblock, (100, 100))

def addthread(thread):
    threads.append(thread)

if __name__ == '__main__':
    main()

