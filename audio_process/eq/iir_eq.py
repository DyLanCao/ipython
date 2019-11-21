import zignal
x = zignal.Sinetone(fs=48000, f0=997, duration=0.1, gaindb=-20)
x.fade_out(millisec=10)
x.convert_to_float(targetbits=32)
x.write_wav_file("sinetone.wav")
#x.plot()
f = zignal.filters.biquads.RBJ(filtertype="peak", gaindb=-6, f0=997, Q=0.707, fs=96000)
f.plot_mag_phase()
#f.plot_pole_zero()
