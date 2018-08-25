from matplotlib.mlab import find
import pyaudio
import numpy as np
import math


chunk = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 20


def Pitch(signal):
    signal = np.fromstring(signal, 'Int16');
    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing));
    f0=round(len(index) *RATE /(2*np.prod(len(signal))))
    return f0;


p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
channels = CHANNELS,
rate = RATE,
input = True,
output = True,
frames_per_buffer = chunk)

for i in range(0, RATE / chunk * RECORD_SECONDS):
    data = stream.read(chunk)
    Frequency=Pitch(data)
    print Frequency

    # if Frequency >= 16.00 and Frequency < 17.32:
    #     print "C0"
    # elif Frequency >= 17.00 and Frequency < 18.35:
    #     print " C#0/Db0"
    # elif Frequency >= 18.00 and Frequency < 19.45:
    #     print "D0"
    # elif Frequency >= 19.00 and Frequency < 20.60:
    #     print " D#0/Eb0"

