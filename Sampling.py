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


# Sample forest to agriculture change

ExtractMultiValuesToPoints("samplePoints","F2AChange","BILINEAR")
