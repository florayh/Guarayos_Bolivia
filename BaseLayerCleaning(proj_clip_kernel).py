# change projection to wgs 1984
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "M:/Private/Guarayos"
input_features = r"M:/Private/Guarayos/baseLayers/(FILENAME)"
output_feature_class = r"M:/Private/Guarayos/GuarayosLandcover.gdb/(NEW_FILENAME)"
out_coordinate_system = arcpy.SpatialReference("WGS 1984")
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)

# clip to Guarayos Buffer
in_feature = "FILENAME"
clip_feature = "M:/Private/Guarayos/GuarayosLandcover.gdb/GuarayosBuffer" 
out_feature = "New_FILENAME"
arcpy.Clip_analysis(in_feature,clip_feature,out_feature)

# Kernel density

