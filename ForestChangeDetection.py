# Step 1. mask ranch, urban, and water for the 2007 and 2017 Guarayos classified map into the following values:
# forest: from 1 to 10
# agriculture: from 2 to 100 (2007) and 1000(2017)
# (mask all other values)
# ranch: from 3 to 0 (2007) and 1(2017)
# urban: from 4 to 0 (2007) and 1(2017)
# water: from 5 to 0 (2007) and 1(2017)
# no data: from 0 to 0 (2007) and 1 (2017) 
            
# so change can be determined by value after extraction:
# 2007       2017
# forest to agriculture: 990
# no change in forest: 0
# forest to something else: -9
# no change in agriculture: 900
# agriculture to something else: -99
# something else to forest: -10
# something else to agriculture: 1000 
# no change in something else: 1
# something else to something else: 1 


import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "M:/Private/Guarayos"
Reclass07 = Reclassify("Guarayos2007Classified", "Value",
                        RemapRange([[1,10],[2,100],[3,0],[4,0],[5,0],[0,0]]))
Reclass17 = Reclassify("Guarayos2017Classified", "Value",
                        RemapRange([[1,10],[2,1000],[3,1],[4,1],[5,1],[0,1]]))

# Step 2. subtraction; Reclassify the change map to reflect changes

subtract = Minus(Reclass17,Reclass07)

inRaster = "subtract"
reclassField = "Value" 
remap = RemapRange([[0,1],[990,2],[-9,0],[900,0],[-99,0],[-10,0],[1000,0],[1,0]])
ChangeMap = Reclassify(inRaster, reclassField, remap, "NODATA")
ChangeMap.save("M:/Private/Guarayos/GuarayosLandcover.gdb/ChangeMap")
