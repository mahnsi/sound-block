import librosa as lr
path = input("path to the audio file: ")

def preprocess_audio(path):
    # waveform is the audio signal as a numpy array (1D for now)
    # sr is the sampling rate which tells you how many times per second the audio wave is measured 
    waveform, sr = lr.load(path, sr=44100, mono=True)