import numpy as np
def get_sin (signal, sample_rate, volume):
    samples = len (signal)
    freq = 10000
    sinusoid = np.arange (float(samples))
    for index in range (samples):
        sinus = np.sin (2 * freq * np.pi * index / samples)
        sinusoid[index] = sinus
    return (0.1 * volume * sinusoid).astype(np.float32)



