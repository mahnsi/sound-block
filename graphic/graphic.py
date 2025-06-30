from vispy import scene
from vispy.visuals.transforms import STTransform
import Grid

####### example #######
canvas = scene.SceneCanvas(keys='interactive', bgcolor = 'black', size=(800, 600), show=True)
view = canvas.central_widget.add_view()
view.camera = 'arcball'

# just 3 different ways to construct a sphere
sphere1 = scene.visuals.Sphere(radius=1, method='latitude', parent=view.scene,
                               edge_color='black')

sphere2 = scene.visuals.Sphere(radius=1, method='ico', parent=view.scene,
                               edge_color='black')

sphere3 = scene.visuals.Sphere(radius=1, rows=10, cols=10, depth=10,
                               method='cube', parent=view.scene,
                               edge_color='green')

# set the position of the spheres
sphere1.transform = STTransform(translate=[-2.5, 0, 0])
sphere3.transform = STTransform(translate=[2.5, 0, 0])

# set the camera range to fit the spheres
view.camera.set_range(x=[-3, 3])


canvas.app.run()
    