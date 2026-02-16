import numpy as np

#maps the audio signal features to the 3d grid coordinates
class FeatureMapper:
    def __init__(self, grid_size):
        self.p = grid_size

    def map_frame(self, pitch, loudness, centroid):
        x = int(pitch * (self.p - 1))
        y = int(loudness * (self.p - 1))
        z = int(centroid * (self.p - 1))
        return x, y, z
