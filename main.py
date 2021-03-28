import graph
import sys
import processing as pc
import tasks
filename = "audio_files/test_file.wav"
filenameshort = "audio_files/short_file.wav"
filename_out = "audio_files/out.wav"
images_dir = "images/"
ndft = 256
noverlap = 84


if __name__ == '__main__':
    signal, sample_rate = tasks.first (filenameshort)
    tasks.done (1)
    tasks.second (signal, sample_rate, 0.1, filename_out, images_dir)
    tasks.done (2, "(You can look at signal plots in directory %s)" % (images_dir))


    starts, spec = pc.make_spectrogramm (signal, ndft, noverlap)
    graph.plot_spectrogramm (spec, sample_rate, len (signal), starts)
    graph.save (images_dir + "spectrogramm")
