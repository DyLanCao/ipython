import wave
import numpy as np

def stereoToMono(audiodata)
    newaudiodata = []

    for i in range(len(audiodata)):
        d = (audiodata[i][0] + audiodata[i][1])/2
            newaudiodata.append(d)

    return np.array(newaudiodata, dtype='int16')

f = wave.open(sys.argv[1], 'rb' )

wav.write(, sr, newaudiodata)
