import aio
import graph
import sys
import processing as pc
filename = "audio_files/test_file.wav"
filenameshort = "audio_files/short_file.wav"
filename_out = "audio_files/out.wav"
images_dir = "images/"
ndft = 256
noverlap = 84
def plot_all (signal, sin_signal):
    graph.draw_plot (signal)
    graph.save (images_dir + "data")
    graph.draw_plot (sin_signal)
    graph.save (images_dir + "noise")
    graph.draw_plot (sin_signal + signal)
    graph.save (images_dir + " data_noise")

if __name__ == '__main__':
    signal, sample_rate = aio.read_signal (filenameshort)
    signal = signal[:150000]
    sin_signal = pc.get_sin (signal, sample_rate, 0.1)

    plot_all (signal, sin_signal)


    starts, spec = pc.make_spectrogramm (signal, ndft, noverlap)

    graph.plot_spectrogramm (spec)
    graph.save (images_dir + "spectrogramm")
    aio.write_signal (filename_out, sin_signal + signal, sample_rate)
    aio.play_sound (filename_out)
