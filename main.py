import graph
import aio
import sys
import processing as pc
import tasks
import numpy as np
im_dir = "images/"
in_audio_dir = "audio_files/in_files/"
out_audio_dir = "audio_files/out_files/"

filenameshorter = in_audio_dir +  "mr_sandman.wav"
filename_out = out_audio_dir + "sound_with_squeak.wav"

ndft = 512
noverlap = 84

images_dir_message = "(You can look at signal plots in directory %s)" % (im_dir)
audio_dir_message = "(You can listen to original signal and signal with squeak in directory %s)" % (out_audio_dir)


frequency = 2000

if __name__ == '__main__':

    signal, sample_rate = tasks.first (filenameshorter)
    tasks.done (1)
    print (sample_rate)
    graph.plot_transfer (sample_rate)
    length_in_sec = int (len (signal) / sample_rate)
    sin_signal = np.array (pc.get_sin_at (frequency, sample_rate,
                                          length_in_sec))
    sin_signal = sin_signal[:360000]
    signal = signal[:len (sin_signal)]
    tasks.second (signal, sin_signal, sample_rate, filename_out)
    tasks.done (2, images_dir_message +"\n" +  audio_dir_message)

    tasks.third_fourth (signal, ndft, noverlap, sample_rate, "spectrogramm")
    tasks.done (3, images_dir_message)

    tasks.third_fourth (sin_signal, ndft, noverlap, sample_rate, "spec_of_diff")
    tasks.done (4, images_dir_message)

    tasks.fivth_sixth (signal + sin_signal, frequency, sample_rate,
                       out_audio_dir + "filtered.wav", "filtered.png",
                       ndft, noverlap)
