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
pi025 = Math.atan2(1, 1)
maxColat = pi025 * 1.5
angleFactor = pi025 / 45

def on_forever():
    global joy
    joy = joystick()
    basic.clear_screen()
    led.plot(x1z * 2 + 2.5, y1z * 2 + 2.5)
basic.forever(on_forever)
