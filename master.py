from templates.world import World

class MasterSimulation():
    def __init__(self):
        self.world = None
        self.time = None

    def initiate_world(self, **kwargs):
        self.world = World()
        self.world.generate_map(**kwargs)