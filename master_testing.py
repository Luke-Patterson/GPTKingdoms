from master import MasterSimulation
from utils import gen_random_terrain_probs

m = MasterSimulation()
terrain_probs = gen_random_terrain_probs()
m.initiate_world(
    extrapolate_val = 5,
    x_start = 8,
    y_start = 8,
    terrain_probs = terrain_probs
)
m.world.map.to_csv("working/sample_map.csv")
pass