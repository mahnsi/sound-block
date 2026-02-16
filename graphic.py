from vispy import scene
from vispy.visuals.transforms import STTransform
import Grid

from vispy import scene, app

class Visualizer:
    def __init__(self, grid, mapper, features, hop_length, sr):
        self.grid = grid
        self.mapper = mapper

        self.pitch, self.loudness, self.centroid = features
        self.length = min(len(self.pitch),
                          len(self.loudness),
                          len(self.centroid))

        self.frame_index = 0
        self.frame_duration = hop_length / sr

        self.canvas =  scene.SceneCanvas(keys='interactive', bgcolor = 'black', size=(800, 600), show=True)

        self.view = self.canvas.central_widget.add_view()
        self.view.camera = 'arcball'

        # create grid
        self.view.camera.set_range(x=[-1, grid.x+1],
                                   y=[-1, grid.y+1],
                                   z=[-1, grid.z+1])

        self.grid.draw(self.view)

        self.timer = app.Timer(
            interval=self.frame_duration,
            connect=self.update,
            start=True
        )

    def update(self, event):
        if self.frame_index >= self.length:
            self.timer.stop()
            return

        x, y, z = self.mapper.map_frame(
            self.pitch[self.frame_index],
            self.loudness[self.frame_index],
            self.centroid[self.frame_index]
        )

        self.grid.activate(x, y, z)
        self.frame_index += 1

    def run(self):
        #main event loop
        self.canvas.app.run()
