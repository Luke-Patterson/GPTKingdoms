class Religion:
    def __init__(self, name, description):
        self.name = name
        self.description = description

from templates.religion import Religion

class Polytheism(Religion):
    def __init__(self):
        super().__init("Polytheism", "Belief in multiple deities with distinct powers.")

class Monotheism(Religion):
    def __init__(self):
        super().__init("Monotheism", "Belief in a single, all-powerful deity.")

class Henotheism(Religion):
    def __init__(self):
        super().__init("Henotheism", "Acknowledgment of many deities but the worship of one primary deity.")

class Pantheism(Religion):
    def __init__(self):
        super().__init("Pantheism", "Belief that the divine is present in all things and the universe itself is divine.")

class Animism(Religion):
    def __init__(self):
        super().__init("Animism", "Belief in spiritual beings or souls in natural elements and living things.")

class Atheism(Religion):
    def __init__(self):
        super().__init("Atheism", "The absence of belief in deities or the supernatural.")

class Agnosticism(Religion):
    def __init__(self):
        super().__init("Agnosticism", "Uncertainty or lack of knowledge about the existence of deities.")

class Shamanism(Religion):
    def __init__(self):
        super().__init("Shamanism", "Spiritual practice involving communication with the spirit world, often through shamans or spiritual leaders.")

class Spiritualism(Religion):
    def __init__(self):
        super().__init("Spiritualism", "Eclectic beliefs often centered around personal growth, healing, and metaphysical concepts.")

class Cultism(Religion):
    def __init__(self):
        super().__init("Cultism", "Religions with secret rites and teachings.")

class Naturalism(Religion):
    def __init__(self):
        super().__init("Naturalism", "Worship and reverence for natural elements or the Earth itself.")

class Universalism(Religion):
    def __init__(self):
        super().__init("Universalism", "Belief in a universal truth or essence underlying all religions.")

# Create instances of each religion type
polytheism = Polytheism()
monotheism = Monotheism()
henotheism = Henotheism()
pantheism = Pantheism()
animism = Animism()
atheism = Atheism()
agnosticism = Agnosticism()
shamanism = Shamanism()
universalism = Universalism()
spiritualism = Spiritualism()
cultism = Cultism()
naturalism = Naturalism()