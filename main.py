on = 0

def on_gesture_shake():
    global on
    on = 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    if on == 1:
        basic.show_icon(IconNames.NO)
        music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                5000,
                228,
                255,
                255,
                2000,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LOGARITHMIC),
            SoundExpressionPlayMode.UNTIL_DONE)
basic.forever(on_forever)

def on_forever2():
    global on
    if input.logo_is_pressed():
        music.stop_all_sounds()
        on = 0
        basic.show_icon(IconNames.YES)
        basic.pause(5000)
        basic.clear_screen()
basic.forever(on_forever2)
