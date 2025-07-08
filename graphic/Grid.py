from vispy import scene
from vispy.color import Color

class Grid:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.spheres = {}
        # build grid
        # STTransform
        # plot each point

    def draw(self, view):
        # draw the grid on the given view, based on the axis values.
        for i in range(self.x):
            for j in range(self.y):
                for k in range(self.z):
                    # draw a point at (i, j, k)
                    sphere = self.draw_sphere(view)
                    sphere.transform = scene.transforms.STTransform(translate=[i, j, k])
                    self.spheres[(i, j, k)] = sphere


    def draw_sphere(self, view):
        # draw a sphere
        return scene.visuals.Sphere(radius=0.5, method='latitude', parent=view.scene,
                               edge_color='black', color=(0, 1, 0, 1))
        

    def activate(self, x, y, z):
        #activate a singular point (sphere) on the 3D graph. (colour it red)
        sphere = self.spheres.get((x, y, z))
        if sphere:
            new_color = Color('red').rgba
            sphere._mesh.color = new_color
            sphere.update()
        else:
            print(f"No sphere found at ({x}, {y}, {z})")
