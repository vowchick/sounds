import matplotlib.pyplot as plt
import numpy as np
import processing as pc
import scipy.signal as signal
def plot_transfer (sample_rate):
    wp = [1850, 2200]
    ws = [1900, 2150]
    gpass = 0.1
    gstop = 10
    order, wn = signal.cheb1ord (wp, ws, gpass, gstop, fs = sample_rate)
    b, a = signal.cheby1 (order, 1, wn,
                        btype='bandstop', fs = sample_rate)
    w, h = signal.freqz (b, a)
    x = w * sample_rate * 1.0 / (2 * np.pi)
    y = 20 * np.log10(abs(h))
    plt.figure(figsize=(10,5))
    plt.semilogx(x, y)
    plt.ylabel('Amplitude [dB]')
    plt.xlabel('Frequency [Hz]')
    plt.title('Frequency response')
    plt.grid(which='both', linestyle='-', color='grey')
    plt.xticks([20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000], ["20", "50", "100", "200", "500", "1K", "2K", "5K", "10K", "20K"])
    save("Here")
def show ():
    plt.show ()

def draw_plot (signal):
    plt.plot (signal)

def save (path):
    plt.savefig (path)
    plt.clf ()

def plot_harmonics (harmonics, sample_rate, length, path):
    m = length / sample_rate
    x_ticks = np.arange (0, m, m / len (harmonics))
    plt.plot (x_ticks, harmonics)
    plt.xlabel ("Sec")
    plt.ylabel ("Hz")
    save (path)

def plot_spectrogramm_builtin (x, sample_rate):
#     f, t, Sxx = signal.spectrogram (x, sample_rate)
#     plt.pcolormesh(t, f, Sxx, shading='gouraud')
#     plt.ylabel('Frequency [Hz]')
#     plt.xlabel('Time [sec]')
   powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(x,
                                                                  Fs=sample_rate)

   plt.xlabel('Time')

   plt.ylabel('Frequency')

def plot_second_task_signals (signal, sin_signal, i_dir):
    draw_plot (signal)
    save (i_dir + "data")
    draw_plot (sin_signal)
    save (i_dir + "noise")
    draw_plot (sin_signal + signal)
    save (i_dir + " data_noise")

def plot_spectrogramm (spec, sample_rate, length, length_sig, starts):
    plt.figure (figsize = (20, 8))
    plt_spec = plt.imshow (spec, origin = 'lower')
    total_ts_sec = int (length_sig / sample_rate)
    # configure y axis

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
                                                             length_sig, x_ticks)]
    plt.xticks(ts_spec,ts_spec_sec)
    plt.xlabel("sec")
    plt.title ("Spectrogram L = {} Spectrogram.shape = {}".format (length_sig,
                                                                   spec.shape))
    mappable = None
    plt.colorbar (mappable, use_gridspec = True)
def draw_test_fft (x, y, n):
    plt.plot (x, 2.0 / n * np.abs (y[0:n//2]))
    plt.grid()
    save ("fft_test.png")
