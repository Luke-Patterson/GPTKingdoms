
class Region():
    def __init__(self, name, description, world, symbol):
        self.name = name
        self.description = description
        self.world = world
        self.boundary_points = []
        self.symbol = symbol

class Forest(Region):
    def __init__(self, name, description, world):
        super().__init(name, description, world, "F")

class Mountain(Region):
    def __init__(self, name, description, world):
        super().__init(name, description, world, "M")

class Desert(Region):
    def __init__(self, name, description, world):
        super().__init(name, description, world, "D")

class Swamp(Region):
    def __init__(self, name, description, world):
        super().__init(name, description, world, "S")

class City(Region):
    def __init__(self, name, description, world):
        super().__init(name, description, world, "C")

class Ocean(Region):
    def __init__(self, name, description, world):
        super().__init(name, description, world, "O")

class Grassland(Region):
    def __init__(self, name, description, world):
        super().__init(name, description, world, "G")

class Tundra(Region):
    def __init__(self, name, description, world):
        super().__init(name, description, world, "T")

class Rainforest(Region):
    def __init__(self, name, description, world):
        super().__init(name, description, world, "R")

class Savanna(Region):
    def __init__(self, name, description, world):
        super().__init(name, description, world, "V")

region_types = {
    "Forest": Forest,
    "Mountain": Mountain,
    "Desert": Desert,
    "Swamp": Swamp,
    "City": City,
    "Ocean": Ocean,
    "Grassland": Grassland,
    "Tundra": Tundra,
    "Rainforest": Rainforest,
}

region_symbols = {
    "Forest": "F",
    "Mountain": "M",
    "Desert": "D",
    "Swamp": "S",
    "City": "C",
    "Ocean": "O",
    "Grassland": "G",
    "Tundra": "T",
    "Rainforest": "R",
}