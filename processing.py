import numpy as np
def get_sin (signal, sample_rate, desired_amplitude):
    samples = len (signal)
    volume = desired_amplitude
    freq = 400
    sinusoid = np.arange (float(samples))
    for index in range (samples):
        sinusoid[index] = np.sin (np.pi * index / samples)
    return (volume * sinusoid).astype(np.float32)



