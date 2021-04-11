import graph
import processing as pc
import aio

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
    graph.plot_spectrogramm (spec, sample_rate, len (signal), starts)
    graph.save (images_dir + filename)

import scipy.signal as sl
def fivth (signal, frequency, sample_rate):
    wp = frequency
    ws = 0.9 * frequency
    gpass = 0.6
    gstop = 10
    order, wn = sl.cheb1ord (wp, ws, gpass, gstop, fs = sample_rate)
    sos = sl.cheby1 (order, 0.01, wn,
                     btype='highpass', fs = sample_rate, output =
                         'sos')
    filtered = sl.sosfilt (sos, signal)
    return filtered
