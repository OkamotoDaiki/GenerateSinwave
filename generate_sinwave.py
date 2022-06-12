import numpy as np
import wave
import struct

def output_sinwave(f0, sec, A=1, fs=44100, output_wave=False, wave_fname="default.wav"):
    """
    Output sin-wave data array and wave file.

    Attributes:
        fo: Fundamental frequency
        sec: time
        A: amplitude
        fs: sampling rate
        output_wave: Boolean value of output
        
    Returns:
        sin_wave: sin wave of the range of amplitude
    """
    nframe = np.arange(0, fs*sec)
    sin_wave = A*np.sin(nframe*2*np.pi*f0/fs) #Generate sin wave

    convert_sin_wave = np.array(sin_wave * (2**15-1)).astype(np.int16) #Convert 16-bit signed integer.
    binary_sin_wave = struct.pack("h"*len(convert_sin_wave), *convert_sin_wave)

    if output_wave:
        #Output wave file.
        wave_write = wave.Wave_write(wave_fname)
        params = (1, 2, fs, len(sin_wave), 'NONE', 'not compressed')
        wave_write.setparams(params)
        wave_write.writeframes(binary_sin_wave)
        wave_write.close()
    return sin_wave