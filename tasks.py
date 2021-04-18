import graph
import processing as pc
import aio
import spec
images_dir = "images/"

def done (number, message = ""):
    print (number, "task finished", message)
def first (f_name):
    return aio.read_signal (f_name)

def second (signal, sin_signal, sample_rate, f_out):
    aio.write_signal (f_out, sin_signal + signal, sample_rate)
    #aio.play_sound (f_out)
    graph.plot_second_task_signals (signal, sin_signal, images_dir)

def third_fourth (signal, ndft, noverlap, sample_rate, filename):
    starts, spec = pc.make_spectrogramm (signal, ndft, noverlap)
    graph.plot_spectrogramm (spec, sample_rate, ndft, len (signal), starts)
    graph.save (images_dir + filename)

import scipy.signal as sl
def fivth_sixth (signal, frequency, sample_rate, aio_name, spec_name,
                ndft, noverlap):
    wp = [1850, 2200]
    ws = [1900, 2150]
    gpass = 0.1
    gstop = 1
    order, wn = sl.cheb1ord (wp, ws, gpass, gstop, fs = sample_rate)
    sos = sl.cheby1 (order, 1, wn,
                     btype='bandstop', output =
                         'sos', fs = sample_rate)
    filtered = sl.sosfiltfilt (sos, signal)

    aio.write_signal (aio_name, filtered, sample_rate)

    third_fourth (filtered, ndft, noverlap, sample_rate, spec_name)
    third_fourth (signal, ndft, noverlap, sample_rate, "spec_orig_and_sin")
