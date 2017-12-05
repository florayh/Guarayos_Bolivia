# Create sampling points within the Guarayos boundary (not the buffered boundary) 
import arcpy, os, random
from arcpy import env
from arcpy.sa import *
env.workspace = "M:/Private/Guarayos"
env.scratchWorkspace = "M:/Private/Guarayos/GuarayosScratch.gdb"


outGDB = "M:/Private/Guarayos/GuarayosLandcover.gdb"
outName = "samplePoints"
conFC = "TCO_GUARAYOS1prjwgs"
numPoints = 1000
arcpy.CreateRandomPoints_management(outGDB, outName, conFC, "", numPoints)

#Point/Line ->raster
## Sample forest to agriculture change
ExtractMultiValuesToPoints("samplePoints","F2A","BILINEAR")

## Population center kernel 
ExtractMultiValuesToPoints("samplePointsUTM","PopCenterKer","BILINEAR")

## Distance to major river kernel
ExtractMultiValuesToPoints("samplePointsUTM","MajRiverKer","BILINEAR")

## Distance to minor river kernel
ExtractMultiValuesToPoints("samplePointsUTM","MinRiverKer","BILINEAR")

## Distance to major roads kernel
ExtractMultiValuesToPoints("samplePointsUTM","MajRoadsKer","BILINEAR")

#Polygon
## Join the following to samplePoints mannually

## INRA-TITULADO20 (has year, type, owner etc. The best info available)
### Fields: (Fecha, Calificaci, Clasificac)
M:\Private\Guarayos\GuarayosScratchr.gdb\samplePoints_INRA

## PGMF: plan general de manejo forestal
### Fields: (Fecha, Tipo_Perso, Clase_Dere)
M:\Private\Guarayos\GuarayosScratchr.gdb\samplePoints_INRA_PGMF

## plusII: government required legal landuse?
### Fields: (Ley_Des)
M:\Private\Guarayos\GuarayosScratch.gdb\samplePoints_INRA_PGMF_PlusII

## TPFP: Tierras de produccion forestal permanente
### do the join as usual, then make "null" to 0 and the rest to 1

# 12/5 Re-do sampling:
# 1. Use adative sampling instead of random sampling
# 2. change the study area to original guarayos boundary instead of buffered boundary
outGDB = "M:/Private/Guarayos/GuarayosScratch.gdb"
outName = "samplePoints_Strata1"
conFC = "Bound1_Stratefied"
numPoints = 200
arcpy.CreateRandomPoints_management(outGDB, outName, conFC, "", numPoints)

outGDB = "M:/Private/Guarayos/GuarayosScratch.gdb"
outName = "samplePoints_Strata2"
conFC = "Bound2_Stratefied"
numPoints = 800
arcpy.CreateRandomPoints_management(outGDB, outName, conFC, "", numPoints)

arcpy.Merge_management(["samplePoints_Strata1","samplePoints_Strata2"],
                       "M:/Private/Guarayos/GuarayosLandcover.gdb/AdaptPoints") 

# 3. For major river and roads, use distance instead of kernel density
# 4. Resample all other layers 

## Distance to major river 
arcpy.Near_analysis("AdaptPoints","MajRiverLineUTM") #should I define a 10 km search radius

## Distance to major roads 
arcpy.Near_analysis("AdaptPoints","MajRoadsClip")

## Sample forest to agriculture change
ExtractMultiValuesToPoints("AdaptPoints","F2A","BILINEAR")

## Population center kernel 
ExtractMultiValuesToPoints("AdaptPoints","PopCenterKer","BILINEAR")

## Distance to minor river kernel
ExtractMultiValuesToPoints("AdaptPoints","MinRiverKer","BILINEAR")



#Polygon
## Join the following to samplePoints mannually

## INRA-TITULADO20 (has year, type, owner etc. The best info available)
### Fields: (Fecha, Calificaci, Clasificac)
M:\Private\Guarayos\GuarayosScratch.gdb\AdaptPoints_INRA

## PGMF: plan general de manejo forestal
### Fields: (Fecha, Tipo_Perso, Clase_Dere)
M:\Private\Guarayos\GuarayosScratch.gdb\samplePoints_INRA_PGMF


## plusII: government required legal landuse?
### Fields: (Ley_Des, renamed "Legal use")
M:\Private\Guarayos\GuarayosScratch.gdb\samplePoints_INRA_PGMF_PlusII

## TPFP: Tierras de produccion forestal permanente
### do the join as usual, then make "null" to 0 and the rest to 1


