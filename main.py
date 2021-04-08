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

test_sample_rate = 4000
part = 0.1
test_out = audio_dir + "test.wav"

if __name__ == '__main__':

    signal, sample_rate = tasks.first (filenameshort)
    tasks.done (1)

    sin_signal = pc.get_sin (signal, sample_rate, part)

    tasks.second (signal, sin_signal, sample_rate, filename_out)
    tasks.done (2, images_dir_message +"\n" +  audio_dir_message)

    tasks.third(signal, ndft, noverlap, sample_rate)
    tasks.done (3, images_dir_message)

    test_signal = aio.get_dialing_sound ()
    tasks.third (test_signal, ndft, noverlap, sample_rate)
    tasks.done ("test3")

    test_sin_signal = pc.get_sin (test_signal, test_sample_rate, part)

    tasks.second (test_signal, test_sin_signal, test_sample_rate, test_out)
    tasks.done ("test2")
