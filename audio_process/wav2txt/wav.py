# -*- coding: utf-8 -*-
import wave
import matplotlib.pyplot as plt
import numpy as np
import sys


f = wave.open(sys.argv[1], 'rb' )
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

np.set_printoptions(threshold='nan')

Data_str = f.readframes(nframes)
Data_num = np.fromstring(Data_str,dtype=np.int16)
print(Data_num)
print(nframes)

np.savetxt(sys.argv[2],list(Data_num))
#b = np.fromfile(sys.argv[2], dtype=np.int32)
#print(b)
"""
fw =file(sys.argv[2],"w")
fw.write(str(list(Data_num)))

lines = fw.readline()
for line in lines:
    print(line)

fw.close()
"""
f.close()
