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

    length_in_sec = int (len (signal) / sample_rate) #get signal length in seconds
    sin_signal = np.array (pc.get_sin_at (frequency, sample_rate,
                                          length_in_sec))
    #cut signal and sin_signal and make them the same length
    sin_signal = sin_signal[:360000]
    signal = signal[:len (sin_signal)]

    tasks.second (signal, sin_signal, sample_rate, filename_out)
    tasks.done (2, images_dir_message +"\n" +  audio_dir_message)

    tasks.third_fourth (signal, ndft, noverlap, sample_rate, "spec_orig")
    tasks.done (3, images_dir_message)

    tasks.third_fourth (sin_signal, ndft, noverlap, sample_rate, "spec_sin_sig")
    tasks.done (4, images_dir_message)

    tasks.fivth_sixth (signal + sin_signal, frequency, sample_rate,
                       out_audio_dir + "filtered.wav", "spec_filtered.png",
                       ndft, noverlap)
    tasks.seventh_eight (signal, sample_rate, ndft, im_dir + "harmonics.png", noverlap)
    tasks.done (7)
    tasks.done (8)
    # x, y = pc.test_fft (sin_signal, sample_rate)
    # graph.draw_test_fft (x, y, len (signal))

