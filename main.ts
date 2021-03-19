/**
 * Choose better variable names, comment code
 */
function joystick () {
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    z = input.acceleration(Dimension.Z)
    rxy = Math.sqrt(x * x + y * y)
    colatz = Math.atan2(rxy, 0 - z)
    colatz = Math.min(colatz / maxColat, 1)
    longiz = Math.atan2(y, x)
    x1z = colatz * Math.cos(longiz)
    y1z = colatz * Math.sin(longiz)
    return [x1z, y1z]
}
let score = 0
let pix = 0
let x0 = 0
let x1 = 0
let y0 = 0
let y1 = 0
let joy: number[] = []
let y1z = 0
let x1z = 0
let longiz = 0
let colatz = 0
let rxy = 0
let z = 0
let y = 0
let x = 0
let maxColat = 0
let drift = 0.04
let deltaDrift = 0.008
let maxDrift = 5
let wavelength = 1.5
let freq = -0.008
let gamma = 6
let pi025 = Math.atan2(1, 1)
maxColat = pi025 * 1.5
let angleFactor = pi025 / 45
basic.forever(function () {
    joy = joystick()
    for (let y2 = 0; y2 <= 4; y2++) {
        y1 = y2 - 2
        y0 += joy[1] * drift
        y1 += y0
        for (let x2 = 0; x2 <= 4; x2++) {
            x1 = x2 - 2
            x0 += joy[0] * drift
            x1 += x0
            rxy = Math.sqrt(x1 * x1 + y1 * y1)
            rxy += control.millis() * freq
            pix = (Math.sin(rxy / wavelength) ** 2) ** gamma
            if (x2 == 2 && y2 == 2) {
                pix = 255
            }
            led.plotBrightness(x2, y2, 255 * pix)
        }
    }
    if (x0 * x0 + y0 * y0 > maxDrift) {
        game.setScore(Math.floor(score / 50))
        game.gameOver()
    }
    score += 1
    drift += 0.00002
})
