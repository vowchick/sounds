import graph
import processing as pc
import aio
import spec
images_dir = "images/"

def done (number, message = ""):
    print (number, "task finished", message)
def first (f_name):
    """
    returns audio file as two variables - first is an array and the 
    second one (sample rate) is a scalar
    """
    return aio.read_signal (f_name)

def second (signal, sin_signal, sample_rate, f_out):
    """
    1) Write sum of initial signal and sinusoid into .wav file
    2) Plot initial, sum and sin_signal (debug purposes) 
    """
    #1
    aio.write_signal (f_out, sin_signal + signal, sample_rate)
    #aio.play_sound (f_out)
    #2
    graph.plot_second_task_signals (signal, sin_signal, images_dir)

def third_fourth (signal, ndft, noverlap, sample_rate, filename):
    """
    1) Make spectrogramm
    2) Plot spectrogramm
    """
    #1
    starts, spec = pc.make_spectrogramm (signal, ndft, noverlap)
    #2
    graph.plot_spectrogramm (spec, sample_rate, ndft, len (signal), starts)
    graph.save (images_dir + filename)

import scipy.signal as sl
def fivth_sixth (signal, frequency, sample_rate, aio_name, spec_name,
                ndft, noverlap): 
    """
    1) Find Chebyshev filter parameters
    2) Apply Chebyshev filter with found parameters to get rid of noise
    3) Write filtered signal into .wav file
    4) Plot spectrogramm of filtered signal
    5) Plot spectrogramm of original signal with sinusoid
    """
    #1
    wp = [1850, 2200]
    ws = [1900, 2150]
    gpass = 0.1
    gstop = 1
    order, wn = sl.cheb1ord (wp, ws, gpass, gstop, fs = sample_rate)
    sos = sl.cheby1 (order, 1, wn,
                     btype='bandstop', output =
                         'sos', fs = sample_rate)
    #2                     
    filtered = sl.sosfiltfilt (sos, signal)
    #3
    aio.write_signal (aio_name, filtered, sample_rate)

    done (5)
    #4
    third_fourth (filtered, ndft, noverlap, sample_rate, spec_name)
    #5
    third_fourth (signal, ndft, noverlap, sample_rate, "spec_orig_and_sin")
    done (6)
def seventh_eight (signal, sample_rate, NFFT, path, noverlap = None):
    """
    1) Find harmonics
    2) Plot them
    """
    #1
    harmonics = pc.find_first_harmonic (signal, NFFT, sample_rate, noverlap)
    #2
    graph.plot_harmonics (harmonics, sample_rate, len (signal), path)

