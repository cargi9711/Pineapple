class Pineapple:
    def __init__(self, variety, sweetness, weight):
        self.variety = variety
        self.sweetness = sweetness
        self.weight = weight

    def taste(self):
        return f"The {self.variety} pineapple tastes {self.sweetness}."

    def __str__(self):
        return f"{self.variety} | Sweetness: {self.sweetness} | Weight: {self.weight}kg"
