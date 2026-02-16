from preprocess import *
from adapter import FeatureMapper
from Grid import Grid
from graphic import Visualizer

GRID_SIZE=8 #grid size
AUDIO_PATH = "MulberryMouse.mp3"

def main():
    #path = input("path to the audio file: ")

    # extract features from the audio file
    waveform, sr, f0, rms, spectral_centroid = extract_normalized_features(AUDIO_PATH)

    # map the features to grid coordinates
    mapper = FeatureMapper(GRID_SIZE)
    # create the base grid
    grid = Grid(GRID_SIZE, GRID_SIZE, GRID_SIZE)

    # create the visualizer using the grid+mapping+audiofeatures
    visualizer = Visualizer(
        grid,
        mapper, (waveform, sr, f0, rms, spectral_centroid),
        hop_length
    )

    # main event loop (runs the visualization)
    visualizer.run()

if __name__ == "__main__":
    main()