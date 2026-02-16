import librosa as lr
import numpy as np

# n_fft is the number of samples in each FFT window. so the size of the window.
n_fft = 1024
# hop_length is how many samples the window moves forward in time for each step
hop_length = 256 
# the above combination is good for rapid updates and fine for no speech

sr = 44100  # standard sampling rate for audio

def preprocess_audio(path):
    # waveform is the audio signal as a numpy array (1D for now)
    # sr is the sampling rate which tells you how many times per second the audio wave is measured 
    # short-time Fourier transform
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
    # typically rms (root mean square) is used to measure loudness as it is direcly proportional to the amplitude.
    rms = lr.feature.rms(y=waveform, frame_length=n_fft, hop_length=hop_length)[0]
    print("RMS:", rms[:10])
    print("Min RMS:", np.min(rms))
    print("Max RMS:", np.max(rms))
    # convert to dB
    # dB scale makes it feel more like how we perceive changes in loudness
    # top_db is a parameter that limits how much dynamic range (in decibels) is displayed in the output. useful for ignoring very quiet sounds
    # ref is the reference value for the dB calculation.
    loudness_db = lr.amplitude_to_db(rms, ref=np.median(rms), top_db=None) # equivalent to 20 * log10(rms)   equivalent to power_to_db
    return loudness_db

def timbre(waveform):
    # spectral centroid is a measure of the "center of mass" of the spectrum, indicating where the center of the frequency distribution is located
    spectral_centroid = lr.feature.spectral_centroid(y=waveform, n_fft=n_fft, hop_length=hop_length)
    
    return spectral_centroid

def note_only(freq):
    pass

def pitch_octave_only(freq):
    pass


def normalize(arr):
    # normalize the array to the range [0, 1]
    arr_min = arr.min()
    arr_max = arr.max()
    return (arr - arr_min) / (arr_max - arr_min)


def extract_features(path):
    waveform, sr = preprocess_audio(path)
    #print(waveform[:100])
    print(np.max(np.abs(waveform)))

    f0 = estimate_pitch(waveform, sr)
    print(f"Estimated pitch (f0): {f0}")
    print("pitch to note:", lr.hz_to_note(f0))

    loudness_db = loudness(waveform)
    print(np.all(loudness_db == loudness_db[0]))
    print(f"Loudness (dB): {loudness_db}")

    #print("Min db:", np.min(loudness_db))
    #print("Max db:", np.max(loudness_db))
    #print(np.unique(loudness_db[:30]))

    spectral_centroid = timbre(waveform)
    print(f"Spectral centroid: {spectral_centroid}")

    return f0, loudness_db, spectral_centroid