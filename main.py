import numpy as np
from preprocess import estimate_pitch, loudness, preprocess_audio, timbre
from adapter import FeatureMapper
from Grid import Grid
from graphic import Visualizer

GRID_SIZE=8 #grid size

def main():
    mapper = FeatureMapper(GRID_SIZE)
    grid = Grid(GRID_SIZE, GRID_SIZE, GRID_SIZE)

    visualizer = Visualizer(
        grid,
        mapper,
        (f0, rms, centroid),
        hop_length,
        SR
    )

    visualizer.run()

if __name__ == "__main__":
    main()