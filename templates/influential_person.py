class InfluentialPerson:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Politician(InfluentialPerson):
    def __init__(self, name):
        super().__init(name, "A person who holds a political office and influences government policies.")

class Scientist(InfluentialPerson):
    def __init__(self, name):
        super().__init(name, "A person who conducts scientific research and contributes to the advancement of knowledge.")

class Artist(InfluentialPerson):
    def __init__(self, name):
        super().__init(name, "A creative individual who expresses ideas and emotions through various art forms.")

class Scholar(InfluentialPerson):
    def __init__(self, name):
        super().__init(name, "A learned person who contributes to the fields of academia and education.")

class BusinessLeader(InfluentialPerson):
    def __init__(self, name):
        super().__init(name, "An individual who leads and influences business enterprises and economic activities.")

class ReligiousLeader(InfluentialPerson):
    def __init__(self, name):
        super().__init(name, "A figure who plays a central role in a religious community and guides spiritual beliefs.")

class General(InfluentialPerson):
    def __init__(self, name):
        super().__init(name, "Commander of armies.")

class Explorer(InfluentialPerson):
    def __init__(self, name):
        super().__init(name, "An adventurous traveler and discoverer of new lands or frontiers.")
