#wave data   -xlxw

#import
import wave as we
import numpy as np
import matplotlib.pyplot as plt
import sys

def wavread(path):
    wavfile =  we.open(path,"rb")
    params = wavfile.getparams()
    framesra,frameswav= params[2],params[3]
    nchannels, sampwidth, framesra, frameswav = params[:4]
    print("nchannels:%d" % nchannels)
    print("sampwidth:%d" % sampwidth)
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.fromstring(datawav,dtype = np.short)
    print(len(datause))
    if nchannels == 2:
        datause.shape = -1,2
    datause = datause.T
    time = np.arange(0, frameswav) * (1.0/framesra)
    return datause,time,nchannels

def main():
    path = sys.argv[1]
    #path = input("The Path is:")
    print(path)
    wavdata,wavtime,nchannels = wavread(path)
    
    N=len(wavdata)
    framerate = 16000
    start=0 
    df = 1 
    freq = [df*n for n in range(0,len(wavdata))] 
    print(len(wavdata))
    print(len(wavtime))
    
    c=np.fft.fft(wavdata)*nchannels
    d=int(len(c)/2)
    print(len(c))

    fig, ax = plt.subplots(2, 1)


    ax[0].plot(wavtime,wavdata,color = 'green')
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')


    ax[1].plot(freq,abs(c),color = 'red')
    ax[1].set_xlabel('Freq(HZ)')
    ax[1].set_ylabel('Y(freq)')
    
    plt.show()
    """
    while freq[d]>4:
        d-=10
        plt.plot(freq[:d-1],abs(c[:d-1]),'r')
        plt.show()

    
    if nchannels == 1:
        plt.title("Night.wav's Frames")
        plt.plot(wavtime, wavdata,color = 'green')
        plt.show()
    else:
        plt.subplot(211)
        plt.plot(wavtime, wavdata[0],color = 'green')
        plt.subplot(212)
        plt.plot(wavtime, wavdata[1])
        plt.show()
    """

main()
