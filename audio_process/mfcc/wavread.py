import scipy
from scipy.io import wavfile

import soundfile as sf

fs,data = wavfile.read("stop.wav")
print("sample:%d" % fs)
print(data)


data_sf, sample_rate = sf.read('stop.wav')

print("sound sample:%d" % sample_rate)
print(data_sf)

