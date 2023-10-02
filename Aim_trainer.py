import math
import random
import time
import pygame

pygame.init() #make pygame work

WIDTH, HEIGHT = 800,600

WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #makiung a window with the hight and width
pygame.display.set_caption("Aim Trainer") #the title

TARGET_INCREMENT = 400 #how mach milisec per frame
TARGET_EVENT = pygame.USEREVENT #taregt event

TARGET_PADDING = 30
BG_COLOR = (0,25,40) #RGB values
LIVES = 3
TOP_BAR_HEIGHT = 50
LABEL_FONT = pygame.font.SysFont("comicsans", 24) #24 is the size and the font(can be ariel

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2 # how many pixels we want to grow by frame
    COLOR = "red"
    SECOUND_COLOR = "white"

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 0 #the starting size
        self.grow = True #false make it shrink

    def update(self):
        if self.size +self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE #the swhrinking part

    def draw(self,win):
        pygame.draw.circle(win,self.COLOR,(self.x,self.y),self.size) #circle(win we want the circle onto, color, center psition, radius)
        pygame.draw.circle(win, self.SECOUND_COLOR, (self.x, self.y), self.size*0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size*0.6)
        pygame.draw.circle(win, self.SECOUND_COLOR, (self.x, self.y), self.size*0.4)#make the target, getting smaller in size

    def collide(self,x,y): #the area that he hits the target
        # we want to chack with a line if the line between the mouse and the center of circle smaller then the radius
        #the order of(self.x-x)**2+(self.y-y)**2 shold be the same couse 1 of them is the center of te mouth and 1 is the center of the circle
        dis = math.sqrt((self.x-x)**2+(self.y-y)**2) #the distance between the 2 point,( we did it ^2 to ignore the minus the absulot value.
        return dis <= self.size #chacing if it in the border of the circle

def draw(win,targets):
    #need to clear the screen and draw the next frame every single fram
    win.fill(BG_COLOR)

    for target in targets:
        target.draw(win)

    #update the new frame

def format_time(secs):
    milli = math.floor(int(secs*1000%1000)/100)#gives the number of secnds from milisecoundes
    seconds = int(round(secs%60,1)) #the % 60 gives the number of secounds we have
    minutes = int(secs//60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"

    #02d give ne 2 digits, if theare is no 2 digit start it with 0.. 00, 01 ,02
def draw_top_bar(win,elapsed_time,targets_pressed,misses):
    pygame.draw.rect(win,"grey", (0,0, WIDTH,TOP_BAR_HEIGHT )) #diside whre to start x,y and then thw witdh and hight of the bar
    time_label = LABEL_FONT.render(
        f"Time:{format_time(elapsed_time)}",1,"black")
    speed = round(targets_pressed/ elapsed_time,1)
    speed_label = LABEL_FONT.render(f"Speed:{speed} t/s",1,"black")

    hits_label = LABEL_FONT.render(f"Hits:{targets_pressed} ", 1, "black")

    live_label = LABEL_FONT.render(f"Lives:{LIVES-misses} ", 1, "black")

    win.blit(time_label,(5,5))#blit make to display another serfece, and we diside the placemant
    win.blit(speed_label,(200, 5))
    win.blit(hits_label, (450, 5))
    win.blit(live_label, (650, 5))

def end_screen(win,elapsed_time,targets_prassed, clicks):
    win.fill(BG_COLOR)
    time_label = LABEL_FONT.render(
        f"Time:{format_time(elapsed_time)}",1,"white")
    speed = round(targets_prassed/ elapsed_time,1)
    speed_label = LABEL_FONT.render(f"Speed:{speed} t/s",1,"white")

    hits_label = LABEL_FONT.render(f"Hits:{targets_prassed} ", 1, "white")

    accuracy = round(targets_prassed/clicks*100, 1)
    accuracy_label = LABEL_FONT.render(f"Accuracy:{accuracy}%", 1, "white")

    win.blit(time_label, (get_middle(time_label), 100))  # we want it in the middle so we do x/2-Width/2 couse we start in the left and print to the right side
    win.blit(speed_label, (get_middle(speed_label),200))
    win.blit(hits_label, (get_middle(hits_label), 300))
    win.blit(accuracy_label, (get_middle(accuracy_label), 400))

    pygame.display.update()

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()


def get_middle(surface):
    return WIDTH/2 - surface.get_width()/2


def main():
    run = True
    targets = [] #where we store all the targets
    clock = pygame.time.Clock()

    target_pressed = 0
    clicks = 0
    misses = 0
    start_time= time.time()

    pygame.time.set_timer(TARGET_EVENT,TARGET_INCREMENT) #triger the event(TARGET_EVENT) every several sec( increment_evet) secounds

    #tell x to close the window
    while run:
        clock.tick(60) # make the appirance slower
        click = False
        mouse_pos = pygame.mouse.get_pos() # give us the x y position of the mouse, pos(x,y)
        elapsed_time = time.time()- start_time #taking the current time and substract it from the nuber of elipse sec

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING,WIDTH-TARGET_PADDING) #to make it stay in the borders of the window
                y = random.randint(TARGET_PADDING+TOP_BAR_HEIGHT,HEIGHT-TARGET_PADDING)# couses not be out of the window
                target = Target(x,y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for target in targets:
            target.update() #update all the targets by update them and the will change

            if target.size <= 0:
                targets.remove(target)#if its 0 size we delte it from the list , it make the timer smooth and not explode the storgae
                misses +=1 #we miss so it added to misses

            if click and target.collide(*mouse_pos): # the * break the tuple to 2 diffrant elements it like muose_pos[0], mouse_pos[1]
                targets.remove(target) #make it disappire afteer clicking it area
                target_pressed += 1

        if misses >= LIVES:
            end_screen(WIN,elapsed_time,target_pressed,misses) #end the game

        draw(WIN, targets)
        draw_top_bar(WIN,elapsed_time,target_pressed,misses)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()