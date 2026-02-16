from preprocess import *
from adapter import FeatureMapper
from Grid import Grid
from graphic import Visualizer

GRID_SIZE=8 #grid size
AUDIO_PATH = "MulberryMouse.mp3"

def main():
    #path = input("path to the audio file: ")
    f0, rms, spectral_centroid = extract_normalized_features(AUDIO_PATH)

    mapper = FeatureMapper(GRID_SIZE)
    grid = Grid(GRID_SIZE, GRID_SIZE, GRID_SIZE)

    visualizer = Visualizer(
        grid,
        mapper, (f0, rms, spectral_centroid),
        hop_length,
        sr
    )

    visualizer.run()

if __name__ == "__main__":
    main()