from vispy import scene
class Grid:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
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

    def draw_sphere(self, view):
        # draw a sphere
        return scene.visuals.Sphere(radius=0.5, method='latitude', parent=view.scene,
                               edge_color='black')
        

    def activate(x, y, z):
        #activate a singular point (sphere) on the 3D graph.
        pass
