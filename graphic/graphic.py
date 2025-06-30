from vispy import scene
from vispy.visuals.transforms import STTransform
import Grid


canvas = scene.SceneCanvas(keys='interactive', bgcolor = 'black', size=(800, 600), show=True)
view = canvas.central_widget.add_view()
view.camera = 'arcball'

# create grid
p=8

grid = Grid.Grid(p, p, p)
grid.draw(view)

view.camera.set_range(x=[-p, p])

canvas.app.run()
