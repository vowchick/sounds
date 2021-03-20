import aio
import sys
filename = "audio_files/test_file.wav"
filenameshort = "audio_files/short_file.wav"
filename_out = "audio_files/out.wav"

if __name__ == '__main__':
    signal, sample_rate = aio.read_signal (filename)

    aio.write_signal (filename_out, signal, sample_rate)
    aio.play_sound (filename_out)

