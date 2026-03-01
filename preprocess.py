import librosa as lr
import numpy as np
import scipy.signal as signal

# n_fft is the number of samples in each FFT window. so the size of the window.
n_fft = 4096
# hop_length is how many samples the window moves forward in time for each step
hop_length = 256 

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

    fmin = lr.note_to_hz('C3')  
    fmax = lr.note_to_hz('C6')

    # YIN is a pitch estimation algorithm
    # f0 (fundamental frequency) will contain the detected pitc in Hz for each time frame a numpy array of size len(waveform) / hop_length
    f0 = lr.yin(waveform, fmin=fmin, fmax=fmax, sr=sr, frame_length=n_fft, hop_length=hop_length)
    
    f0[f0 > 1500] = np.nan # # anything above ~D6 is suspicious (heuristic)

    f0 = signal.medfilt(f0, kernel_size=5) # median filter to smooth out the pitch contour
    
    #pitch perception is logarithmic. midi is a linear perception scale, so this is better for a grid like ours. 
    pitch_midi = lr.hz_to_midi(f0)

    return pitch_midi

def estimate_pitch_v2(waveform, sr):
    fmin = lr.note_to_hz('C2')
    fmax = lr.note_to_hz('C7')
    
    # pyin returns f0, voiced_flag, and voiced_probabilities
    f0, voiced_flag, voiced_probs = lr.pyin(waveform, fmin=fmin, fmax=fmax, sr=sr, 
                                             frame_length=n_fft, hop_length=hop_length)
    # pyin sets unvoiced frames to nan automatically
    # optionally zero out low-confidence frames too
    f0[voiced_probs < 0.5] = np.nan
    return f0

def estimate_pitch_v3(waveform, sr):
    fmin = lr.note_to_hz('C2')
    fmax = lr.note_to_hz('C7')
    
    f0, voiced_flag, voiced_probs = lr.pyin(waveform, fmin=fmin, fmax=fmax, sr=sr,
                                             frame_length=n_fft, hop_length=hop_length)
    
    pitch_midi = lr.hz_to_midi(f0) 
    return pitch_midi

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

def estimate_timbre(waveform):
    # spectral centroid is a measure of the "center of mass" of the spectrum, indicating where the center of the frequency distribution is located
    spectral_centroid = lr.feature.spectral_centroid(y=waveform, n_fft=n_fft, hop_length=hop_length)[0]
    
    return spectral_centroid

def note_only(freq):
    pass

def pitch_octave_only(freq):
    pass


def normalize(arr):
    arr_min = np.nanmin(arr)
    arr_max = np.nanmax(arr)

    print ("Min:", arr_min)
    print ("Max:", arr_max)

    if arr_max == arr_min:
        return np.zeros_like(arr)
    normalized = (arr - arr_min) / (arr_max - arr_min)
    normalized[np.isnan(arr)] = 0  
    return normalized


def extract_features(path):
    waveform, sr = preprocess_audio(path)
    print(np.max(np.abs(waveform)))

    pitch = estimate_pitch(waveform, sr)
    #voiced = pitch < lr.note_to_hz('C7')
    #pitch_voiced = np.where(voiced, pitch, np.nan)

    print(f"Estimated pitch (f0): {pitch}")
    #print("pitch to note:", lr.hz_to_note(pitch))

    loudness_db = loudness(waveform)
    print(np.all(loudness_db == loudness_db[0]))
    print(f"Loudness (dB): {loudness_db}")

    #print("Min db:", np.min(loudness_db))
    #print("Max db:", np.max(loudness_db))
    #print(np.unique(loudness_db[:30]))

    timbre = estimate_timbre(waveform)
    print(f"Spectral centroid (timbre): {timbre}")

    return waveform, sr, pitch, loudness_db, timbre

def extract_normalized_features(path):
    # nomalizes pitch, loudness, and spectral centroid
    waveform, sr, pitch, loudness, timbre = extract_features(path)
    
    pitch = normalize(pitch)
    #print ("Normalized pitch:", pitch)
    loudness = normalize(loudness)
    timbre = normalize(timbre)

    return waveform, sr, pitch, loudness, timbre