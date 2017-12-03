# Create sampling points within the Guarayos boundary (not the buffered boundary) 
import arcpy, os, random
from arcpy import env
from arcpy.sa import *
env.workspace = "M:/Private/Guarayos"

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


