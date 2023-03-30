"""

MODE:

0: Menüpunkt: Home

1: Menüpunkt (SKIP)

2: Menüpunkt (SKIP)

3: Menüpunkt (SKIP)

4: JUMP -> 0

5: TETRIS

"""
def Figur_3():
    global FIGUR, Figur_X1, Figur_Y1, Figur_X2, Figur_Y2, Figur_X3, Figur_Y3
    FIGUR = 3
    if Rotation2 == 1 or Rotation2 == 3:
        Figur_X1 = FIGUR_X
        Figur_Y1 = FIGUR_Y
        Figur_X2 = FIGUR_X
        Figur_Y2 = FIGUR_Y - 1
        Figur_X3 = -5
        Figur_Y3 = -5
    else:
        if Rotation2 == 2 or Rotation2 == 4:
            Figur_X1 = FIGUR_X
            Figur_Y1 = FIGUR_Y
            Figur_X2 = FIGUR_X - 1
            Figur_Y2 = FIGUR_Y
            Figur_X3 = -5
            Figur_Y3 = -5
        else:
            pass
def Figur2():
    global FIGUR, Figur_X1, Figur_Y1, Figur_X2, Figur_Y2, Figur_X3, Figur_Y3
    FIGUR = 2
    if Rotation2 == 1:
        Figur_X1 = FIGUR_X
        Figur_Y1 = FIGUR_Y - 1
        Figur_X2 = FIGUR_X
        Figur_Y2 = FIGUR_Y
        Figur_X3 = FIGUR_X + 1
        Figur_Y3 = FIGUR_Y
    else:
        if Rotation2 == 2:
            Figur_X1 = FIGUR_X - 1
            Figur_Y1 = FIGUR_Y
            Figur_X2 = FIGUR_X
            Figur_Y2 = FIGUR_Y
            Figur_X3 = FIGUR_X
            Figur_Y3 = FIGUR_Y - 1
        else:
            if Rotation2 == 3:
                Figur_X1 = FIGUR_X
                Figur_Y1 = FIGUR_Y + 1
                Figur_X2 = FIGUR_X
                Figur_Y2 = FIGUR_Y
                Figur_X3 = FIGUR_X - 1
                Figur_Y3 = FIGUR_Y
            else:
                if Rotation2 == 4:
                    Figur_X1 = FIGUR_X + 1
                    Figur_Y1 = FIGUR_Y
                    Figur_X2 = FIGUR_X
                    Figur_Y2 = FIGUR_Y
                    Figur_X3 = FIGUR_X
                    Figur_Y3 = FIGUR_Y + 1
                else:
                    pass
def TouchPrüfung():
    if FIGUR == 1:
        TpFig1()
    else:
        if FIGUR == 2:
            TpFig2()
        else:
            if FIGUR == 3:
                TpFig3()
            else:
                pass
def TpFig1():
    global TOUCH
    if Figur_Y1 == 4:
        TOUCH = 1
    else:
        if led.point_brightness(Figur_X1, Figur_Y1 + 1) > 0:
            TOUCH = 1
        else:
            pass
def Tetris():
    global Shuffle, FIGUR_X, FIGUR_Y, Figur_DelX1, Figur_DelX2, Figur_DelX3, Figur_DelY1, Figur_DelY2, Figur_DelY3, TOUCH
    if Shuffle == 1:
        Figur_1()
    else:
        if Shuffle == 2:
            Figur2()
        else:
            if Shuffle == 3:
                Figur_3()
    if TOUCH >= 1:
        Shuffle = randint(1, 3)
        FIGUR_X = 2
        FIGUR_Y = 0
        Figur_DelX1 = -2
        Figur_DelX2 = -2
        Figur_DelX3 = -2
        Figur_DelY1 = -2
        Figur_DelY2 = -2
        Figur_DelY3 = -2
        TOUCH = 0
    else:
        GO()
    TouchPrüfung()

def on_button_pressed_a():
    global MODE, FIGUR_X
    if MODE == 0:
        basic.clear_screen()
        MODE = 5
    if MODE == 5:
        if FIGUR == 1:
            if Figur_X1 != 0:
                FIGUR_X += -1
                Figur_1()
        else:
            if FIGUR == 2:
                if Rotation2 == 1 or Rotation2 == 4:
                    if 0 != Figur_X2:
                        FIGUR_X += -1
                else:
                    if Rotation2 == 2 or Rotation2 == 3:
                        if 0 != Figur_X2 - 1:
                            FIGUR_X += -1
            else:
                if FIGUR == 3:
                    if Rotation2 == 1 or Rotation2 == 3:
                        if Figur_X1 != 0:
                            FIGUR_X += -1
                    else:
                        if Rotation2 == 2 or Rotation2 == 4:
                            if Figur_X1 - 1 != 0:
                                FIGUR_X += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def TpFig3():
    global TOUCH
    if Figur_Y1 == 4 or Figur_Y2 == 4:
        TOUCH = 1
    else:
        if Rotation2 == 1 or Rotation2 == 3:
            if led.point_brightness(Figur_X1, Figur_Y1 + 1) > 0:
                TOUCH = 1
        else:
            if Rotation2 == 2 or Rotation2 == 4:
                if led.point_brightness(Figur_X1, Figur_Y1 + 1) > 0:
                    TOUCH = 1
                else:
                    if led.point_brightness(Figur_X2, Figur_Y2 + 1) > 0:
                        TOUCH = 1
            else:
                pass
