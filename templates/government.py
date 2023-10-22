
class Government():
    def __init__(self, type):
        self.type = type
from templates.government import Government
class DirectDemocracy(Government):
    def __init__(self):
        super().__init__("Direct Democracy")

class RepresentativeDemocracy(Government):
    def __init__(self):
        super().__init__("Representative Democracy")

class AbsoluteMonarchy(Government):
    def __init__(self):
        super().__init__("Absolute Monarchy")

class ConstitutionalMonarchy(Government):
    def __init__(self):
        super().__init__("Constitutional Monarchy")

class Autocracy(Government):
    def __init__(self):
        super().__init__("Autocracy")

class Totalitarianism(Government):
    def __init__(self):
        super().__init__("Totalitarianism")

class Oligarchy(Government):
    def __init__(self):
        super().__init__("Oligarchy")

class Theocracy(Government):
    def __init__(self):
        super().__init__("Theocracy")

class Communism(Government):
    def __init__(self):
        super().__init__("Communism")

class Socialism(Government):
    def __init__(self):
        super().__init__("Socialism")

class Fascism(Government):
    def __init__(self):
        super().__init__("Fascism")

class Federalism(Government):
    def __init__(self):
        super().__init__("Federalism")

class Confederation(Government):
    def __init__(self):
        super().__init__("Confederation")

class Anarchy(Government):
    def __init__(self):
        super().__init__("Anarchy")

class MilitaryDictatorship(Government):
    def __init__(self):
        super().__init__("Military Dictatorship")

class Meritocracy(Government):
    def __init__(self):
        super().__init__("Meritocracy")

class Technocracy(Government):
    def __init__(self):
        super().__init__("Technocracy")

class Plutocracy(Government):
    def __init__(self):
        super().__init__("Plutocracy")

class ParliamentarySystem(Government):
    def __init__(self):
        super().__init__("Parliamentary System")

class PresidentialSystem(Government):
    def __init__(self):
        super().__init__("Presidential System")

class SinglePartyState(Government):
    def __init__(self):
        super().__init__("Single-Party State")

class HybridSystems(Government):
    def __init__(self):
        super().__init__("Hybrid Systems")

class EDemocracy(Government):
    def __init__(self):
        super().__init__("E-democracy")

class TransitionalGovernment(Government):
    def __init__(self):
        super().__init__("Transitional Government")

# Create instances of each government type
direct_democracy = DirectDemocracy()
representative_democracy = RepresentativeDemocracy()
absolute_monarchy = AbsoluteMonarchy()
constitutional_monarchy = ConstitutionalMonarchy()
autocracy = Autocracy()
totalitarianism = Totalitarianism()
oligarchy = Oligarchy()
theocracy = Theocracy()
communism = Communism()
socialism = Socialism()
fascism = Fascism()
federalism = Federalism()
confederation = Confederation()
anarchy = Anarchy()
military_dictatorship = MilitaryDictatorship()
meritocracy = Meritocracy()
technocracy = Technocracy()
plutocracy = Plutocracy()
parliamentary_system = ParliamentarySystem()
presidential_system = PresidentialSystem()
single_party_state = SinglePartyState()
hybrid_systems = HybridSystems()
e_democracy = EDemocracy()
transitional_government = TransitionalGovernment()