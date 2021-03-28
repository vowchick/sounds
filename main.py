import graph
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


if __name__ == '__main__':
    signal, sample_rate = tasks.first (filenameshort)
    tasks.done (1)

    tasks.second (signal, sample_rate, 0.1, filename_out)
    tasks.done (2, images_dir_message +"\n" +  audio_dir_message)

    tasks.third(signal, ndft, noverlap, sample_rate)
    tasks.done (3, images_dir_message)
