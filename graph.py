import matplotlib.pyplot as plt
def show ():
    plt.show ()
def draw_plot (signal):
    plt.plot (signal)
def save (path):
    plt.savefig (path)
    plt.clf ()

def plot_spectrogramm (spec):
    plt.figure (figsize = (20, 8))
    plt_spec = plt.imshow (spec, origin = 'lower')
