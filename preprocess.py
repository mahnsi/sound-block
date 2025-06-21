import librosa as lr

# n_fft is the number of samples in each FFT window. so the size of the window.
n_fft = 1024
# hop_length is how many samples the window moves forward in time for each step
hop_length = 256 
# the above combination is good for rapid updates and fine for no speech

def preprocess_audio(path):
    # waveform is the audio signal as a numpy array (1D for now)
    # sr is the sampling rate which tells you how many times per second the audio wave is measured 
    try:
        print(f"Loading audio file from: {path}")
        waveform, sr = lr.load(path, sr=44100, mono=True)
        return waveform, sr
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return None, None

def estimate_pitch(waveform, sr):
    print("Estimating pitch...")
    # pitch is the frequency of the audio signal in Hz

    # we are interested in the pitch range of a piano, which is from C2 to C7
    fmin = lr.note_to_hz('C2')  
    fmax = lr.note_to_hz('C7')

    # YIN is a pitch estimation algorithm
    # f0 (fundamental frequency) will contain the detected pitc in Hz for each time frame a numpy array of size len(waveform) / hop_length
    f0 = lr.yin(waveform, fmin=fmin, fmax=fmax, sr=sr, frame_length=n_fft, hop_length=hop_length)
    return f0

def loudness(waveform):
    # loudness is the perceived volume of the audio signal
    # typically rms (root mean square) is used to measure loudness
    rms = lr.feature.rms(y=waveform, frame_length=n_fft, hop_length=hop_length)

def timbre():
    spectral_centroid = []
    return spectral_centroid

def main():
    #path = input("path to the audio file: ")
    path = "MulberryMouse.mp3"
    waveform, sr = preprocess_audio(path)
    f0 = estimate_pitch(waveform, sr)
    print(f"Estimated pitch (f0): {f0}")

if __name__ == "__main__":
    main()