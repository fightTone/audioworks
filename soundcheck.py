import winsound
import time

tonePin = 0

def delay(delayTime):
    time.sleep(delayTime/1000.0)

def tone(unused, freq, length, msg):
    print msg
    winsound.Beep(int(min(max(freq,28),32766)),int(length))

if __name__ == "__main__":
    tone(tonePin, 293, 231.480833333, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 391, 231.480833333, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 293, 694.4425, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 293, 115.740416667, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 293, 115.740416667, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 293, 231.480833333, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 391, 231.480833333, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 329, 925.923333333, "Playing Tone: 329 = E4 minus 3 cents")
    tone(tonePin, 329, 231.480833333, "Playing Tone: 329 = E4 minus 3 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 369, 925.923333333, "Playing Tone: 369 = F#4 minus 5 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 493, 925.923333333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 293, 231.480833333, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 391, 231.480833333, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 293, 925.923333333, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 293, 231.480833333, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 391, 231.480833333, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 329, 694.4425, "Playing Tone: 329 = E4 minus 3 cents")
    tone(tonePin, 329, 231.480833333, "Playing Tone: 329 = E4 minus 3 cents")
    tone(tonePin, 329, 231.480833333, "Playing Tone: 329 = E4 minus 3 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 659, 231.480833333, "Playing Tone: 659 = E5 minus 1 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 391, 694.4425, "Playing Tone: 391 = G4 minus 4 cents")
    delay(231.480833333)
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 462.961666667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 462.961666667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 391, 347.22125, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 440, 115.740416667, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 493, 925.923333333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 347.22125, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 115.740416667, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 115.740416667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 115.740416667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 462.961666667, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 587, 462.961666667, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 462.961666667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 462.961666667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 391, 347.22125, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 440, 115.740416667, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 493, 925.923333333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 347.22125, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 115.740416667, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 115.740416667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 115.740416667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 391, 231.480833333, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 783, 231.480833333, "Playing Tone: 783 = G5 minus 2 cents")
    delay(231.480833333)
    tone(tonePin, 293, 231.480833333, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 391, 231.480833333, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 293, 694.4425, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 293, 115.740416667, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 293, 115.740416667, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 293, 231.480833333, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 391, 231.480833333, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 329, 925.923333333, "Playing Tone: 329 = E4 minus 3 cents")
    tone(tonePin, 329, 231.480833333, "Playing Tone: 329 = E4 minus 3 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 369, 925.923333333, "Playing Tone: 369 = F#4 minus 5 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 493, 925.923333333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 293, 231.480833333, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 391, 231.480833333, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 293, 925.923333333, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 293, 231.480833333, "Playing Tone: 293 = D4 minus 4 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 391, 231.480833333, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 329, 694.4425, "Playing Tone: 329 = E4 minus 3 cents")
    tone(tonePin, 329, 231.480833333, "Playing Tone: 329 = E4 minus 3 cents")
    tone(tonePin, 329, 231.480833333, "Playing Tone: 329 = E4 minus 3 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 659, 231.480833333, "Playing Tone: 659 = E5 minus 1 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 391, 694.4425, "Playing Tone: 391 = G4 minus 4 cents")
    delay(231.480833333)
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 462.961666667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 462.961666667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 391, 347.22125, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 440, 115.740416667, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 493, 925.923333333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 347.22125, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 115.740416667, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 115.740416667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 115.740416667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 440, 462.961666667, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 587, 462.961666667, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 462.961666667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 462.961666667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 391, 347.22125, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 440, 115.740416667, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 493, 925.923333333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 347.22125, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 115.740416667, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 231.480833333, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 115.740416667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 493, 115.740416667, "Playing Tone: 493 = B4 minus 3 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 523, 231.480833333, "Playing Tone: 523 = C5 minus 1 cents")
    tone(tonePin, 440, 231.480833333, "Playing Tone: 440 = A4 plus 0 cents")
    tone(tonePin, 391, 231.480833333, "Playing Tone: 391 = G4 minus 4 cents")
    tone(tonePin, 587, 231.480833333, "Playing Tone: 587 = D5 minus 1 cents")
    tone(tonePin, 783, 231.480833333, "Playing Tone: 783 = G5 minus 2 cents")