import numpy as np
def get_sin (signal, sample_rate, volume):
    samples = len (signal)
    freq = 10000
    sinusoid = np.arange (float(samples))
    for index in range (samples):
        sinus = np.sin (2 * freq * np.pi * index / samples)
        sinusoid[index] = sinus
    return (volume * sinusoid).astype(np.float32)

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
