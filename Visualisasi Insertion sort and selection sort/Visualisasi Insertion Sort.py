import pygame as gim
import random, sys

resolution = (640, 480)
gim.init()
gim.font.init()
myfont = gim.font.SysFont('Calibri', 15)
screen = gim.display.set_mode(resolution)
gim.display.set_caption('Sorting Algorithm')

n_input = input("masukan nilai 'n' =")
n = int(n_input)

start = True

#generate random value for bar width
width = []
for i in range(n):
    random_list = random.randint(1, n)
    width.append(random_list)

print('n =', width)
#generate bar
red = (255, 0, 0)
blue = (0, 0, 255)
screen.fill(0)
j = 0
k = 0
count = 0
value = []

#insertion Algorithm
def insertion(value):
    for pas in range(1, len(value)):
        temp = value[pas]
        i = pas - 1
        while i >= 0 and value[i] > temp:
            value[i +1] = value[i]
            i = i - 1
        value[i + 1] = temp

#selection sort
'''def selection(value) :
    for pas in range(0,len(value)-1):
        i_min=pas
        for i in range(i_min+1,len(value)) :
            if value[i] < value[i_min]:
                i_min=i
        temp=value[pas]
        value[pas]=value[i_min]
        value[i_min]=temp'''

i_min = 0
while start:
    for i in width:
        bar = gim.Rect(0, j, i, 2)
        j += 3
        gim.draw.rect(screen, red, bar)
        gim.display.flip()
    j = 0

    for i in range(n):
        selection(width)
        bar = gim.Rect(n, j, i, 2)
        j += 3
        gim.draw.rect(screen, blue, bar)
        gim.display.flip()
    
    j = 0
    after = myfont.render('Seteleh diurutkan', width, False, blue)
    screen.blit(after, (n+50, 100))

    for event in gim.event.get():
        if event.type == gim.QUIT:
            gim.quit()
            exit(0)