def GO():
    global FIGUR_Y, Figur_DelX1, Figur_DelX2, Figur_DelX3, Figur_DelY1, Figur_DelY2, Figur_DelY3
    FIGUR_Y += 1
    led.unplot(Figur_DelX1, Figur_DelY1)
    led.unplot(Figur_DelX2, Figur_DelY2)
    led.unplot(Figur_DelX3, Figur_DelY3)
    Figur_DelX1 = Figur_X1
    Figur_DelX2 = Figur_X2
    Figur_DelX3 = Figur_X3
    Figur_DelY1 = Figur_Y1
    Figur_DelY2 = Figur_Y2
    Figur_DelY3 = Figur_Y3
    led.plot(Figur_X1, Figur_Y1)
    led.plot(Figur_X2, Figur_Y2)
    led.plot(Figur_X3, Figur_Y3)
def Figur_1():
    global FIGUR, Figur_X1, Figur_Y1, Figur_X2, Figur_Y2, Figur_X3, Figur_Y3
    FIGUR = 1
    Figur_X1 = FIGUR_X
    Figur_Y1 = FIGUR_Y
    Figur_X2 = -5
    Figur_Y2 = -5
    Figur_X3 = -5
    Figur_Y3 = -5

def on_button_pressed_ab():
    global Rotation2
    if MODE == 5:
        Rotation2 += 1
        if Rotation2 >= 4:
            Rotation2 = 1
        if FIGUR == 1:
            pass
        else:
            if FIGUR == 2:
                Figur2()
            else:
                if FIGUR == 3:
                    Figur_3()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def TpFig2():
    global TOUCH
    if Figur_Y1 == 4:
        TOUCH = 1
    else:
        if Figur_Y2 == 4:
            TOUCH = 1
        else:
            if Figur_Y3 == 4:
                TOUCH = 1
            else:
                if Rotation2 == 1:
                    if led.point_brightness(Figur_X2, Figur_Y2 + 1) > 0:
                        TOUCH = 1
                    else:
                        if led.point_brightness(Figur_X3, Figur_Y3 + 1) > 0:
                            TOUCH = 1
                        else:
                            pass
                else:
                    if Rotation2 == 2:
                        if led.point_brightness(Figur_X2, Figur_Y2 + 1) > 0:
                            TOUCH = 1
                        else:
                            if led.point_brightness(Figur_X1, Figur_Y1 + 1) > 0:
                                TOUCH = 1
                            else:
                                pass
                    else:
                        if Rotation2 == 3 or Rotation2 == 4:
                            if led.point_brightness(Figur_X3, Figur_Y3 + 1) > 0:
                                TOUCH = 1
                            else:
                                if led.point_brightness(Figur_X1, Figur_Y1 + 1) > 0:
                                    TOUCH = 1
                                else:
                                    pass
                        else:
                            pass

def on_button_pressed_b():
    global MODE, FIGUR_X
    if MODE != 5:
        MODE += 1
    if MODE == 5:
        if FIGUR == 1:
            if Figur_X1 != 4:
                FIGUR_X += 1
                Figur_1()
        else:
            if FIGUR == 2:
                if Rotation2 == 1 or Rotation2 == 4:
                    if 4 != Figur_X2 + 1:
                        FIGUR_X += 1
                else:
                    if Rotation2 == 2 or Rotation2 == 3:
                        if 4 != Figur_X2:
                            FIGUR_X += 1
            else:
                if FIGUR == 3:
                    if Rotation2 == 1 or Rotation2 == 3:
                        if Figur_X1 != 4:
                            FIGUR_X += 1
                    else:
                        if Rotation2 == 2 or Rotation2 == 4:
                            if Figur_X1 + 1 != 4:
                                FIGUR_X += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def StartAnimation():
    led.plot(0, 0)
Figur_DelY3 = 0
Figur_DelY2 = 0
Figur_DelY1 = 0
Figur_DelX3 = 0
Figur_DelX2 = 0
Figur_DelX1 = 0
Figur_Y3 = 0
Figur_X3 = 0
Figur_Y2 = 0
Figur_X2 = 0
Figur_Y1 = 0
Figur_X1 = 0
FIGUR = 0
FIGUR_X = 0
FIGUR_Y = 0
MODE = 0
TOUCH = 0
Rotation2 = 0
Shuffle = 0
Loop2 = 1
Shuffle = randint(1, 3)
Rotation2 = 1
TOUCH = 0
MODE = 0
FIGUR_Y = 0
FIGUR_X = 2

def on_forever():
    global MODE
    if MODE == 0:
        StartAnimation()
    else:
        if MODE == 1:
            basic.clear_screen()
            MODE += 1
        else:
            if MODE == 2:
                basic.clear_screen()
                MODE += 1
            else:
                if MODE == 3:
                    basic.clear_screen()
                    MODE += 1
                else:
                    if MODE == 4:
                        basic.clear_screen()
                        MODE = 0
                    else:
                        if MODE == 5:
                            Tetris()
                            basic.pause(700)
                        else:
                            pass
basic.forever(on_forever)
