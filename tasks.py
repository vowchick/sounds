import graph
import processing as pc
import aio

images_dir = "images/"

def done (number, message = ""):
    print (number, "task finished", message)
def first (f_name):
    return aio.read_signal (f_name)

def second (signal, sample_rate, part, f_out):
    sin_signal = pc.get_sin (signal, sample_rate, part)
    aio.write_signal (f_out, sin_signal + signal, sample_rate)
    #aio.play_sound (f_out)
    graph.plot_second_task_signals (signal, sin_signal, images_dir)



def third (signal, ndft, noverlap, sample_rate):
    starts, spec = pc.make_spectrogramm (signal, ndft, noverlap)
    graph.plot_spectrogramm (spec, sample_rate, len (signal), starts)
    graph.save (images_dir + "spectrogramm")
