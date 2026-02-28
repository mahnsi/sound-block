from vispy import scene
from vispy.visuals.transforms import STTransform
import Grid
import time
import sounddevice as sd
from adapter import FeatureMapper

from vispy import scene, app

class Visualizer:
    def __init__(self, grid_size, features, hop_length):
        self.grid = Grid.Grid(grid_size, grid_size, grid_size) # create grid
        self.mapper = FeatureMapper(self.grid.x) # map the features to grid coordinates

        self.waveform, self.sr, self.pitch, self.loudness, self.centroid, = features
        self.hop_length = hop_length
        
        # ensure we dont index beyond any array
        self.length = min(len(self.pitch),
                          len(self.loudness),
                          len(self.centroid))

        
        # creates window and OpenGL context
        self.canvas =  scene.SceneCanvas(keys='interactive', bgcolor = 'black', size=(800, 600), show=True)

        self.view = self.canvas.central_widget.add_view()
        self.view.camera = 'arcball'

        # range so we can see the full grid
        self.view.camera.set_range(x=[-1, self.grid.x+1],
                                   y=[-1, self.grid.y+1],
                                   z=[-1, self.grid.z+1])

        # draw the grid in the window
        self.grid.draw(self.view)

        self.timer = app.Timer(
                interval=0.01,
                connect=self.update, #calls update() every 10ms
                start=False)
        
        self.start_time = None

    def start(self):
        sd.play(self.waveform, self.sr) # play the audio file
        self.start_time = time.time() # record starting wall-clock time
        self.timer.start() # start the app.Timer to start periodically calling update()

    def update(self, event):
        if self.start_time is None:
            return

        elapsed = time.time() - self.start_time #eleapsed time since audio began

        current_frame = int(
            elapsed * self.sr #number of samples played so far
            / self.hop_length) #divided by hop length (number of feature frames so far)

        if current_frame >= self.length: #audio done
            self.timer.stop()
            return
        
        # map the current frame's features to grid coordinates 
        x, y, z = self.mapper.map_frame(
            self.pitch[current_frame], #left-right
            self.centroid[current_frame], #depth
            self.loudness[current_frame], #up-down 
        )

        #activate the corresponding point on the grid
        self.grid.activate(x, y, z)
        print("x y z:", x, y, z)

    def run(self):
        self.start()
        #main event loop
        self.canvas.app.run()
