import librosa
import simpleaudio as sa
import soundfile as sf
import numpy as np
def read_signal (path):
    return librosa.load (path)
def write_signal (path, signal, sample_rate):
    sf.write (path, signal, sample_rate)

def play_sound (filename_out):
    wave_obj = sa.WaveObject.from_wave_file(filename_out)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def get_signal_at (hz, sample_rate, length_in_sec):
    ## 1 sec length time series with sampling rate
    ts1sec = list (np.linspace (0, np.pi * 2 * hz, sample_rate))

    ## 1 sec length time series with sampling rate
    ts = ts1sec * length_in_sec
    return (list(np.sin(ts)))

def get_dialing_sound ():
    sample_rate = 4000
    length_in_sec = 3

    ## --------------------------------- ##
    ## 3 seconds of "digit 1" sound
    ## Pressing digit 2 buttom generates 
    ## the sine waves at frequency 
    ## 697Hz and 1209Hz.
    ## --------------------------------- ##
    ts1  = np.array(get_signal_at (697, sample_rate, length_in_sec))
    ts1 += np.array(get_signal_at (1209, sample_rate, length_in_sec))
    ts1  = list (ts1)

    ## -------------------- ##
    ## 2 seconds of silence
    ## -------------------- ##
    ts_silence = [0] * sample_rate * 1

    ## --------------------------------- ##
    ## 3 seconds of "digit 2" sounds 
    ## Pressing digit 2 buttom generates 
    ## the sine waves at frequency 
    ## 697Hz and 1336Hz.
    ## --------------------------------- ##
    ts2  = np.array (get_signal_at (697, sample_rate, length_in_sec))
    ts2 += np.array (get_signal_at (1336, sample_rate, length_in_sec))
    ts2  = list (ts2)

    ## -------------------- ##
    ## Add up to 7 seconds
    ## ------------------- ##
    ts = ts1 + ts_silence  + ts2
    return ts

