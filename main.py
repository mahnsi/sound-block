import numpy as np
from preprocess import estimate_pitch, loudness, preprocess_audio, timbre
from adapter import FeatureMapper
from Grid import Grid
from graphic import Visualizer

p=8 #grid size

def main():
    #path = input("path to the audio file: ")
    path = "MulberryMouse.mp3"
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

if __name__ == "__main__":
    main()