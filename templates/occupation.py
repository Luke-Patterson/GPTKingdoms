class Occupation:
    def __init__(self, name, description, industry):
        self.name = name
        self.description = description
        self.industry = industry

class Blacksmith(Occupation):
    def __init__(self):
        super().__init("Blacksmith", "Crafts weapons, armor, and tools from metals, often with magical enhancements.", "Blacksmithing")

class Alchemist(Occupation):
    def __init__(self):
        super().__init("Alchemist", "Creates potions, elixirs, and performs transmutations with mystical ingredients.", "Alchemy")

class Enchanter(Occupation):
    def __init__(self):
        super().__init("Enchanter", "Infuses objects with magical spells and enhancements to improve their abilities.", "Enchanting")

class Herbalist(Occupation):
    def __init__(self):
        super().__init("Herbalist", "Gathers and cultivates magical herbs and plants for medicinal and mystical purposes.", "Herbalism")

class Scribe(Occupation):
    def __init__(self):
        super().__init("Scribe", "Records and writes records.", "Printing")

class Carpenter(Occupation):
    def __init__(self):
        super().__init("Carpenter", "Crafts furniture, wooden structures, and magical wands and staves.", "Carpentry")

class Tailor(Occupation):
    def __init__(self):
        super().__init("Tailor", "Creates clothing, robes, and garments woven with enchanted threads and materials.", "Tailoring")

class Jeweler(Occupation):
    def __init__(self):
        super().__init("Jeweler", "Designs and crafts magical amulets, rings, and talismans with mystical properties.", "Jewelry Crafting")

class Potter(Occupation):
    def __init__(self):
        super().__init("Potter", "Makes enchanted pottery and ceramics for household and decorative use.", "Pottery")

class Brewer(Occupation):
    def __init__(self):
        super().__init("Brewer", "Brews magical ales, meads, and spirits with mystical ingredients and effects.", "Brewing")

class Engraver(Occupation):
    def __init__(self):
        super().__init("Engraver", "Artistically etches and inscribes runes, symbols, and magical sigils onto various surfaces.", "Engraving")

class Glassblower(Occupation):
    def __init__(self):
        super().__init("Glassblower", "Crafts magical glassware, crystal balls, and enchanted lenses for scrying and divination.", "Glassblowing")

class Lapidary(Occupation):
    def __init__(self):
        super().__init("Lapidary", "Cuts and shapes mystical gemstones and crystals for jewelry and artifacts.", "Lapidary")

class Runecrafter(Occupation):
    def __init__(self):
        super().__init("Runecrafter", "Carves magical runes onto stones, weapons, and objects to grant them unique properties.", "Runecrafting")

class Perfumer(Occupation):
    def __init__(self):
        super().__init("Perfumer", "Creates enchanted perfumes and scents with mystical effects and alluring properties.", "Perfumery")

class Bookbinder(Occupation):
    def __init__(self):
        super().__init("Bookbinder", "Binds ancient tomes, grimoires, and spellbooks with protective and magical coverings.", "Bookbinding")

class Illuminator(Occupation):
    def __init__(self):
        super().__init("Illuminator", "Decorates manuscripts with enchanted illustrations, enhancing their magical significance.", "Illumination")

class Clockmaker(Occupation):
    def __init__(self):
        super().__init("Clockmaker", "Builds magical timepieces, celestial clocks, and astrological devices.", "Clockmaking")

class Stonecutter(Occupation):
    def __init__(self):
        super().__init("Stonecutter", "Shapes enchanted stones and crystals for architecture, monuments, and sculptures.", "Stonecutting")

class Tinker(Occupation):
    def __init__(self):
        super().__init("Tinker", "Creates enchanted gadgets, devices, and contraptions with various magical functions.", "Tinkering")

class Apothecarist(Occupation):
    def __init__(self):
        super().__init("Apothecarist", "Prepares magical remedies, salves, and elixirs for healing and enhancement.", "Apothecary")

class Miner(Occupation):
    def __init__(self):
        super().__init("Miner", "Delves into the depths of the earth to extract valuable magical resources.", "Mining")

class Gemcutter(Occupation):
    def __init__(self):
        super().__init("Gemcutter", "Cuts and polishes mystical gemstones for jewelry and magical artifacts.", "Mining")

class Fisherman(Occupation):
    def __init__(self):
        super().__init("Fisherman", "Nets and traps magical aquatic beings for food and spell components.", "Fishing")

# Create instances of the remaining occupations
fisherman = Fisherman()
miner = Miner()
gemcutter = Gemcutter()
engraver = Engraver()
glassblower = Glassblower()
lapidary = Lapidary()
runecrafter = Runecrafter()
perfumer = Perfumer()
bookbinder = Bookbinder()
illuminator = Illuminator()
clockmaker = Clockmaker()
stonecutter = Stonecutter()
tinker = Tinker()
apothecarist = Apothecarist()

# Create instances of the remaining occupations
potion_brewer = PotionBrewer()
scroll_scribe = ScrollScribe()
carpenter = Carpenter()
tailor = Tailor()
jeweler = Jeweler()
potter = Potter()
brewer = Brewer()

# Create instances of occupations
blacksmith = Blacksmith()
alchemist = Alchemist()
enchanter = Enchanter()
herbalist = Herbalist()
