"""

Choose better variable names, comment code

"""
def joystick():
    global x, y, z, rxy, colatz, longiz, x1z, y1z
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    z = input.acceleration(Dimension.Z)
    rxy = Math.sqrt(x * x + y * y)
    colatz = Math.atan2(rxy, 0 - z)
    colatz = min(colatz / maxColat, 1)
    longiz = Math.atan2(y, x)
    x1z = colatz * Math.cos(longiz)
    y1z = colatz * Math.sin(longiz)
    return [x1z, y1z]
score = 0
pix = 0
x0 = 0
x1 = 0
y0 = 0
y1 = 0
joy: List[number] = []
y1z = 0
x1z = 0
longiz = 0
colatz = 0
rxy = 0
z = 0
y = 0
x = 0
maxColat = 0
drift = 0.04
deltaDrift = 0.008
maxDrift = 5
wavelength = 1.5
freq = -0.008
gamma = 6
pi025 = Math.atan2(1, 1)
maxColat = pi025 * 1.5
angleFactor = pi025 / 45

def on_forever():
    global joy, y1, y0, x1, x0, rxy, pix, score, drift
    joy = joystick()
    for y2 in range(5):
        y1 = y2 - 2
        y0 += joy[1] * drift
        y1 += y0
        for x2 in range(5):
            x1 = x2 - 2
            x0 += joy[0] * drift
            x1 += x0
            rxy = Math.sqrt(x1 * x1 + y1 * y1)
            rxy += control.millis() * freq
            pix = (Math.sin(rxy / wavelength) ** 2) ** gamma
            if x2 == 2 and y2 == 2:
                pix = 255
            led.plot_brightness(x2, y2, 255 * pix)
    if x0 * x0 + y0 * y0 > maxDrift:
        game.set_score(Math.floor(score / 50))
        game.game_over()
    score += 1
    drift += 0.00002
basic.forever(on_forever)
