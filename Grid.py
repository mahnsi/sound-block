import numpy as np
from vispy import scene
from vispy.color import Color

class Grid:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.active_key = None

        # list of all the positions in the grid
        positions = [[i,j,k] for i in range(self.x) for j in range(self.y) for k in range(self.z)]
        # corresponding list to define colour for each point. (0101 is green with full opacity)
        colors = [[0,1,0,1]] * len(positions)
        self.positions = np.array(positions)
        self.colors = np.array(colors)
        

    def _idx(self, x, y, z):
        # 3d coords --> index into colors array
        return x * self.y * self.z + y * self.z + z
    
    def draw(self, view):
        self.markers = scene.visuals.Markers(parent=view.scene)
        self.markers.set_data(self.positions, face_color=self.colors, size=10)
    
    def activate(self, x, y, z):
        key = (x, y, z)

        #deactivate the previously active point (if any) (change back to green)
        if self.active_key:
            self.colors[self._idx(*self.active_key)] = [0, 1, 0, 1]

        #activate a singular point (sphere) on the 3D graph. (colour it red)  
        idx = self._idx(x, y, z)
        self.colors[idx] = [1, 0, 0, 1]
        self.active_key = key
        self.markers.set_data(self.positions, face_color=self.colors, size=10)

