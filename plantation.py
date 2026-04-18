class Plantation:
    def __init__(self, location, size_hectares):
        self.location = location
        self.size_hectares = size_hectares

    def describe(self):
        return f"Plantation in {self.location} covering {self.size_hectares} hectares."
