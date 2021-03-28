import graph
import processing as pc
import aio

def done (number, message = ""):
    print (number, "task finished", message)
def first (f_name):
    return aio.read_signal (f_name)

def second (signal, sample_rate, part, f_out, i_dir):
    sin_signal = pc.get_sin (signal, sample_rate, part)
    aio.write_signal (f_out, sin_signal + signal, sample_rate)
    aio.play_sound (f_out)
    graph.plot_second_task_signals (signal, sin_signal, i_dir)




