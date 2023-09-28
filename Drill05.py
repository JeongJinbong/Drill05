import random
from pico2d import *

from move_character_with_mouse import handle_events

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hx, hy = random.randint(0,1200), random.randint(0,1150)
cx, cy = random.randint(0,1200), random.randint(0,1150)
frame = 0

def movetohand():
    global cx, cy
    global hx, hy
    global frame
    x1, y1 = cx, cy
    x2, y2 = hx, hy
    for i in range(0, 100, 1):
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand_arrow.draw(hx, hy)
        t = i/100
        movex = (1-t) * x1 + t * x2
        movey = (1-t) * y1 + t * y2
        if cx < hx:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, movex, movey)
        elif cx > hx:
            character.clip_draw(frame * 100, 0 * 1, 100, 100, movex, movey)
        update_canvas()
        frame = (frame + 1) % 8
        handle_events()
        delay(0.016)

while running:
    movetohand()
    update_canvas()
close_canvas()