from math import log, pow

A4 = 440
C0 = A4*pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
def pitch(freq):
    h = round(12*log(freq/C0))
    octave = h // 12
    n = h % 12
    n=int(n)
    print name[n]
    print octave




pitch(400)