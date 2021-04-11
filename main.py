import graph
import aio
import sys
import processing as pc
import tasks
im_dir = "images/"
audio_dir = "audio_files/"
filename = audio_dir + "test_file.wav"
filenameshort = audio_dir +  "short_file.wav"
filename_out = audio_dir + "out.wav"
ndft = 256
noverlap = 84
images_dir_message = "(You can look at signal plots in directory %s)" % (im_dir)
audio_dir_message = "(You can listen to original signal and signal with squeak in directory %s)" % (audio_dir)

frequency = 500
test_sample_rate = 4000
part = 0.5
test_out = audio_dir + "test.wav"

def test_filter (sig, sin_sig, freq, s_r):
    tasks.third_fourth (sig, ndft, noverlap, s_r, "orig")
    tasks.third_fourth (sig + sin_sig, ndft, noverlap, s_r, "orig_squeak")
    tasks.third_fourth (sin_sig, ndft, noverlap, s_r, "squeak")

    filtered = tasks.fivth (sig + sin_sig, freq, s_r)
    aio.write_signal ("right_here_is_okay.wav", filtered, s_r)
    aio.write_signal ("original_and_sqeak.wav",  sig + sin_sig, s_r)

    aio.write_signal ("squeak.wav", sin_sig, s_r)

    tasks.third_fourth (filtered, ndft, noverlap, s_r, "filtered")

    graph.draw_plot (sig)
    graph.save ("sig.png")
    graph.draw_plot (filtered)
    graph.save ("filtered.png")


if __name__ == '__main__':

    signal, sample_rate = tasks.first (filenameshort)
    tasks.done (1)

    sin_signal = pc.get_sin (signal, sample_rate, part, frequency)
    sec_sin_sig = pc.get_sin (signal, sample_rate, 0.1, 1000)

#    tasks.second (signal, sin_signal, sample_rate, filename_out)
#    tasks.done (2, images_dir_message +"\n" +  audio_dir_message)

#    tasks.third_fourth (signal, ndft, noverlap, sample_rate, "spectrogramm")
#    tasks.done (3, images_dir_message)

#    tasks.third_fourth (sin_signal, ndft, noverlap, sample_rate, "spec_of_diff")
#    tasks.done (4, images_dir_message)

    test_signal = aio.get_dialing_sound ()
#    tasks.third_fourth (test_signal, ndft, noverlap, sample_rate, "test")
#    tasks.done ("test3")
    import numpy as np
    tasks.third_fourth (test_signal, ndft, noverlap, sample_rate, "test")
    test_sin_signal = np.array (pc.get_sin_at (frequency, test_sample_rate, 7))
    tasks.third_fourth (test_sin_signal, ndft, noverlap, test_sample_rate, "test")
#    test_sin_signal = pc.get_sin (test_signal, test_sample_rate, part, frequency)

#    tasks.second (test_signal, test_sin_signal, test_sample_rate, test_out)
#    tasks.done ("test2")

    print (frequency)
    test_filter (test_signal
                 , test_sin_signal, frequency, test_sample_rate)


