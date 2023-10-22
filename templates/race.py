class Race():
    def __init__(self, name, strg, dex, intel, constit, charis, lifespan):
        self.name = name
        self.avg_strength = strg
        self.avg_dexterity = dex
        self.avg_intelligence = intel
        self.avg_constitution = constit
        self.avg_charisma = charis
        self.avg_lifespan = lifespan
        self.origin = []
        self.powers = []
        self.religious_preferences = {}
        self.terrain_preferences = {}
        self.occupation_preferences = {}
        self.racial_relationships = {}
        self.social_preferences = {}
        self.procreation_rate = None

