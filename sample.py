from generate_sinwave import output_sinwave

if __name__=="__main__":
    f0 = 440
    sec = 1
    fname = "440Hz.wav"
    sin_wave = output_sinwave(f0, sec, output_wave=True, wave_fname=fname)