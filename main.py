from pineapple import Pineapple
from plantation import Plantation
from harvest import Harvest

pineapple = Pineapple("Queen", "Very Sweet", 1.2)
plantation = Plantation("Tropical Region", 50)
harvest = Harvest(1000, "High")

print(pineapple)
print(pineapple.taste())
print(plantation.describe())
print(harvest.report())
