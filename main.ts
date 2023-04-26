let on = 0
input.onGesture(Gesture.Shake, function () {
    on = 1
})
basic.forever(function () {
    if (on == 1) {
        basic.showIcon(IconNames.No)
        music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 5000, 228, 255, 255, 2000, SoundExpressionEffect.Vibrato, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
    }
})
basic.forever(function () {
    if (input.logoIsPressed()) {
        music.stopAllSounds()
        on = 0
        basic.showIcon(IconNames.Yes)
        basic.pause(5000)
        basic.clearScreen()
    }
})
