import librosa
import simpleaudio as sa
import soundfile as sf
def read_signal (path):
    return librosa.load (path)
def write_signal (path, signal, sample_rate):
    sf.write (path, signal, sample_rate)

def play_sound (filename_out):
    wave_obj = sa.WaveObject.from_wave_file(filename_out)
    play_obj = wave_obj.play()
    play_obj.wait_done()

