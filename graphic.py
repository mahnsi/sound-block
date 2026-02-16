from vispy import scene
from vispy.visuals.transforms import STTransform
import Grid
import time
import sounddevice as sd

from vispy import scene, app

class Visualizer:
    def __init__(self, grid, mapper, features, hop_length):
        self.grid = grid
        self.mapper = mapper

        self.waveform, self.sr, self.pitch, self.loudness, self.centroid, = features
        self.hop_length = hop_length
        
        self.length = min(len(self.pitch),
                          len(self.loudness),
                          len(self.centroid))

        self.start_time = None

        self.canvas =  scene.SceneCanvas(keys='interactive', bgcolor = 'black', size=(800, 600), show=True)

        self.view = self.canvas.central_widget.add_view()
        self.view.camera = 'arcball'

        # create grid
        self.view.camera.set_range(x=[-1, grid.x+1],
                                   y=[-1, grid.y+1],
                                   z=[-1, grid.z+1])

        self.grid.draw(self.view)

        self.timer = app.Timer(
                interval=0.01,
                connect=self.update,
                start=False)

    def start(self):
        sd.play(self.waveform, self.sr)
        self.start_time = time.time()
        self.timer.start()

    def update(self, event):
        if self.start_time is None:
            return

        elapsed = time.time() - self.start_time

        current_frame = int(
            elapsed * self.sr / self.hop_length
        )

        if current_frame >= self.length:
            self.timer.stop()
            return
        
        # map the current frame's features to grid coordinates 
        x, y, z = self.mapper.map_frame(
            self.pitch[current_frame],
            self.loudness[current_frame],
            self.centroid[current_frame]
        )

        #activate the corresponding point on the grid
        self.grid.activate(x, y, z)

    def run(self):
        self.start()
        #main event loop
        self.canvas.app.run()
