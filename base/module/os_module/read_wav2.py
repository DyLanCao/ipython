import wave, struct

w = wave.read('test.wav', 'r')

length = waveFile.getnframes()
for i in range(0,20):
    waveData = waveFile.readframes(1)
    data = struct.unpack("<h", waveData)
    print(int(data[0]))
