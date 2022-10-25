import pygame
import numpy

screensize = (1920, 1080)


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(screensize)
    screen.fill((0, 0, 0))
    pygame.display.update()

    framerate = 60
    cumulativetime = 0

    running = True

    lastframe = pygame.time.get_ticks()

    questions = []
    answers = []
    correctanswers = []

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

    while running:
        t = pygame.time.get_ticks()
        dt = (t - lastframe) / 1000.0
        cumulativetime += dt
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False


if __name__ == '__main__':
    main()
