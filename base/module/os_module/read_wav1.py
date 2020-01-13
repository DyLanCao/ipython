import soundfile as sf
data, samplerate = sf.read('test.wav')
print samplerate
print data[0]
