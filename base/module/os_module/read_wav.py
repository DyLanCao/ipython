import wave
w = wave.open('/media/caoyin/work/igithub/ipython/base/module/os_module/test.wav', 'r')
for i in range(w.getnframes()):
    frame = w.readframes(i)
    print frame
