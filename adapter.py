import numpy as np

#maps the audio signal features to the 3d grid coordinates
class FeatureMapper:
    def __init__(self, grid):
        self.x = grid.x
        self.y = grid.y
        self.z = grid.z

    def map_frame(self, pitch, loudness, centroid):
        x = int(pitch * (self.x - 1))
        y = int(loudness * (self.y - 1))
        z = int(centroid * (self.z - 1))
        return x, y, z
