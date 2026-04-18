class Harvest:
    def __init__(self, quantity, quality):
        self.quantity = quantity
        self.quality = quality

    def report(self):
        return f"Harvested {self.quantity} pineapples with {self.quality} quality."
