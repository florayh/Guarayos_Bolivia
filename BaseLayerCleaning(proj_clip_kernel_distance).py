import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "M:/Private/Guarayos"
env.scratchWorkspace = "M:/Private/Guarayos/GuarayosScratch.gdb"

# change projection to wgs 1984 utm20S
input_features = r"M:/Private/Guarayos/baseLayers/FILENAME"
output_feature_class = r"M:/Private/Guarayos/GuarayosScratch.gdb/FILENAME2"
out_coordinate_system = arcpy.SpatialReference("WGS 1984 UTM Zone 20S")
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)

# clip to Guarayos Buffer
in_feature = "FILENAME"
clip_feature = "M:/Private/Guarayos/GuarayosLandcover.gdb/GuarayosBuffer" 
out_feature = "M:/Private/Guarayos/GuarayosScratch.gdb/FILENAME2"
arcpy.Clip_analysis(in_feature,clip_feature,out_feature)

# Kernel density
arcpy.env.extent = "GuarayosBufferUTM"
in_feature = "FILENAME"
cellSize = 30
searchRadius = 8000
FILENAME2 = KernelDensity(in_feature, "NONE", cellSize, searchRadius)
## if result satisfying: 
FILENAME2.save = ("M:/Private/Guarayos/GuarayosLandcover.gdb/FILENAME2")


######################layers to work on:################################
# centros_poblados.shp - PopCenterUTM - PopCenterClip - PopCenterKer (cellSize: 30, searchRadius: 20000)
# rios_mayores.shp - MajRiverUTM - MajRiverClip - MajRiverLine - MajRiverKer (searchRadius: 15000)
# rios_minor: 5000
# distance to road: 20000

## population 
arcpy.env.extent = "GuarayosBufferUTM"
in_feature = "PopCenterClipUTM"
cellSize = 30
searchRadius = 20000
PopCenterKer = KernelDensity(in_feature, "NONE", cellSize, searchRadius)

## major rivers
input_features = r"M:/Private/Guarayos/GuarayosLandcover.gdb/MajRiverLine"
output_feature_class = r"M:/Private/Guarayos/GuarayosLandcover.gdb/MajRiverLineUTM"
out_coordinate_system = arcpy.SpatialReference("WGS 1984 UTM Zone 20S")
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)

arcpy.env.extent = "GuarayosBufferUTM"
in_feature = "MajRiverLineUTM"
cellSize = 30
searchRadius = 15000
MajRiverKer = KernelDensity(in_feature, "NONE", cellSize, searchRadius)

## minor rivers
# change projection 
input_features = r"M:/Private/Guarayos/baseLayers/rios_menor.shp"
output_feature_class = r"M:/Private/Guarayos/GuarayosLandcover.gdb/MinRiverUTM"
out_coordinate_system = arcpy.SpatialReference("WGS 1984 UTM Zone 20S")
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)

# clip to Guarayos Buffer
in_feature = "MinRiverUTM"
clip_feature = "M:/Private/Guarayos/GuarayosLandcover.gdb/GuarayosBufferUTM" 
out_feature = "M:/Private/Guarayos/GuarayosLandcover.gdb/MinRiverClip"
arcpy.Clip_analysis(in_feature,clip_feature,out_feature)

# Kernel density
arcpy.env.extent = "GuarayosBufferUTM"
in_feature = "MinRiverClip"
cellSize = 30
searchRadius = 5000
MinRiverKer = KernelDensity(in_feature, "NONE", cellSize, searchRadius)


## major roads
# change projection 
input_features = r"M:/Private/Guarayos/baseLayers/red_fundamental.shp"
output_feature_class = r"M:/Private/Guarayos/GuarayosLandcover.gdb/MajRoadsUTM"
out_coordinate_system = arcpy.SpatialReference("WGS 1984 UTM Zone 20S")
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)

# clip to Guarayos Buffer
in_feature = "MajRoadsUTM"
clip_feature = "M:/Private/Guarayos/GuarayosLandcover.gdb/GuarayosBufferUTM" 
out_feature = "M:/Private/Guarayos/GuarayosLandcover.gdb/MajRoadsClip"
arcpy.Clip_analysis(in_feature,clip_feature,out_feature)

# Kernel density
arcpy.env.extent = "GuarayosBufferUTM"
in_feature = "MajRoadsClip"
cellSize = 30
searchRadius = 20000
MajRoadsKer = KernelDensity(in_feature, "NONE", cellSize, searchRadius)


## INRA-TITULADO20 
input_features = r"M:/Private/Guarayos/baseLayers/INRA-TITULADO20.shp"
output_feature_class = r"M:/Private/Guarayos/GuarayosLandcover.gdb/InraUTM"
out_coordinate_system = arcpy.SpatialReference("WGS 1984 UTM Zone 20S")
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)

in_feature = "InraUTM"
clip_feature = "M:/Private/Guarayos/GuarayosLandcover.gdb/GuarayosBufferUTM" 
out_feature = "M:/Private/Guarayos/GuarayosLandcover.gdb/InraClip"
arcpy.Clip_analysis(in_feature,clip_feature,out_feature)

## PGMF 
input_features = r"M:/Private/Guarayos/baseLayers/PGMF.shp"
output_feature_class = r"M:/Private/Guarayos/GuarayosScratch.gdb/PgmfUTM"
out_coordinate_system = arcpy.SpatialReference("WGS 1984 UTM Zone 20S")
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)

in_feature = "PgmfUTM"
clip_feature = "M:/Private/Guarayos/GuarayosLandcover.gdb/GuarayosBufferUTM" 
out_feature = "M:/Private/Guarayos/GuarayosScratch.gdb/PgmfClip"
arcpy.Clip_analysis(in_feature,clip_feature,out_feature)

## plusII 
input_features = r"M:/Private/Guarayos/baseLayers/plusII.shp"
output_feature_class = r"M:/Private/Guarayos/GuarayosScratch.gdb/plusIIUTM"
out_coordinate_system = arcpy.SpatialReference("WGS 1984 UTM Zone 20S")
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)

in_feature = "plusIIUTM"
clip_feature = "M:/Private/Guarayos/GuarayosLandcover.gdb/GuarayosBufferUTM" 
out_feature = "M:/Private/Guarayos/GuarayosScratch.gdb/plusIIClip"
arcpy.Clip_analysis(in_feature,clip_feature,out_feature)

## plusII 
input_features = r"M:/Private/Guarayos/baseLayers/TPFP_modificado_limber.shp"
output_feature_class = r"M:/Private/Guarayos/GuarayosScratch.gdb/TpfpUTM"
out_coordinate_system = arcpy.SpatialReference("WGS 1984 UTM Zone 20S")
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)

in_feature = "TpfpUTM"
clip_feature = "M:/Private/Guarayos/GuarayosLandcover.gdb/GuarayosBufferUTM" 
out_feature = "M:/Private/Guarayos/GuarayosScratch.gdb/TpfpClip"
arcpy.Clip_analysis(in_feature,clip_feature,out_feature)


