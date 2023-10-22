
class Industry:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Agriculture(Industry):
    def __init__(self):
        super().__init("Agriculture", "Cultivating magical crops and tending to mystical livestock for food and resources.")

class Blacksmithing(Industry):
    def __init__(self):
        super().__init("Blacksmithing", "Crafting weapons, armor, and tools from metals, often with magical enhancements.")

class Alchemy(Industry):
    def __init__(self):
        super().__init("Alchemy", "The mystical science of transforming substances, creating potions, and elixirs with magical properties.")

class Enchanting(Industry):
    def __init__(self):
        super().__init("Enchanting", "Infusing objects with magical spells and enhancements to improve their abilities.")

class Herbalism(Industry):
    def __init__(self):
        super().__init("Herbalism", "Gathering and cultivating magical herbs and plants for medicinal and mystical purposes.")

class PotionBrewing(Industry):
    def __init__(self):
        super().__init("Potion Brewing", "Creating potent brews and elixirs with various magical effects.")

class Printing(Industry):
    def __init__(self):
        super().__init("Printing", "Producing written materials.")

class Carpentry(Industry):
    def __init__(self):
        super().__init("Carpentry", "Crafting furniture, wooden structures, and magical wands and staves.")

class Tailoring(Industry):
    def __init__(self):
        super().__init("Tailoring", "Creating clothing, robes, and garments woven with enchanted threads and materials.")

class JewelryCrafting(Industry):
    def __init__(self):
        super().__init("Jewelry Crafting", "Designing and crafting magical amulets, rings, and talismans with mystical properties.")

class Pottery(Industry):
    def __init__(self):
        super().__init("Pottery", "Making enchanted pottery and ceramics for household and decorative use.")

class Brewing(Industry):
    def __init__(self):
        super().__init("Brewing", "Brewing magical ales, meads, and spirits with mystical ingredients and effects.")
class Engraving(Industry):
    def __init__(self):
        super().__init("Engraving", "Artistic etching and inscribing of runes, symbols, and magical sigils onto various surfaces.")

class Glassblowing(Industry):
    def __init__(self):
        super().__init("Glassblowing", "Crafting magical glassware, crystal balls, and enchanted lenses for scrying and divination.")

class Lapidary(Industry):
    def __init__(self):
        super().__init("Lapidary", "Cutting and shaping mystical gemstones and crystals for jewelry and artifacts.")

class Runecrafting(Industry):
    def __init__(self):
        super().__init("Runecrafting", "Carving magical runes onto stones, weapons, and objects to grant them unique properties.")

class Perfumery(Industry):
    def __init__(self):
        super().__init("Perfumery", "Creating enchanted perfumes and scents with mystical effects and alluring properties.")

class Bookbinding(Industry):
    def __init__(self):
        super().__init("Bookbinding", "Binding ancient tomes, grimoires, and spellbooks with protective and magical coverings.")

class Illumination(Industry):
    def __init__(self):
        super().__init("Illumination", "Decorating manuscripts with enchanted illustrations, enhancing their magical significance.")

class Clockmaking(Industry):
    def __init__(self):
        super().__init("Clockmaking", "Building magical timepieces, celestial clocks, and astrological devices.")

class Stonecutting(Industry):
    def __init__(self):
        super().__init("Stonecutting", "Shaping enchanted stones and crystals for architecture, monuments, and sculptures.")

class Tinkering(Industry):
    def __init__(self):
        super().__init("Tinkering", "Creating enchanted gadgets, devices, and contraptions with various magical functions.")

class Apothecary(Industry):
    def __init__(self):
        super().__init("Apothecary", "Preparing magical remedies, salves, and elixirs for healing and enhancement.")

class Mining(Industry):
    def __init__(self):
        super().__init("Mining", "Extracting magical ores, gemstones, and rare minerals from underground deposits.")

class Fishing(Industry):
    def __init__(self):
        super().__init("Fishing", "Harvesting creatures from waters for sustenance and magical ingredients.")


# Create instances of additional  industries
fishing = Fishing()
mining = Mining()
agriculture = Agriculture()
engraving = Engraving()
glassblowing = Glassblowing()
lapidary = Lapidary()
runecrafting = Runecrafting()
perfumery = Perfumery()
bookbinding = Bookbinding()
illumination = Illumination()
clockmaking = Clockmaking()
stonecutting = Stonecutting()
tinkering = Tinkering()
apothecary = Apothecary()

# Create instances of  industries
blacksmithing = Blacksmithing()
alchemy = Alchemy()
enchanting = Enchanting()
herbalism = Herbalism()
potion_brewing = PotionBrewing()
scribing = Scribing()
carpentry = Carpentry()
tailoring = Tailoring()
jewelry_crafting = JewelryCrafting()
pottery = Pottery()
brewing = Brewing()