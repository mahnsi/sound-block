import librosa as lr
path = input("path to the audio file: ")

def preprocess_audio(path):
    # waveform is the audio signal as a numpy array (1D for now)
    # sr is the sampling rate which tells you how many times per second the audio wave is measured 
    waveform, sr = lr.load(path, sr=44100, mono=True)
    return waveform, sr

def estimate_pitch(waveform, sr):
    # pitch is the frequency of the audio signal in Hz

    # we are interested in the pitch range of a piano, which is from C2 to C7
    fmin = lr.note_to_hz('C2')  
    fmax = lr.note_to_hz('C7')

    # n_fft is the number of samples in each FFT window. so the size of the window.
    n_fft = 1024
    # hop_length is how many samples the window moves forward in time for each step
    hop_length = 256 
    # the above combination is good for rapid updates and fine for no speech

    # YIN is a pitch estimation algorithm
    # f0 will contain the detected pitch in Hz for each time frame a numpy array of size len(waveform) / hop_length
    f0 = lr.yin(waveform, fmin=fmin, fmax=fmax, sr=sr, hop_length=512)