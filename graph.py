import matplotlib.pyplot as plt
import numpy as np
import processing as pc
def show ():
    plt.show ()

def draw_plot (signal):
    plt.plot (signal)

def save (path):
    plt.savefig (path)
    plt.clf ()

def plot_second_task_signals (signal, sin_signal, i_dir):
    draw_plot (signal)
    save (i_dir + "data")
    draw_plot (sin_signal)
    save (i_dir + "noise")
    draw_plot (sin_signal + signal)
    save (i_dir + " data_noise")

def plot_spectrogramm (spec, sample_rate, length, starts):
    plt.figure (figsize = (20, 8))
    plt_spec = plt.imshow (spec, origin = 'lower')
    total_ts_sec = int (length / sample_rate)
    ## configure y axis

    y_ticks = 10
    k = np.linspace (0, spec.shape[0], y_ticks)
    k_in_hz = pc.get_hz (k, sample_rate, length)
    plt.yticks (k, k_in_hz)
    plt.ylabel ("Hz")

    ## configure x axis

    x_ticks = 10

    ts_spec = np.linspace (0, spec.shape[1], x_ticks)
    ts_spec_sec  = ["{:4.2f}".format(i) for i in np.linspace(0, total_ts_sec *
                                                             starts[-1] /
                                                             length, x_ticks)]
    plt.xticks(ts_spec,ts_spec_sec)
    plt.xlabel("sec")
    plt.title ("Spectrogram L = {} Spectrogram.shape = {}".format (length,
                                                                   spec.shape))
    mappable = None
    plt.colorbar (mappable, use_gridspec = True)
