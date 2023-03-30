function Figur2 () {
    FIGUR = 2
    if (Rotation2 == 1) {
        Figur_X1 = FIGUR_X
        Figur_Y1 = FIGUR_Y - 1
        Figur_X2 = FIGUR_X
        Figur_Y2 = FIGUR_Y
        Figur_X3 = FIGUR_X + 1
        Figur_Y3 = FIGUR_Y
    } else if (Rotation2 == 2) {
        Figur_X1 = FIGUR_X - 1
        Figur_Y1 = FIGUR_Y
        Figur_X2 = FIGUR_X
        Figur_Y2 = FIGUR_Y
        Figur_X3 = FIGUR_X
        Figur_Y3 = FIGUR_Y - 1
    } else if (Rotation2 == 3) {
        Figur_X1 = FIGUR_X
        Figur_Y1 = FIGUR_Y + 1
        Figur_X2 = FIGUR_X
        Figur_Y2 = FIGUR_Y
        Figur_X3 = FIGUR_X - 1
        Figur_Y3 = FIGUR_Y
    } else if (Rotation2 == 4) {
        Figur_X1 = FIGUR_X + 1
        Figur_Y1 = FIGUR_Y
        Figur_X2 = FIGUR_X
        Figur_Y2 = FIGUR_Y
        Figur_X3 = FIGUR_X
        Figur_Y3 = FIGUR_Y + 1
    } else {
    	
    }
}
function TouchPrüfung () {
    if (FIGUR == 1) {
        TpFig1()
    } else if (FIGUR == 2) {
        TpFig2()
    } else if (FIGUR == 3) {
        TpFig3()
    }
}
function GO () {
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
}
function TpFig1 () {
    if (Figur_Y1 == 4) {
        TOUCH = 1
    } else if (led.pointBrightness(Figur_X1, Figur_Y1 + 1) > 0) {
        TOUCH = 1
    } else {
    	
    }
}
input.onButtonPressed(Button.A, function () {
    if (MODE == 0) {
        basic.clearScreen()
        MODE = 5
    }
    if (MODE == 5) {
        if (FIGUR == 1) {
            if (Figur_X1 != 0) {
                FIGUR_X += -1
                Figur_1()
            }
        } else if (FIGUR == 2) {
            if (Rotation2 == 1 || Rotation2 == 4) {
                if (0 != Figur_X2) {
                    FIGUR_X += -1
                }
            } else if (Rotation2 == 2 || Rotation2 == 3) {
                if (0 != Figur_X2 - 1) {
                    FIGUR_X += -1
                }
            }
        } else if (FIGUR == 3) {
            if (Rotation2 == 1 || Rotation2 == 3) {
                if (Figur_X1 != 0) {
                    FIGUR_X += -1
                }
            } else if (Rotation2 == 2 || Rotation2 == 4) {
                if (Figur_X1 - 1 != 0) {
                    FIGUR_X += -1
                }
            }
        }
    }
})
function Figur_1 () {
    FIGUR = 1
    Figur_X1 = FIGUR_X
    Figur_Y1 = FIGUR_Y
    Figur_X2 = -5
    Figur_Y2 = -5
    Figur_X3 = -5
    Figur_Y3 = -5
}
function TpFig3 () {
    if (Figur_Y1 == 4 || Figur_Y2 == 4) {
        TOUCH = 1
    } else if (Rotation2 == 1 || Rotation2 == 3) {
        if (led.pointBrightness(Figur_X1, Figur_Y1 + 1) > 0) {
            TOUCH = 1
        }
    } else if (Rotation2 == 2 || Rotation2 == 4) {
        if (led.pointBrightness(Figur_X1, Figur_Y1 + 1) > 0) {
            TOUCH = 1
        } else if (led.pointBrightness(Figur_X2, Figur_Y2 + 1) > 0) {
            TOUCH = 1
        }
    } else {
    	
    }
}
// MODE:
// 
// 0: Menüpunkt: Home
// 
// 1: Menüpunkt (SKIP)
// 
// 2: Menüpunkt (SKIP)
// 
// 3: Menüpunkt (SKIP)
// 
// 4: JUMP -> 0
// 
// 5: TETRIS
function Figur_3 () {
    FIGUR = 3
    if (Rotation2 == 1 || Rotation2 == 3) {
        Figur_X1 = FIGUR_X
        Figur_Y1 = FIGUR_Y
        Figur_X2 = FIGUR_X
        Figur_Y2 = FIGUR_Y - 1
        Figur_X3 = -5
        Figur_Y3 = -5
    } else if (Rotation2 == 2 || Rotation2 == 4) {
        Figur_X1 = FIGUR_X
        Figur_Y1 = FIGUR_Y
        Figur_X2 = FIGUR_X - 1
        Figur_Y2 = FIGUR_Y
        Figur_X3 = -5
        Figur_Y3 = -5
    } else {
    	
    }
}
input.onButtonPressed(Button.AB, function () {
    if (MODE == 5) {
        Rotation2 += 1
        if (Rotation2 >= 4) {
            Rotation2 = 1
        }
        if (FIGUR == 1) {
        	
        } else if (FIGUR == 2) {
            Figur2()
        } else if (FIGUR == 3) {
            Figur_3()
        }
    }
})
function TpFig2 () {
    if (Figur_Y1 == 4) {
        TOUCH = 1
    } else if (Figur_Y2 == 4) {
        TOUCH = 1
    } else if (Figur_Y3 == 4) {
        TOUCH = 1
    } else if (Rotation2 == 1) {
        if (led.pointBrightness(Figur_X2, Figur_Y2 + 1) > 0) {
            TOUCH = 1
        } else if (led.pointBrightness(Figur_X3, Figur_Y3 + 1) > 0) {
            TOUCH = 1
        } else {
        	
        }
    } else if (Rotation2 == 2) {
        if (led.pointBrightness(Figur_X2, Figur_Y2 + 1) > 0) {
            TOUCH = 1
        } else if (led.pointBrightness(Figur_X1, Figur_Y1 + 1) > 0) {
            TOUCH = 1
        } else {
        	
        }
    } else if (Rotation2 == 3 || Rotation2 == 4) {
        if (led.pointBrightness(Figur_X3, Figur_Y3 + 1) > 0) {
            TOUCH = 1
        } else if (led.pointBrightness(Figur_X1, Figur_Y1 + 1) > 0) {
            TOUCH = 1
        } else {
        	
        }
    } else {
    	
    }
}
input.onButtonPressed(Button.B, function () {
    if (MODE != 5) {
        MODE += 1
    }
    if (MODE == 5) {
        if (FIGUR == 1) {
            if (Figur_X1 != 4) {
                FIGUR_X += 1
                Figur_1()
            }
        } else if (FIGUR == 2) {
            if (Rotation2 == 1 || Rotation2 == 4) {
                if (4 != Figur_X2 + 1) {
                    FIGUR_X += 1
                }
            } else if (Rotation2 == 2 || Rotation2 == 3) {
                if (4 != Figur_X2) {
                    FIGUR_X += 1
                }
            }
        } else if (FIGUR == 3) {
            if (Rotation2 == 1 || Rotation2 == 3) {
                if (Figur_X1 != 4) {
                    FIGUR_X += 1
                }
            } else if (Rotation2 == 2 || Rotation2 == 4) {
                if (Figur_X1 + 1 != 4) {
                    FIGUR_X += 1
                }
            }
        }
    }
})
function StartAnimation () {
    led.plot(0, 0)
}
function Tetris () {
    if (Shuffle == 1) {
        Figur_1()
    } else if (Shuffle == 2) {
        Figur2()
    } else if (Shuffle == 3) {
        Figur_3()
    }
    if (TOUCH >= 1) {
        OberGrenzPrüfung()
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
    } else {
        GO()
    }
    TouchPrüfung()
}
function OberGrenzPrüfung () {
	
}
let Figur_DelY3 = 0
let Figur_DelX3 = 0
let Figur_DelY2 = 0
let Figur_DelX2 = 0
let Figur_DelY1 = 0
let Figur_DelX1 = 0
let Figur_Y3 = 0
let Figur_X3 = 0
let Figur_Y2 = 0
let Figur_X2 = 0
let Figur_Y1 = 0
let Figur_X1 = 0
let FIGUR = 0
let FIGUR_X = 0
let FIGUR_Y = 0
let MODE = 0
let TOUCH = 0
let Rotation2 = 0
let Shuffle = 0
let Loop2 = 1
Shuffle = randint(1, 3)
Rotation2 = 1
TOUCH = 0
MODE = 0
FIGUR_Y = 0
FIGUR_X = 2
basic.forever(function () {
    if (MODE == 0) {
        StartAnimation()
    } else if (MODE == 1) {
        basic.clearScreen()
        MODE += 1
    } else if (MODE == 2) {
        basic.clearScreen()
        MODE += 1
    } else if (MODE == 3) {
        basic.clearScreen()
        MODE += 1
    } else if (MODE == 4) {
        basic.clearScreen()
        MODE = 0
    } else if (MODE == 5) {
        Tetris()
        basic.pause(700)
    }
})
