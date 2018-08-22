import audioop
import wave
import sys
import time

freq_e2 = 082.41     # frequency of the low E string in Hz
freq_a2 = 110.00     # frequency of the A string in Hz
freq_d3 = 146.83     # frequency of the D string in Hz
freq_g3 = 196.00     # frequency of the G string in Hz
freq_b3 = 246.94     # frequency of the B string in Hz
freq_e4 = 329.63     # frequency of the high E string in Hz
freq_curr =          # get frequency

while (freq_curr < freq_e2 - 5) or (freq_curr > freq_e2 + 5):
    if freq_curr < freq_e2:                                             # if too high
        freq_diff = freq_e2 - freq_curr                                 # calculate difference
        print("Too low:\t" + str(freq_curr))                            # output
    elif freq_curr > freq_e2:                                           # if too low
        freq_diff = freq_curr - freq_e2                                 # calculate difference
        print("Too high:\t" + str(freq_curr))                           # output
    time.sleep(0.1)                                                 # wait to prevent melting CPU
    print("E2 done!")                                                   # output
    freq_curr = # get frequency

while (freq_curr < freq_a2 - 5) or (freq_curr > freq_a2 + 5):
    if freq_curr < freq_a2:                                             # if too high
        freq_diff = freq_a2 - freq_curr                                 # calculate difference
        print("Too low:\t" + str(freq_curr))                            # output
    elif freq_curr > freq_a2:                                           # if too low
        freq_diff = freq_curr - freq_a2                                 # calculate difference
        print("Too high:\t" + str(freq_curr))                           # output
    time.sleep(0.1)                                                 # wait to prevent melting CPU
    print("A2 done!")                                                   # output
    freq_curr = # get frequency

while (freq_curr < freq_d3 - 5) or (freq_curr > freq_d3 + 5):
    if freq_curr < freq_d3:                                             # if too high
        freq_diff = freq_d3 - freq_curr                                 # calculate difference
        print("Too low:\t" + str(freq_curr))                            # output
    elif freq_curr > freq_d3:                                           # if too low
        freq_diff = freq_curr - freq_d3                                 # calculate difference
        print("Too high:\t" + str(freq_curr))                           # output
    time.sleep(0.1)                                                 # wait to prevent melting CPU
    print("D3 done!")                                                   # output
    freq_curr = # get frequency

while (freq_curr < freq_g3 - 5) or (freq_curr > freq_g3 + 5):
    if freq_curr < freq_g3:                                             # if too high
        freq_diff = freq_g3 - freq_curr                                 # calculate difference
        print("Too low:\t" + str(freq_curr))                            # output
    elif freq_curr > freq_g3:                                           # if too low
        freq_diff = freq_curr - freq_g3                                 # calculate difference
        print("Too high:\t" + str(freq_curr))                           # output
    time.sleep(0.1)                                                 # wait to prevent melting CPU
    print("G3 done!")                                                   # output
    freq_curr = # get frequency

while (freq_curr < freq_b3 - 5) or (freq_curr > freq_b3 + 5):
    if freq_curr < freq_b3:                                             # if too high
        freq_diff = freq_b3 - freq_curr                                 # calculate difference
        print("Too low:\t" + str(freq_curr))                            # output
    elif freq_curr > freq_b3:                                           # if too low
        freq_diff = freq_curr - freq_b3                                 # calculate difference
        print("Too high:\t" + str(freq_curr))                           # output
    time.sleep(0.1)                                                 # wait to prevent melting CPU
    print("B3 done!")                                                   # output
    freq_curr = # get frequency

while (freq_curr < freq_e4 - 5) or (freq_curr > freq_e4 + 5):
    if freq_curr < freq_e4:                                             # if too high
        freq_diff = freq_e4 - freq_curr                                 # calculate difference
        print("Too low:\t" + str(freq_curr))                            # output
    elif freq_curr > freq_e4:                                           # if too low
        freq_diff = freq_curr - freq_e4                                 # calculate difference
        print("Too high:\t" + str(freq_curr))                           # output
    time.sleep(0.1)                                                 # wait to prevent melting CPU
    print("E4 done!")                                                   # output
    freq_curr = # get frequency


sys.exit()  