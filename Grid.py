from vispy import scene
from vispy.color import Color

class Grid:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.spheres = {}
        self.active_key = None
        # build grid
        # STTransform
        # plot each point

    def draw(self, view):
        # draw the grid on the given view, based on the axis values.
        for i in range(self.x):
            for j in range(self.y):
                for k in range(self.z):
                    # draw a sphere at point (i, j, k)
                    sphere = scene.visuals.Sphere(radius=0.4, method='latitude', parent=view.scene,
                        edge_color='black', color=(0, 1, 0, 1))

                    sphere.transform = scene.transforms.STTransform(translate=[i, j, k])
                    self.spheres[(i, j, k)] = sphere
        

    def activate(self, x, y, z):
        key = (x, y, z)

        #deactivate the previously active point (if any) (change back to green)
        if self.active_key and self.active_key in self.spheres:
            self.spheres[self.active_key].mesh.color = Color('green').rgba

        #activate a singular point (sphere) on the 3D graph. (colour it red)
        sphere = self.spheres.get((x, y, z))
        if sphere:
            self.spheres[key].mesh.color = Color('red').rgba
            self.active_key = key
        else:
            print(f"No sphere found at ({x}, {y}, {z})")
