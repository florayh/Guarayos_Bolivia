# Generalization of classified image
# Step 1. Majority Filter
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "M:/Private/Guarayos"
Majfilt07 = MajorityFilter("Guarayos2007Classified","EIGHT","HALF")
Majfilt17 = MajorityFilter("Guarayos2017Classified","EIGHT","HALF")

# Step 2. Boundary Clean

BndCln07 = BoundaryClean("Majfilt07","DESCEND","TWO_WAY")
BndCln17 = BoundaryClean("Majfilt17","DESCEND","TWO_WAY")
