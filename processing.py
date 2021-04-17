import numpy as np

#function to add squeak (sinusoid wave)

def get_sin (signal, sample_rate, volume, freq):
    samples = len (signal)
    sinusoid = np.arange (float(samples))
    for index in range (samples):
        sinus = np.sin (2 * freq * np.pi * index / samples)
        sinusoid[index] = sinus
    return (volume * sinusoid).astype(np.float32)


def get_sin_at (hz, sample_rate, length_in_sec):
    ## 1 sec length time series with sampling rate
    ts1sec = list (np.linspace (0, np.pi * 2 * hz, sample_rate))

    ## 1 sec length time series with sampling rate
    ts = ts1sec * int (length_in_sec)
    return (list (np.sin (ts)))

# functions for plotting spectrogramm

def get_xn(Xs, n):
    length = len (Xs)
    ks = np.arange (0, length, 1)
    xn = np.sum (Xs * np.exp ((1j * 2 * np.pi * ks * n) / length)) / length
    return xn

def get_all_xns (Xs):
    xns = []
    length = len (Xs)
    for i in range (int (length / 2)):
        xns.append (np.abs (get_xn (Xs, i)) * 2)
    return xns

def get_hz (k, sample_rate, length):
    return (float (sample_rate) * k.astype (float) / length).astype(int)

def make_spectrogramm (orig, ndft, noverlap = None):
    '''
       orig - original data
       ndft     - number of smamples used in each block for DFT
       noverlap - number of points that overlap between blocks.
    '''
    if noverlap is None:
        noverlap = ndft / 2
    noverlap = int (noverlap)

    starts = np.arange (0, len (orig), ndft - noverlap, dtype = int)
    # leave windows >= ndft sample size
    starts = starts[starts + ndft < len (orig)]
    xns = []
    for start in starts:
        # short dft
        window = get_all_xns (orig[start : start + ndft])
        xns.append (window)
    spec = np.array (xns).T
    #rescale (standard procedure)
    spec = 10 * np.log10 (spec)
    assert spec.shape[1] == len (starts)
    return (starts, spec)
